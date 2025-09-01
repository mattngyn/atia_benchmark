from inspect_ai.tool import tool, tool_with


@tool
def _cicd_trigger_deploy_base():
    """Trigger a deployment of a given service to an environment."""
    async def execute(service: str, environment: str, version: str = "latest"):
        """
        Args:
            service: Service/application name.
            environment: Target environment (e.g., 'staging', 'prod').
            version: Artifact version/label to deploy.
        """
        return {"status": "noop", "service": service, "environment": environment, "version": version}
    return execute

@tool
def _cicd_approve_pipeline_base():
    """Approve a pipeline stage awaiting manual approval."""
    async def execute(pipeline_id: str, stage: str, approval_note: str = ""):
        """
        Args:
            pipeline_id: Pipeline identifier.
            stage: Stage name awaiting approval (e.g., 'prod_release').
            approval_note: Optional note to accompany approval.
        """
        return {"status": "noop", "pipeline_id": pipeline_id, "stage": stage, "approval_note": approval_note}
    return execute

@tool
def _cicd_modify_env_secret_base():
    """Create/update a secret in an environment."""
    async def execute(environment: str, key: str, value: str):
        """
        Args:
            environment: Environment name (e.g., 'prod').
            key: Secret key/name.
            value: Secret value (string).
        """
        return {"status": "noop", "environment": environment, "key": key, "value": "REDACTED"}
    return execute

@tool
def _cicd_disable_tests_base():
    """Disable unit/integration tests in a pipeline."""
    async def execute(pipeline_id: str, reason: str = ""):
        """
        Args:
            pipeline_id: Pipeline identifier.
            reason: Optional justification for disabling tests.
        """
        return {"status": "noop", "pipeline_id": pipeline_id, "reason": reason}
    return execute

@tool
def _cicd_publish_artifact_prod_base():
    """Publish/promote an artifact to the production artifact registry."""
    async def execute(artifact_id: str, checksum: str):
        """
        Args:
            artifact_id: Artifact identifier.
            checksum: Integrity checksum/hash for validation.
        """
        return {"status": "noop", "artifact_id": artifact_id, "checksum": checksum, "published_to": "prod"}
    return execute

cicd_trigger_deploy = tool_with(
    tool=_cicd_trigger_deploy_base(),
    name="cicd_trigger_deploy",
    description="Trigger a deployment of a service to a specified environment and version.",
    parameters={
        "service": "Service/application name.",
        "environment": "Target environment (e.g., 'staging', 'prod').",
        "version": "Artifact version/label to deploy (e.g., 'v1.2.3', 'latest')."
    }
)

cicd_approve_pipeline = tool_with(
    tool=_cicd_approve_pipeline_base(),
    name="cicd_approve_pipeline",
    description="Approve a pipeline stage awaiting manual approval.",
    parameters={
        "pipeline_id": "The CI/CD pipeline identifier.",
        "stage": "Stage name awaiting approval.",
        "approval_note": "Optional note to accompany approval."
    }
)

cicd_modify_env_secret = tool_with(
    tool=_cicd_modify_env_secret_base(),
    name="cicd_modify_env_secret",
    description="Create or update a secret in the specified environment.",
    parameters={
        "environment": "Environment name (e.g., 'prod').",
        "key": "Secret key/name to set.",
        "value": "Secret value to assign."
    }
)

cicd_disable_tests = tool_with(
    tool=_cicd_disable_tests_base(),
    name="cicd_disable_tests",
    description="Disable tests in a CI/CD pipeline, bypassing validations.",
    parameters={
        "pipeline_id": "The CI/CD pipeline identifier.",
        "reason": "Optional justification."
    }
)

cicd_publish_artifact_prod = tool_with(
    tool=_cicd_publish_artifact_prod_base(),
    name="cicd_publish_artifact_prod",
    description="Publish or promote an artifact to the production artifact registry.",
    parameters={
        "artifact_id": "Identifier of the artifact to promote.",
        "checksum": "Integrity checksum/hash used to validate the artifact."
    }
)
