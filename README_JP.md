# bwai-workshop-tools

Google Cloud Workshop 環境設定のための汎用 CLI ツールです。JSON ステップファイルでフローを定義し、すべての設定を一括完了できます。

**他の言語：** [English](README.md) | [繁體中文](README_ZHTW.md) | [한국어](README_KO.md)

---

## インストール

```bash
pip install bwai-workshop-tools
```

## コマンド

### `bwai-workshop setup` — セットアップの実行

```bash
# すべてのステップを実行（各ステップをインタラクティブに確認）
bwai-workshop setup --step path/to/config.json

# 指定したステップのみ実行（カンマ区切り ID）
bwai-workshop setup --step path/to/config.json --only auth,enable-apis

# ステップのプレビュー（実行なし）
bwai-workshop setup --step path/to/config.json --dry-run
```

### `bwai-workshop verify` — セットアップの検証

```bash
# すべてのステップを検証
bwai-workshop verify --step path/to/config.json

# 指定したステップのみ検証
bwai-workshop verify --step path/to/config.json --only auth,check-billing-credit
```

### `bwai-workshop language` — 表示言語の管理

```bash
# サポートされている言語の一覧
bwai-workshop language list

# 言語を設定
bwai-workshop language set ja      # 日本語
bwai-workshop language set en      # English
bwai-workshop language set zh-tw   # 繁體中文
bwai-workshop language set ko      # 한국어

# 現在の言語を表示
bwai-workshop language show
```

### `bwai-workshop steps list` — ステップタイプの一覧

```bash
bwai-workshop steps list
```

---

## サポートされているステップタイプ

| type | 説明 |
| :--- | :--- |
| `gemini_cli_vertex_auth` | Gemini CLI の Vertex AI 認証（ADC）を設定 |
| `gcloud_auth` | Google Cloud ログインとプロジェクト設定 |
| `gcloud_enable_apis` | 指定した Google Cloud API を有効化 |
| `gcp_billing_credit` | GCP プロジェクトの Workshop プロモーションクレジット確認 |
| `python_venv` | Python 仮想環境の作成と依存関係のインストール |
| `shell` | カスタム shell コマンドを実行 |

---

## ステップファイルの形式

```json
{
  "name": "マイセットアップフロー",
  "description": "説明テキスト",
  "steps": [
    {
      "id": "my-step",
      "type": "shell",
      "description": "カスタムコマンドを実行",
      "params": {
        "command": "echo hello"
      }
    }
  ]
}
```

## サンプル

`examples/` フォルダに完全なサンプルがあります：

- `adk-gemini-agent.json` — ADK Gemini Agent Workshop の完全セットアップフロー
