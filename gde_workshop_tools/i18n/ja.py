STRINGS: dict[str, str] = {
    # ── App ──────────────────────────────────────────────────
    "app.title":                        "GDE Workshop Setup",

    # ── Runner ───────────────────────────────────────────────
    "runner.file_not_found":            "ステップ設定ファイルが見つかりません：",
    "runner.unknown_type":              "不明なステップタイプ：",
    "runner.available_types":           "利用可能なタイプ：",
    "runner.confirm_step":              "このステップを実行しますか？",
    "runner.step_skipped":              "スキップ",
    "runner.step_completed":            "ステップ完了",
    "runner.step_failed":               "ステップ失敗、実行を停止します",
    "runner.all_done":                  "🎉  すべてのステップが完了しました！",
    "runner.dry_run_skip":              "(dry-run) スキップ",
    "runner.dry_run_done":              "(dry-run) {total} ステップを一覧表示",

    # ── CLI verify ───────────────────────────────────────────
    "cli.verify.file_not_found":        "ステップ設定ファイルが見つかりません：",
    "cli.verify.manual_header":         "⚠  以下の項目は手動で確認が必要です",
    "cli.verify.all_passed":            "✔  すべての自動検証が通過しました",
    "cli.verify.failed":                "✘  一部のステップが失敗しました。修正後に再検証してください。",

    # ── UI ───────────────────────────────────────────────────
    "ui.input_title":                   "入力",
    "ui.input_default_hint":            "Enter で既定値を使用",
    "ui.command_title":                 "コマンド実行",

    # ── Language commands ────────────────────────────────────
    "lang.list_title":                  "サポートされている言語",
    "lang.col_code":                    "コード",
    "lang.col_name":                    "名前",
    "lang.col_current":                 "現在",
    "lang.current_marker":              "← 現在",
    "lang.set_success":                 "言語を {lang}（{name}）に設定しました",
    "lang.invalid":                     "サポートされていない言語：{lang}",
    "lang.supported":                   "サポート：{supported}",
    "lang.current":                     "現在の言語：{lang}（{name}）",

    # ── Step descriptions ────────────────────────────────────
    "step.gemini_cli_vertex_auth.desc": "Gemini CLI の Vertex AI 認証（ADC）を設定",
    "step.gcloud_auth.desc":            "Google Cloud ログインとプロジェクト設定",
    "step.gcloud_enable_apis.desc":     "指定した Google Cloud API を有効化",
    "step.gcp_billing_credit.desc":     "GCP プロジェクトの Workshop プロモーションクレジット確認",
    "step.python_venv.desc":            "Python 仮想環境の作成と依存関係のインストール",
    "step.shell.desc":                  "カスタム shell コマンドを実行",
    "step.base.no_verify":              "このステップタイプは検証をサポートしていません",

    # ── run: GeminiCliVertexAuth ─────────────────────────────
    "run.gemini.ask_project":           "GOOGLE_CLOUD_PROJECT を入力してください（GCP プロジェクト ID）",
    "run.gemini.ask_location":          "GOOGLE_CLOUD_LOCATION を入力してください",
    "run.gemini.project_empty":         "プロジェクト ID は空にできません",
    "run.gemini.conflict_keys":         "競合する環境変数が検出されました：{keys}",
    "run.gemini.conflict_detail":       "Vertex AI ADC を使用する際はこれらの変数を unset する必要があります",
    "run.gemini.conflict_confirm":      "それでも続行しますか？",
    "run.gemini.cancelled":             "キャンセルしました",
    "run.gemini.written":               "{path} に書き込みました：",

    # ── run: GCloudAuth ──────────────────────────────────────
    "run.gcloud_auth.ask_project":      "GCP プロジェクト ID を入力してください",
    "run.gcloud_auth.project_empty":    "プロジェクト ID は空にできません",
    "run.gcloud_auth.set_project":      "プロジェクトを設定中：{project}",

    # ── run: GCloudEnableApis ────────────────────────────────
    "run.apis.none":                    "API が指定されていません。スキップします",

    # ── run: GcpBillingCredit ────────────────────────────────
    "run.billing.manual_info":          "このステップは Workshop プロモーションコードの手動引き換えが必要です。",
    "run.billing.manual_link_label":    "以下のリンクでプロモーションコードを引き換えてください：",

    # ── run: PythonVenv ──────────────────────────────────────
    "run.venv.already_exists":          "仮想環境 {venv_dir} は既に存在します。作成をスキップします",
    "run.venv.create_failed":           "仮想環境の作成に失敗しました",
    "run.venv.created":                 "仮想環境が作成されました：{venv_dir}",
    "run.venv.requirements_not_found":  "{requirements} が見つかりません",
    "run.venv.install_complete":        "依存関係のインストールが完了しました",

    # ── run: Shell ───────────────────────────────────────────
    "run.shell.no_command":             "command パラメータが指定されていません",
    "run.shell.complete":               "コマンドが正常に実行されました",
    "run.shell.failed":                 "コマンドが失敗しました（exit code {code}）",

    # ── verify: GeminiCliVertexAuth ──────────────────────────
    "verify.gemini.env_exists":         "{path} が存在します",
    "verify.gemini.env_not_found":      "{path} が存在しません",
    "verify.gemini.project_set":        "GOOGLE_CLOUD_PROJECT が設定されています",
    "verify.gemini.project_not_set":    "GOOGLE_CLOUD_PROJECT が設定されていません",
    "verify.gemini.location_set":       "GOOGLE_CLOUD_LOCATION が設定されています",
    "verify.gemini.location_not_set":   "GOOGLE_CLOUD_LOCATION が設定されていません",
    "verify.gemini.adc_exists":         "Application Default Credentials が存在します",
    "verify.gemini.adc_not_found":      "Application Default Credentials が見つかりません。gcloud auth application-default login を実行してください",

    # ── verify: GCloudAuth ───────────────────────────────────
    "verify.gcloud_auth.logged_in":     "gcloud にログイン済み",
    "verify.gcloud_auth.not_logged_in": "gcloud にログインしていません。gcloud auth login を実行してください",
    "verify.gcloud_auth.project_set":   "GCP プロジェクトが設定されています",
    "verify.gcloud_auth.project_not_set": "GCP プロジェクトが設定されていません。gcloud config set project を実行してください",

    # ── verify: GCloudEnableApis ─────────────────────────────
    "verify.apis.none_specified":       "API が指定されていません",
    "verify.apis.enabled":              "{api} が有効です",
    "verify.apis.not_enabled":          "{api} がまだ有効ではありません",
    "verify.apis.query_failed":         "{api}：クエリできません（gcloud にログインしてプロジェクトを設定してください）",

    # ── verify: GcpBillingCredit ─────────────────────────────
    "verify.billing.no_project_id":     "GCP プロジェクト ID を取得できません。まず gcloud config set project を実行してください",
    "verify.billing.project":           "GCP プロジェクト",
    "verify.billing.query_failed":      "Billing 状態をクエリできません（gcloud にログインしていることを確認）",
    "verify.billing.response_error":    "Billing API レスポンス形式エラー",
    "verify.billing.not_enabled":       "プロジェクトの Billing がまだ有効になっていません。Cloud Console で有効にしてください",
    "verify.billing.enabled":           "Billing アカウントがリンクされています",
    "verify.billing.account_active":    "Billing アカウントが有効です",
    "verify.billing.account_inactive":  "Billing アカウントが閉鎖または停止されています",
    "verify.billing.token_failed":      "Access Token を取得できません。gcloud にログインしていることを確認してください",
    "verify.billing.manual_check":      "プロモーションクレジットは Cloud Console での手動確認が必要です",

    # ── verify: PythonVenv ───────────────────────────────────
    "verify.venv.not_found":            "仮想環境 {venv_dir} が存在しません",
    "verify.venv.exists":               "仮想環境 {venv_dir} が存在します",
    "verify.venv.pip_not_found":        "{pip_path} が見つかりません。仮想環境が破損している可能性があります",
    "verify.venv.requirements_not_found": "{requirements} が見つかりません",
    "verify.venv.pip_check_passed":     "パッケージの依存関係が正常です（pip check 通過）",
    "verify.venv.pip_check_failed":     "パッケージの依存関係に問題があります",

    # ── verify: Shell ────────────────────────────────────────
    "verify.shell.no_command":          "shell ステップに verify_command が設定されていません。検証をスキップします",
    "verify.shell.passed":              "検証コマンドが通過しました",
    "verify.shell.failed":              "検証コマンドが失敗しました",
}
