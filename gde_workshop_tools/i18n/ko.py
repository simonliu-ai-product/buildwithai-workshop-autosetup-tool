STRINGS: dict[str, str] = {
    # ── App ──────────────────────────────────────────────────
    "app.title":                        "GDE Workshop Setup",

    # ── Runner ───────────────────────────────────────────────
    "runner.file_not_found":            "단계 설정 파일을 찾을 수 없음: ",
    "runner.unknown_type":              "알 수 없는 단계 유형: ",
    "runner.available_types":           "사용 가능한 유형: ",
    "runner.confirm_step":              "이 단계를 실행할까요?",
    "runner.step_skipped":              "건너뜀",
    "runner.step_completed":            "단계 완료",
    "runner.step_failed":               "단계 실패, 실행 중단",
    "runner.all_done":                  "🎉  모든 단계가 완료되었습니다!",
    "runner.dry_run_skip":              "(dry-run) 건너뜀",
    "runner.dry_run_done":              "(dry-run) {total}개 단계 나열됨",

    # ── CLI verify ───────────────────────────────────────────
    "cli.verify.file_not_found":        "단계 설정 파일을 찾을 수 없음: ",
    "cli.verify.manual_header":         "⚠  다음 항목은 수동으로 확인이 필요합니다",
    "cli.verify.all_passed":            "✔  자동 검증 모두 통과",
    "cli.verify.failed":                "✘  일부 단계 실패. 수정 후 재검증하세요.",

    # ── UI ───────────────────────────────────────────────────
    "ui.input_title":                   "입력",
    "ui.input_default_hint":            "Enter로 기본값 사용",
    "ui.command_title":                 "명령 실행",

    # ── Language commands ────────────────────────────────────
    "lang.list_title":                  "지원 언어",
    "lang.col_code":                    "코드",
    "lang.col_name":                    "이름",
    "lang.col_current":                 "현재",
    "lang.current_marker":              "← 현재",
    "lang.set_success":                 "언어가 {lang}({name})로 설정됨",
    "lang.invalid":                     "지원하지 않는 언어: {lang}",
    "lang.supported":                   "지원: {supported}",
    "lang.current":                     "현재 언어: {lang} ({name})",

    # ── Step descriptions ────────────────────────────────────
    "step.gemini_cli_vertex_auth.desc": "Gemini CLI Vertex AI 인증(ADC) 설정",
    "step.gcloud_auth.desc":            "Google Cloud 로그인 및 프로젝트 설정",
    "step.gcloud_enable_apis.desc":     "지정된 Google Cloud API 활성화",
    "step.gcp_billing_credit.desc":     "GCP 프로젝트 Workshop 프로모션 크레딧 확인",
    "step.python_venv.desc":            "Python 가상 환경 생성 및 의존성 설치",
    "step.shell.desc":                  "커스텀 shell 명령 실행",
    "step.base.no_verify":              "이 단계 유형은 검증을 지원하지 않습니다",

    # ── run: GeminiCliVertexAuth ─────────────────────────────
    "run.gemini.ask_project":           "GOOGLE_CLOUD_PROJECT 입력 (GCP 프로젝트 ID)",
    "run.gemini.ask_location":          "GOOGLE_CLOUD_LOCATION 입력",
    "run.gemini.project_empty":         "프로젝트 ID는 비워둘 수 없습니다",
    "run.gemini.conflict_keys":         "충돌하는 환경 변수 감지: {keys}",
    "run.gemini.conflict_detail":       "Vertex AI ADC 사용 시 이 변수들을 unset해야 합니다",
    "run.gemini.conflict_confirm":      "계속 진행할까요?",
    "run.gemini.cancelled":             "취소됨",
    "run.gemini.written":               "{path}에 작성됨:",

    # ── run: GCloudAuth ──────────────────────────────────────
    "run.gcloud_auth.ask_project":      "GCP 프로젝트 ID 입력",
    "run.gcloud_auth.project_empty":    "프로젝트 ID는 비워둘 수 없습니다",
    "run.gcloud_auth.set_project":      "프로젝트 설정 중: {project}",

    # ── run: GCloudEnableApis ────────────────────────────────
    "run.apis.none":                    "API 미지정, 건너뜀",

    # ── run: GcpBillingCredit ────────────────────────────────
    "run.billing.manual_info":          "이 단계는 Workshop 프로모션 코드를 수동으로 교환해야 합니다.",
    "run.billing.manual_link_label":    "다음 링크에서 프로모션 코드를 교환하세요:",

    # ── run: PythonVenv ──────────────────────────────────────
    "run.venv.already_exists":          "가상 환경 {venv_dir} 이미 존재, 생성 건너뜀",
    "run.venv.create_failed":           "가상 환경 생성 실패",
    "run.venv.created":                 "가상 환경 생성됨: {venv_dir}",
    "run.venv.requirements_not_found":  "{requirements} 없음",
    "run.venv.install_complete":        "의존성 설치 완료",

    # ── run: Shell ───────────────────────────────────────────
    "run.shell.no_command":             "command 파라미터 미지정",
    "run.shell.complete":               "명령 실행 완료",
    "run.shell.failed":                 "명령 실패 (exit code {code})",

    # ── verify: GeminiCliVertexAuth ──────────────────────────
    "verify.gemini.env_exists":         "{path} 존재함",
    "verify.gemini.env_not_found":      "{path} 존재하지 않음",
    "verify.gemini.project_set":        "GOOGLE_CLOUD_PROJECT 설정됨",
    "verify.gemini.project_not_set":    "GOOGLE_CLOUD_PROJECT 미설정",
    "verify.gemini.location_set":       "GOOGLE_CLOUD_LOCATION 설정됨",
    "verify.gemini.location_not_set":   "GOOGLE_CLOUD_LOCATION 미설정",
    "verify.gemini.adc_exists":         "Application Default Credentials 존재함",
    "verify.gemini.adc_not_found":      "Application Default Credentials 없음. gcloud auth application-default login 실행 필요",

    # ── verify: GCloudAuth ───────────────────────────────────
    "verify.gcloud_auth.logged_in":     "gcloud 로그인됨",
    "verify.gcloud_auth.not_logged_in": "gcloud 미로그인. gcloud auth login 실행 필요",
    "verify.gcloud_auth.project_set":   "GCP 프로젝트 설정됨",
    "verify.gcloud_auth.project_not_set": "GCP 프로젝트 미설정. gcloud config set project <PROJECT_ID> 실행 필요",

    # ── verify: GCloudEnableApis ─────────────────────────────
    "verify.apis.none_specified":       "API 미지정",
    "verify.apis.enabled":              "{api} 활성화됨",
    "verify.apis.not_enabled":          "{api} 미활성화",
    "verify.apis.query_failed":         "{api}: 조회 불가 (gcloud 로그인 및 프로젝트 설정 확인)",

    # ── verify: GcpBillingCredit ─────────────────────────────
    "verify.billing.no_project_id":     "GCP 프로젝트 ID를 가져올 수 없음. gcloud config set project 먼저 실행",
    "verify.billing.project":           "GCP 프로젝트",
    "verify.billing.query_failed":      "Billing 상태 조회 불가 (gcloud 로그인 확인)",
    "verify.billing.response_error":    "Billing API 응답 형식 오류",
    "verify.billing.not_enabled":       "프로젝트 Billing 미활성화. Cloud Console에서 활성화 필요",
    "verify.billing.enabled":           "Billing 계정 연결됨",
    "verify.billing.account_active":    "Billing 계정 활성 상태",
    "verify.billing.account_inactive":  "Billing 계정 닫힘 또는 정지",
    "verify.billing.token_failed":      "Access Token 가져오기 실패. gcloud 로그인 확인",
    "verify.billing.manual_check":      "프로모션 크레딧은 Cloud Console에서 수동 확인 필요",

    # ── verify: PythonVenv ───────────────────────────────────
    "verify.venv.not_found":            "가상 환경 {venv_dir} 없음",
    "verify.venv.exists":               "가상 환경 {venv_dir} 존재함",
    "verify.venv.pip_not_found":        "{pip_path} 없음, 가상 환경이 손상되었을 수 있음",
    "verify.venv.requirements_not_found": "{requirements} 없음",
    "verify.venv.pip_check_passed":     "패키지 의존성 정상 (pip check 통과)",
    "verify.venv.pip_check_failed":     "패키지 의존성 문제 발견",

    # ── verify: Shell ────────────────────────────────────────
    "verify.shell.no_command":          "shell 단계에 verify_command 없음, 검증 건너뜀",
    "verify.shell.passed":              "검증 명령 통과",
    "verify.shell.failed":              "검증 명령 실패",
}
