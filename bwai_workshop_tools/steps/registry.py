from .gcloud import GeminiCliVertexAuthStep, GCloudAuthStep, GCloudEnableApisStep, GcpBillingCreditStep
from .python_env import PythonVenvStep
from .shell import ShellStep

REGISTRY = {
    "gemini_cli_vertex_auth": GeminiCliVertexAuthStep,
    "gcloud_auth": GCloudAuthStep,
    "gcloud_enable_apis": GCloudEnableApisStep,
    "gcp_billing_credit": GcpBillingCreditStep,
    "python_venv": PythonVenvStep,
    "shell": ShellStep,
}
