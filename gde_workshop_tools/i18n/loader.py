import json
from pathlib import Path
from functools import lru_cache

SUPPORTED_LANGUAGES: dict[str, str] = {
    "zh-tw": "繁體中文",
    "en":    "English",
    "ja":    "日本語",
    "ko":    "한국어",
}

CONFIG_PATH = Path("~/.config/gde-workshop/settings.json").expanduser()


def get_language() -> str:
    """讀取目前語言設定，預設為繁體中文"""
    if CONFIG_PATH.exists():
        try:
            with open(CONFIG_PATH) as f:
                return json.load(f).get("language", "zh-tw")
        except (json.JSONDecodeError, OSError):
            pass
    return "zh-tw"


def set_language(lang: str) -> None:
    """儲存語言設定"""
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_PATH, "w") as f:
        json.dump({"language": lang}, f)
    _get_strings.cache_clear()


@lru_cache(maxsize=4)
def _get_strings(lang: str) -> dict:
    """載入並快取指定語言的字串字典"""
    from . import zh_tw, en, ja, ko
    modules = {"zh-tw": zh_tw, "en": en, "ja": ja, "ko": ko}
    module = modules.get(lang, zh_tw)
    return getattr(module, "STRINGS", {})


def t(key: str, **kwargs) -> str:
    """取得翻譯字串；若找不到則 fallback 到繁體中文"""
    lang = get_language()
    strings = _get_strings(lang)
    fallback = _get_strings("zh-tw")
    text = strings.get(key) or fallback.get(key) or key
    return text.format(**kwargs) if kwargs else text
