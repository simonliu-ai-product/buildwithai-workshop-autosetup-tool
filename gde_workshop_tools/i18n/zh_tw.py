STRINGS: dict[str, str] = {
    # ── App ──────────────────────────────────────────────────
    "app.title":                        "GDE Workshop Setup",

    # ── Runner ───────────────────────────────────────────────
    "runner.file_not_found":            "找不到步驟設定檔：",
    "runner.unknown_type":              "未知的步驟類型：",
    "runner.available_types":           "可用類型：",
    "runner.confirm_step":              "執行此步驟？",
    "runner.step_skipped":              "已跳過",
    "runner.step_completed":            "步驟完成",
    "runner.step_failed":               "步驟失敗，停止執行",
    "runner.all_done":                  "🎉  所有步驟完成！",
    "runner.dry_run_skip":              "(dry-run) 跳過執行",
    "runner.dry_run_done":              "(dry-run) 共列出 {total} 個步驟",

    # ── CLI verify ───────────────────────────────────────────
    "cli.verify.file_not_found":        "找不到步驟設定檔：",
    "cli.verify.manual_header":         "⚠  以下項目需人工確認",
    "cli.verify.all_passed":            "✔  自動驗證全部通過",
    "cli.verify.failed":                "✘  部分步驟驗證失敗，請依照提示修正後重新驗證",

    # ── UI ───────────────────────────────────────────────────
    "ui.input_title":                   "輸入",
    "ui.input_default_hint":            "直接按 Enter 使用預設值",
    "ui.command_title":                 "執行指令",

    # ── Language commands ────────────────────────────────────
    "lang.list_title":                  "支援的語言",
    "lang.col_code":                    "語言代碼",
    "lang.col_name":                    "名稱",
    "lang.col_current":                 "目前設定",
    "lang.current_marker":              "← 目前",
    "lang.set_success":                 "語言已設定為 {lang}（{name}）",
    "lang.invalid":                     "不支援的語言：{lang}",
    "lang.supported":                   "支援：{supported}",
    "lang.current":                     "目前語言：{lang}（{name}）",

    # ── Step descriptions ────────────────────────────────────
    "step.gemini_cli_vertex_auth.desc": "設定 Gemini CLI 使用 Vertex AI 認證（ADC）",
    "step.gcloud_auth.desc":            "Google Cloud 登入與專案設定",
    "step.gcloud_enable_apis.desc":     "啟用指定的 Google Cloud API",
    "step.gcp_billing_credit.desc":     "排查 GCP 專案是否已綁定 Workshop 促銷抵免額",
    "step.python_venv.desc":            "建立 Python 虛擬環境並安裝依賴套件",
    "step.shell.desc":                  "執行自訂 shell 指令",
    "step.base.no_verify":              "此步驟類型不支援驗證",

    # ── run: GeminiCliVertexAuth ─────────────────────────────
    "run.gemini.ask_project":           "請輸入 GOOGLE_CLOUD_PROJECT（GCP 專案 ID）",
    "run.gemini.ask_location":          "請輸入 GOOGLE_CLOUD_LOCATION",
    "run.gemini.project_empty":         "專案 ID 不能為空",
    "run.gemini.conflict_keys":         "偵測到衝突的環境變數：{keys}",
    "run.gemini.conflict_detail":       "使用 Vertex AI ADC 時需要先 unset 這些變數，否則可能導致認證失敗",
    "run.gemini.conflict_confirm":      "是否仍要繼續？",
    "run.gemini.cancelled":             "已取消",
    "run.gemini.written":               "已寫入 {path}：",

    # ── run: GCloudAuth ──────────────────────────────────────
    "run.gcloud_auth.ask_project":      "請輸入 GCP 專案 ID",
    "run.gcloud_auth.project_empty":    "專案 ID 不能為空",
    "run.gcloud_auth.set_project":      "設定專案：{project}",

    # ── run: GCloudEnableApis ────────────────────────────────
    "run.apis.none":                    "未指定任何 API，跳過",

    # ── run: GcpBillingCredit ────────────────────────────────
    "run.billing.manual_info":          "此步驟需要手動兌換 Workshop 促銷代碼，無法自動執行。",
    "run.billing.manual_link_label":    "請至以下連結兌換促銷代碼：",

    # ── run: PythonVenv ──────────────────────────────────────
    "run.venv.already_exists":          "虛擬環境 {venv_dir} 已存在，跳過建立",
    "run.venv.create_failed":           "建立虛擬環境失敗",
    "run.venv.created":                 "虛擬環境已建立：{venv_dir}",
    "run.venv.requirements_not_found":  "找不到 {requirements}",
    "run.venv.install_complete":        "依賴套件安裝完成",

    # ── run: Shell ───────────────────────────────────────────
    "run.shell.no_command":             "未指定 command 參數",
    "run.shell.complete":               "指令執行完成",
    "run.shell.failed":                 "指令失敗（exit code {code}）",

    # ── verify: GeminiCliVertexAuth ──────────────────────────
    "verify.gemini.env_exists":         "{path} 存在",
    "verify.gemini.env_not_found":      "{path} 不存在",
    "verify.gemini.project_set":        "GOOGLE_CLOUD_PROJECT 已設定",
    "verify.gemini.project_not_set":    "GOOGLE_CLOUD_PROJECT 未設定",
    "verify.gemini.location_set":       "GOOGLE_CLOUD_LOCATION 已設定",
    "verify.gemini.location_not_set":   "GOOGLE_CLOUD_LOCATION 未設定",
    "verify.gemini.adc_exists":         "Application Default Credentials 存在",
    "verify.gemini.adc_not_found":      "Application Default Credentials 不存在，請執行 gcloud auth application-default login",

    # ── verify: GCloudAuth ───────────────────────────────────
    "verify.gcloud_auth.logged_in":     "gcloud 已登入",
    "verify.gcloud_auth.not_logged_in": "gcloud 未登入，請執行 gcloud auth login",
    "verify.gcloud_auth.project_set":   "GCP 專案已設定",
    "verify.gcloud_auth.project_not_set": "GCP 專案未設定，請執行 gcloud config set project <PROJECT_ID>",

    # ── verify: GCloudEnableApis ─────────────────────────────
    "verify.apis.none_specified":       "未指定任何 API",
    "verify.apis.enabled":              "{api} 已啟用",
    "verify.apis.not_enabled":          "{api} 尚未啟用",
    "verify.apis.query_failed":         "{api}：無法查詢（請確認 gcloud 已登入並設定專案）",

    # ── verify: GcpBillingCredit ─────────────────────────────
    "verify.billing.no_project_id":     "無法取得 GCP 專案 ID，請先執行 gcloud config set project",
    "verify.billing.project":           "GCP 專案",
    "verify.billing.query_failed":      "無法查詢 Billing 狀態（請確認 gcloud 已登入）",
    "verify.billing.response_error":    "Billing API 回應格式異常",
    "verify.billing.not_enabled":       "專案尚未啟用 Billing，請至 Cloud Console 開啟",
    "verify.billing.enabled":           "Billing 帳號已綁定",
    "verify.billing.account_active":    "Billing 帳號正常啟用中",
    "verify.billing.account_inactive":  "Billing 帳號已關閉或暫停",
    "verify.billing.token_failed":      "無法取得 Access Token，請確認 gcloud 已登入",
    "verify.billing.manual_check":      "促銷抵免額需至 Cloud Console 人工確認",

    # ── verify: PythonVenv ───────────────────────────────────
    "verify.venv.not_found":            "虛擬環境 {venv_dir} 不存在",
    "verify.venv.exists":               "虛擬環境 {venv_dir} 存在",
    "verify.venv.pip_not_found":        "找不到 {pip_path}，虛擬環境可能損壞",
    "verify.venv.requirements_not_found": "找不到 {requirements}",
    "verify.venv.pip_check_passed":     "套件相依性正常（pip check 通過）",
    "verify.venv.pip_check_failed":     "套件相依性有問題",

    # ── verify: Shell ────────────────────────────────────────
    "verify.shell.no_command":          "shell 步驟未設定 verify_command，略過驗證",
    "verify.shell.passed":              "驗證指令通過",
    "verify.shell.failed":              "驗證指令失敗",
}
