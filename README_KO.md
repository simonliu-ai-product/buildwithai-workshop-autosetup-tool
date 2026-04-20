# bwai-workshop-tools

Google Cloud Workshop 환경 설정을 위한 범용 CLI 도구입니다. JSON 단계 파일로 흐름을 정의하고 모든 설정을 한 번에 완료할 수 있습니다.

**다른 언어：** [English](README.md) | [繁體中文](README_ZHTW.md) | [日本語](README_JP.md)

---

## 설치

```bash
git clone https://github.com/simonliu-ai-product/buildwithai-workshop-autosetup-tool.git
cd buildwithai-workshop-autosetup-tool
pip install -e .
```

## 명령어

### `bwai-workshop setup` — 설정 실행

```bash
# 모든 단계 실행 (각 단계를 대화형으로 확인)
bwai-workshop setup --step path/to/config.json

# 지정한 단계만 실행 (쉼표로 구분된 ID)
bwai-workshop setup --step path/to/config.json --only auth,enable-apis

# 단계 미리보기 (실행 없이)
bwai-workshop setup --step path/to/config.json --dry-run
```

### `bwai-workshop verify` — 설정 검증

```bash
# 모든 단계 검증
bwai-workshop verify --step path/to/config.json

# 지정한 단계만 검증
bwai-workshop verify --step path/to/config.json --only auth,check-billing-credit
```

### `bwai-workshop language` — 표시 언어 관리

```bash
# 지원 언어 목록
bwai-workshop language list

# 언어 설정
bwai-workshop language set ko      # 한국어
bwai-workshop language set en      # English
bwai-workshop language set zh-tw   # 繁體中文
bwai-workshop language set ja      # 日本語

# 현재 언어 확인
bwai-workshop language show
```

### `bwai-workshop steps list` — 단계 유형 목록

```bash
bwai-workshop steps list
```

---

## 지원 단계 유형

| type | 설명 |
| :--- | :--- |
| `gemini_cli_vertex_auth` | Gemini CLI Vertex AI 인증(ADC) 설정 |
| `gcloud_auth` | Google Cloud 로그인 및 프로젝트 설정 |
| `gcloud_enable_apis` | 지정된 Google Cloud API 활성화 |
| `gcp_billing_credit` | GCP 프로젝트 Workshop 프로모션 크레딧 확인 |
| `python_venv` | Python 가상 환경 생성 및 의존성 설치 |
| `shell` | 커스텀 shell 명령 실행 |

---

## 단계 파일 형식

```json
{
  "name": "내 설정 흐름",
  "description": "설명 텍스트",
  "steps": [
    {
      "id": "my-step",
      "type": "shell",
      "description": "커스텀 명령 실행",
      "params": {
        "command": "echo hello"
      }
    }
  ]
}
```

## 예시

`examples/` 폴더에 완전한 예시가 있습니다:

- `adk-gemini-agent.json` — ADK Gemini Agent Workshop 전체 설정 흐름
