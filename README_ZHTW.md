# bwai-workshop-tools

通用 Google Cloud Workshop 環境設定 CLI 工具。透過 JSON 步驟檔定義流程，一鍵完成所有設定。

**其他語言：** [English](README.md) | [日本語](README_JP.md) | [한국어](README_KO.md)

---

## 安裝

```bash
pip install bwai-workshop-tools
```

## 指令說明

### `bwai-workshop setup` — 執行設定流程

```bash
# 執行所有步驟（互動式逐步確認）
bwai-workshop setup --step path/to/config.json

# 只執行指定步驟（逗號分隔 ID）
bwai-workshop setup --step path/to/config.json --only auth,enable-apis

# 預覽步驟，不實際執行
bwai-workshop setup --step path/to/config.json --dry-run
```

### `bwai-workshop verify` — 驗證設定是否完成

```bash
# 驗證所有步驟
bwai-workshop verify --step path/to/config.json

# 只驗證指定步驟
bwai-workshop verify --step path/to/config.json --only auth,check-billing-credit
```

### `bwai-workshop language` — 管理顯示語言

```bash
# 列出支援的語言
bwai-workshop language list

# 設定語言
bwai-workshop language set zh-tw   # 繁體中文
bwai-workshop language set en      # English
bwai-workshop language set ja      # 日本語
bwai-workshop language set ko      # 한국어

# 查看目前語言
bwai-workshop language show
```

### `bwai-workshop steps list` — 列出步驟類型

```bash
bwai-workshop steps list
```

---

## 支援的步驟類型

| type | 說明 |
| :--- | :--- |
| `gemini_cli_vertex_auth` | 設定 Gemini CLI 使用 Vertex AI 認證（ADC） |
| `gcloud_auth` | Google Cloud 登入與專案設定 |
| `gcloud_enable_apis` | 啟用指定的 Google Cloud API |
| `gcp_billing_credit` | 排查 GCP 專案是否已綁定 Workshop 促銷抵免額 |
| `python_venv` | 建立 Python 虛擬環境並安裝依賴套件 |
| `shell` | 執行自訂 shell 指令 |

---

## 步驟檔格式

```json
{
  "name": "我的設定流程",
  "description": "說明文字",
  "steps": [
    {
      "id": "my-step",
      "type": "shell",
      "description": "執行自訂指令",
      "params": {
        "command": "echo hello"
      }
    }
  ]
}
```

## 範例

`examples/` 資料夾中有完整範例：

- `adk-gemini-agent.json` — ADK Gemini Agent Workshop 完整設定流程
