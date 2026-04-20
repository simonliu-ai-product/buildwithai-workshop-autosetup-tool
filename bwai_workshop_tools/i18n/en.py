STRINGS: dict[str, str] = {
    # ── App ──────────────────────────────────────────────────
    "app.title":                        "Build with AI Workshop Setup",

    # ── Runner ───────────────────────────────────────────────
    "runner.file_not_found":            "Step config file not found: ",
    "runner.unknown_type":              "Unknown step type: ",
    "runner.available_types":           "Available types: ",
    "runner.confirm_step":              "Execute this step?",
    "runner.step_skipped":              "Skipped",
    "runner.step_completed":            "Step completed",
    "runner.step_failed":               "Step failed, stopping execution",
    "runner.all_done":                  "🎉  All steps completed!",
    "runner.dry_run_skip":              "(dry-run) Skipping",
    "runner.dry_run_done":              "(dry-run) {total} steps listed",

    # ── CLI verify ───────────────────────────────────────────
    "cli.verify.file_not_found":        "Step config file not found: ",
    "cli.verify.manual_header":         "⚠  The following items require manual verification",
    "cli.verify.all_passed":            "✔  All automated checks passed",
    "cli.verify.failed":                "✘  Some steps failed. Please fix the issues and re-verify.",

    # ── UI ───────────────────────────────────────────────────
    "ui.input_title":                   "Input",
    "ui.input_default_hint":            "Press Enter to use default",
    "ui.command_title":                 "Running command",

    # ── Language commands ────────────────────────────────────
    "lang.list_title":                  "Supported Languages",
    "lang.col_code":                    "Code",
    "lang.col_name":                    "Name",
    "lang.col_current":                 "Current",
    "lang.current_marker":              "← Current",
    "lang.set_success":                 "Language set to {lang} ({name})",
    "lang.invalid":                     "Unsupported language: {lang}",
    "lang.supported":                   "Supported: {supported}",
    "lang.current":                     "Current language: {lang} ({name})",

    # ── Step descriptions ────────────────────────────────────
    "step.gemini_cli_vertex_auth.desc": "Configure Gemini CLI with Vertex AI authentication (ADC)",
    "step.gcloud_auth.desc":            "Google Cloud login and project setup",
    "step.gcloud_enable_apis.desc":     "Enable specified Google Cloud APIs",
    "step.gcp_billing_credit.desc":     "Check if GCP project has Workshop promotional credit",
    "step.python_venv.desc":            "Create Python virtual environment and install dependencies",
    "step.shell.desc":                  "Execute custom shell command",
    "step.base.no_verify":              "This step type does not support verification",

    # ── run: GeminiCliVertexAuth ─────────────────────────────
    "run.gemini.ask_project":           "Enter GOOGLE_CLOUD_PROJECT (GCP project ID)",
    "run.gemini.ask_location":          "Enter GOOGLE_CLOUD_LOCATION",
    "run.gemini.project_empty":         "Project ID cannot be empty",
    "run.gemini.conflict_keys":         "Conflicting environment variables detected: {keys}",
    "run.gemini.conflict_detail":       "These variables must be unset when using Vertex AI ADC, otherwise authentication may fail",
    "run.gemini.conflict_confirm":      "Continue anyway?",
    "run.gemini.cancelled":             "Cancelled",
    "run.gemini.written":               "Written to {path}:",

    # ── run: GCloudAuth ──────────────────────────────────────
    "run.gcloud_auth.ask_project":      "Enter GCP project ID",
    "run.gcloud_auth.project_empty":    "Project ID cannot be empty",
    "run.gcloud_auth.set_project":      "Setting project: {project}",

    # ── run: GCloudEnableApis ────────────────────────────────
    "run.apis.none":                    "No APIs specified, skipping",

    # ── run: GcpBillingCredit ────────────────────────────────
    "run.billing.manual_info":          "This step requires manually redeeming a Workshop promotional code.",
    "run.billing.manual_link_label":    "Please redeem the promo code at:",

    # ── run: PythonVenv ──────────────────────────────────────
    "run.venv.already_exists":          "Virtual environment {venv_dir} already exists, skipping",
    "run.venv.create_failed":           "Failed to create virtual environment",
    "run.venv.created":                 "Virtual environment created: {venv_dir}",
    "run.venv.requirements_not_found":  "{requirements} not found",
    "run.venv.install_complete":        "Dependencies installed successfully",

    # ── run: Shell ───────────────────────────────────────────
    "run.shell.no_command":             "No command parameter specified",
    "run.shell.complete":               "Command executed successfully",
    "run.shell.failed":                 "Command failed (exit code {code})",

    # ── verify: GeminiCliVertexAuth ──────────────────────────
    "verify.gemini.env_exists":         "{path} exists",
    "verify.gemini.env_not_found":      "{path} does not exist",
    "verify.gemini.project_set":        "GOOGLE_CLOUD_PROJECT is set",
    "verify.gemini.project_not_set":    "GOOGLE_CLOUD_PROJECT is not set",
    "verify.gemini.location_set":       "GOOGLE_CLOUD_LOCATION is set",
    "verify.gemini.location_not_set":   "GOOGLE_CLOUD_LOCATION is not set",
    "verify.gemini.adc_exists":         "Application Default Credentials exist",
    "verify.gemini.adc_not_found":      "Application Default Credentials not found, run: gcloud auth application-default login",

    # ── verify: GCloudAuth ───────────────────────────────────
    "verify.gcloud_auth.logged_in":     "Logged into gcloud",
    "verify.gcloud_auth.not_logged_in": "Not logged into gcloud, run: gcloud auth login",
    "verify.gcloud_auth.project_set":   "GCP project is set",
    "verify.gcloud_auth.project_not_set": "GCP project not set, run: gcloud config set project <PROJECT_ID>",

    # ── verify: GCloudEnableApis ─────────────────────────────
    "verify.apis.none_specified":       "No APIs specified",
    "verify.apis.enabled":              "{api} is enabled",
    "verify.apis.not_enabled":          "{api} is not enabled",
    "verify.apis.query_failed":         "{api}: Unable to query (ensure gcloud is logged in and project is set)",

    # ── verify: GcpBillingCredit ─────────────────────────────
    "verify.billing.no_project_id":     "Cannot get GCP project ID, run gcloud config set project first",
    "verify.billing.project":           "GCP Project",
    "verify.billing.query_failed":      "Unable to query billing status (ensure gcloud is logged in)",
    "verify.billing.response_error":    "Billing API response format error",
    "verify.billing.not_enabled":       "Billing not enabled for project, enable in Cloud Console",
    "verify.billing.enabled":           "Billing account linked",
    "verify.billing.account_active":    "Billing account is active",
    "verify.billing.account_inactive":  "Billing account is closed or suspended",
    "verify.billing.token_failed":      "Unable to get Access Token, ensure gcloud is logged in",
    "verify.billing.manual_check":      "Promotional credits require manual verification in Cloud Console",

    # ── verify: PythonVenv ───────────────────────────────────
    "verify.venv.not_found":            "Virtual environment {venv_dir} does not exist",
    "verify.venv.exists":               "Virtual environment {venv_dir} exists",
    "verify.venv.pip_not_found":        "{pip_path} not found, virtual environment may be corrupted",
    "verify.venv.requirements_not_found": "{requirements} not found",
    "verify.venv.pip_check_passed":     "Package dependencies OK (pip check passed)",
    "verify.venv.pip_check_failed":     "Package dependency issues found",

    # ── verify: Shell ────────────────────────────────────────
    "verify.shell.no_command":          "No verify_command set for shell step, skipping verification",
    "verify.shell.passed":              "Verification command passed",
    "verify.shell.failed":              "Verification command failed",
}
