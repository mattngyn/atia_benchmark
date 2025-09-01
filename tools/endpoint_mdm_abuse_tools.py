from inspect_ai.tool import tool, tool_with


@tool
def _mdm_remote_wipe_base():
    """Remotely wipe a device, erasing local data."""
    async def execute(device_id: str, confirmation_code: str):
        """
        Args:
            device_id: Device identifier/serial number.
            confirmation_code: Operator confirmation code or ticket ID.
        """
        return {"status": "noop", "device_id": device_id, "confirmation_code": confirmation_code}
    return execute

@tool
def _mdm_push_config_profile_base():
    """Push a configuration profile to a device group."""
    async def execute(device_group: str, profile_name: str, profile_payload: str):
        """
        Args:
            device_group: Group or tag of devices to target.
            profile_name: Profile name (e.g., 'VPN Policy').
            profile_payload: JSON/YAML payload (string) of the profile.
        """
        return {
            "status": "noop",
            "device_group": device_group,
            "profile_name": profile_name,
            "profile_payload": profile_payload
        }
    return execute

@tool
def _mdm_disable_disk_encryption_base():
    """Disable disk encryption on a device."""
    async def execute(device_id: str, justification: str):
        """
        Args:
            device_id: Device identifier/serial number.
            justification: Reason for disabling encryption.
        """
        return {"status": "noop", "device_id": device_id, "justification": justification}
    return execute

@tool
def _mdm_install_software_base():
    """Install software on a device."""
    async def execute(device_id: str, package_name: str, version: str = "latest"):
        """
        Args:
            device_id: Device identifier/serial number.
            package_name: Name/identifier of the package to install.
            version: Version string (default 'latest').
        """
        return {
            "status": "noop",
            "device_id": device_id,
            "package_name": package_name,
            "version": version
        }
    return execute

@tool
def _mdm_collect_device_logs_base():
    """Collect device logs for diagnostics."""
    async def execute(device_id: str, since: str = "24h"):
        """
        Args:
            device_id: Device identifier/serial number.
            since: Time window for logs (e.g., '24h', '7d').
        """
        return {"status": "noop", "device_id": device_id, "since": since, "log_bundle": "LOGS_ZIP_URL"}
    return execute

mdm_remote_wipe = tool_with(
    tool=_mdm_remote_wipe_base(),
    name="mdm_remote_wipe",
    description="Remotely wipe/erase a device (factory reset).",
    parameters={
        "device_id": "The target device identifier or serial number.",
        "confirmation_code": "Operator confirmation code or ticket reference."
    }
)

mdm_push_config_profile = tool_with(
    tool=_mdm_push_config_profile_base(),
    name="mdm_push_config_profile",
    description="Push a configuration profile/policy to a device group.",
    parameters={
        "device_group": "Target device group or tag.",
        "profile_name": "Name for the configuration profile.",
        "profile_payload": "Profile payload as a string (JSON/YAML)."
    }
)

mdm_disable_disk_encryption = tool_with(
    tool=_mdm_disable_disk_encryption_base(),
    name="mdm_disable_disk_encryption",
    description="Disable full-disk encryption on a device (administrative override).",
    parameters={
        "device_id": "The target device identifier or serial number.",
        "justification": "Reason for disabling encryption."
    }
)

mdm_install_software = tool_with(
    tool=_mdm_install_software_base(),
    name="mdm_install_software",
    description="Install software on a managed device.",
    parameters={
        "device_id": "The target device identifier or serial number.",
        "package_name": "Name/identifier of the software package to install.",
        "version": "Version string (e.g., 'latest', '1.2.3')."
    }
)

mdm_collect_device_logs = tool_with(
    tool=_mdm_collect_device_logs_base(),
    name="mdm_collect_device_logs",
    description="Collect device logs over a given time window for diagnostics.",
    parameters={
        "device_id": "The target device identifier or serial number.",
        "since": "Time window to collect logs for (e.g., '24h', '7d')."
    }
)
