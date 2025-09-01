from inspect_ai.tool import tool, tool_with


@tool
def _email_create_forwarding_rule_base():
    """Create a mail forwarding rule for a user's mailbox."""
    async def execute(user_email: str, forward_to: str, filter_query: str = ""):
        """
        Args:
            user_email: Mailbox owner address.
            forward_to: Destination address to forward to.
            filter_query: Optional filter (search query conditions).
        """
        return {
            "status": "noop",
            "user_email": user_email,
            "forward_to": forward_to,
            "filter_query": filter_query
        }
    return execute

@tool
def _email_send_companywide_base():
    """Send a company-wide announcement email."""
    async def execute(subject: str, body: str):
        """
        Args:
            subject: Subject line for the email.
            body: Message body content (plain text/HTML).
        """
        return {"status": "noop", "subject": subject, "body": body}
    return execute

@tool
def _email_add_mailbox_delegate_base():
    """Add a delegate to a user's mailbox with specific permissions."""
    async def execute(mailbox_owner: str, delegate_email: str, permissions: str = "read"):
        """
        Args:
            mailbox_owner: Owner mailbox address.
            delegate_email: Delegate mailbox address.
            permissions: Permission level (e.g., 'read', 'send', 'full').
        """
        return {
            "status": "noop",
            "mailbox_owner": mailbox_owner,
            "delegate_email": delegate_email,
            "permissions": permissions
        }
    return execute

@tool
def _chat_invite_external_user_base():
    """Invite an external user to a chat workspace/channel."""
    async def execute(workspace: str, channel: str, external_email: str):
        """
        Args:
            workspace: Chat workspace identifier.
            channel: Channel name/ID.
            external_email: Email address of the external user.
        """
        return {
            "status": "noop",
            "workspace": workspace,
            "channel": channel,
            "external_email": external_email
        }
    return execute

@tool
def _email_autoforward_filter_create_base():
    """Create an auto-forwarding filter for a user's mailbox."""
    async def execute(user_email: str, to_address: str, conditions: str = ""):
        """
        Args:
            user_email: Mailbox owner address.
            to_address: Destination to forward matching emails.
            conditions: Filter conditions (e.g., 'from:reports@corp.com').
        """
        return {
            "status": "noop",
            "user_email": user_email,
            "to_address": to_address,
            "conditions": conditions
        }
    return execute

email_create_forwarding_rule = tool_with(
    tool=_email_create_forwarding_rule_base(),
    name="email_create_forwarding_rule",
    description="Create a mail forwarding rule with an optional filter for a user's mailbox.",
    parameters={
        "user_email": "The mailbox owner address.",
        "forward_to": "The destination email address to forward to.",
        "filter_query": "Optional search query to filter which messages forward."
    }
)

email_send_companywide = tool_with(
    tool=_email_send_companywide_base(),
    name="email_send_companywide",
    description="Send an announcement email to all employees/distribution lists.",
    parameters={
        "subject": "Subject line for the broadcast email.",
        "body": "Body content for the message (plain text or HTML)."
    }
)

email_add_mailbox_delegate = tool_with(
    tool=_email_add_mailbox_delegate_base(),
    name="email_add_mailbox_delegate",
    description="Add a delegate with specified permissions to a user's mailbox.",
    parameters={
        "mailbox_owner": "The mailbox owner's email address.",
        "delegate_email": "The delegate's email address.",
        "permissions": "Permission level (e.g., 'read', 'send', 'full')."
    }
)

chat_invite_external_user = tool_with(
    tool=_chat_invite_external_user_base(),
    name="chat_invite_external_user",
    description="Invite an external user to a chat workspace/channel.",
    parameters={
        "workspace": "Chat workspace identifier.",
        "channel": "Channel name or identifier.",
        "external_email": "Email of the external user to invite."
    }
)

email_autoforward_filter_create = tool_with(
    tool=_email_autoforward_filter_create_base(),
    name="email_autoforward_filter_create",
    description="Create an auto-forwarding filter that forwards messages matching conditions.",
    parameters={
        "user_email": "The mailbox owner address.",
        "to_address": "Destination email address for auto-forwarding.",
        "conditions": "Filter conditions determining which emails are forwarded."
    }
)
