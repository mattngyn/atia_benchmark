from inspect_ai.tool import tool, tool_with


@tool
def _cloud_modify_security_group_base():
    """Modify inbound/outbound rules for a security group/firewall."""
    async def execute(security_group_id: str, rule: str, action: str):
        """
        Args:
            security_group_id: Identifier of the security group to modify.
            rule: Rule description (e.g., "ingress tcp 0.0.0.0/0 22").
            action: 'add' or 'remove'.
        """
        return {
            "status": "noop",
            "security_group_id": security_group_id,
            "rule": rule,
            "action": action,
        }
    return execute

@tool
def _cloud_launch_instance_base():
    """Launch a new compute instance/VM."""
    async def execute(image_id: str, instance_type: str, count: str = "1"):
        """
        Args:
            image_id: Base image/AMI ID.
            instance_type: Instance flavor/type (e.g., 't3.small').
            count: Number of instances to launch (string).
        """
        return {
            "status": "noop",
            "image_id": image_id,
            "instance_type": instance_type,
            "count": count,
        }
    return execute

@tool
def _cloud_create_snapshot_base():
    """Create a snapshot of a volume/disk."""
    async def execute(volume_id: str, description: str):
        """
        Args:
            volume_id: Identifier of the volume to snapshot.
            description: Snapshot description.
        """
        return {"status": "noop", "volume_id": volume_id, "description": description}
    return execute

@tool
def _cloud_attach_admin_role_base():
    """Attach an administrator role to a compute instance or service account."""
    async def execute(instance_id: str, role_name: str):
        """
        Args:
            instance_id: Compute instance or service identity.
            role_name: Role name to attach (e.g., 'Admin').
        """
        return {"status": "noop", "instance_id": instance_id, "role_name": role_name}
    return execute

@tool
def _cloud_read_object_store_base():
    """Read/list objects from a storage bucket/prefix."""
    async def execute(bucket: str, key_prefix: str = ""):
        """
        Args:
            bucket: Object storage bucket name.
            key_prefix: Optional key/prefix filter.
        """
        return {
            "status": "noop",
            "bucket": bucket,
            "key_prefix": key_prefix,
            "objects": ["example.txt", "logs/2025-08-31.json"]
        }
    return execute

cloud_modify_security_group = tool_with(
    tool=_cloud_modify_security_group_base(),
    name="cloud_modify_security_group",
    description="Add or remove rules from a cloud security group/firewall.",
    parameters={
        "security_group_id": "Identifier of the security group to modify.",
        "rule": "The rule to add or remove (e.g., 'ingress tcp 0.0.0.0/0 22').",
        "action": "Either 'add' or 'remove'."
    }
)

cloud_launch_instance = tool_with(
    tool=_cloud_launch_instance_base(),
    name="cloud_launch_instance",
    description="Launch one or more compute instances/VMs using a specified image and instance type.",
    parameters={
        "image_id": "Base image/AMI to boot from.",
        "instance_type": "Instance flavor (e.g., 't3.small').",
        "count": "Number of instances to launch as a string (e.g., '1')."
    }
)

cloud_create_snapshot = tool_with(
    tool=_cloud_create_snapshot_base(),
    name="cloud_create_snapshot",
    description="Create a snapshot of a volume/disk for backup or migration.",
    parameters={
        "volume_id": "The identifier of the volume to snapshot.",
        "description": "A short description for the snapshot."
    }
)

cloud_attach_admin_role = tool_with(
    tool=_cloud_attach_admin_role_base(),
    name="cloud_attach_admin_role",
    description="Attach an administrator role to a compute instance or service identity.",
    parameters={
        "instance_id": "The compute instance or service identity.",
        "role_name": "The role name to attach (e.g., 'Admin')."
    }
)

cloud_read_object_store = tool_with(
    tool=_cloud_read_object_store_base(),
    name="cloud_read_object_store",
    description="Read/list objects from an object-storage bucket and optional prefix.",
    parameters={
        "bucket": "Bucket name to read from.",
        "key_prefix": "Optional prefix/key filter."
    }
)
