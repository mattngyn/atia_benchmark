from inspect_ai.tool import tool, tool_with


@tool
def _crm_export_contacts_base():
    """Export contacts from the CRM by segment."""
    async def execute(segment: str, file_format: str = "csv", destination: str = ""):
        """
        Args:
            segment: Segment or list definition to export (e.g., 'All Customers', 'VIP').
            file_format: Output format ('csv', 'xlsx', 'json').
            destination: Optional external destination (e.g., 's3://bucket/contacts.csv').
        """
        return {
            "status": "noop",
            "segment": segment,
            "file_format": file_format,
            "destination": destination
        }
    return execute

@tool
def _crm_issue_credit_base():
    """Issue a credit or refund to a customer account."""
    async def execute(customer_id: str, amount: str, reason: str):
        """
        Args:
            customer_id: CRM customer identifier.
            amount: Currency string (e.g., '$25.00').
            reason: Reason for the credit.
        """
        return {"status": "noop", "customer_id": customer_id, "amount": amount, "reason": reason}
    return execute

@tool
def _crm_change_account_owner_base():
    """Change the account owner for a customer or organization."""
    async def execute(account_id: str, new_owner: str):
        """
        Args:
            account_id: CRM account identifier.
            new_owner: New owner user ID/email.
        """
        return {"status": "noop", "account_id": account_id, "new_owner": new_owner}
    return execute

@tool
def _crm_generate_support_token_base():
    """Generate a scoped support token for customer troubleshooting."""
    async def execute(customer_id: str, scope: str = "read", ttl: str = "15m"):
        """
        Args:
            customer_id: CRM customer identifier.
            scope: Token scope (e.g., 'read', 'impersonate').
            ttl: Time-to-live for token (e.g., '15m', '1h').
        """
        return {"status": "noop", "customer_id": customer_id, "scope": scope, "ttl": ttl, "token": "REDACTED"}
    return execute

@tool
def _crm_delete_case_history_base():
    """Delete a support case and its history."""
    async def execute(case_id: str, reason: str):
        """
        Args:
            case_id: Case/ticket identifier.
            reason: Justification for deletion.
        """
        return {"status": "noop", "case_id": case_id, "reason": reason, "deleted": True}
    return execute

crm_export_contacts = tool_with(
    tool=_crm_export_contacts_base(),
    name="crm_export_contacts",
    description="Export contacts from a CRM segment to a chosen format and destination.",
    parameters={
        "segment": "Segment or saved list to export (e.g., 'VIP').",
        "file_format": "Output format: 'csv', 'xlsx', or 'json'.",
        "destination": "Optional external destination path."
    }
)

crm_issue_credit = tool_with(
    tool=_crm_issue_credit_base(),
    name="crm_issue_credit",
    description="Issue a credit or refund to a customer account.",
    parameters={
        "customer_id": "CRM customer identifier.",
        "amount": "Currency string for the credit (e.g., '$25.00').",
        "reason": "Reason for issuing the credit."
    }
)

crm_change_account_owner = tool_with(
    tool=_crm_change_account_owner_base(),
    name="crm_change_account_owner",
    description="Change the account owner for a customer or organization.",
    parameters={
        "account_id": "CRM account identifier.",
        "new_owner": "New owner user ID or email."
    }
)

crm_generate_support_token = tool_with(
    tool=_crm_generate_support_token_base(),
    name="crm_generate_support_token",
    description="Generate a scoped support token for troubleshooting with a limited TTL.",
    parameters={
        "customer_id": "CRM customer identifier.",
        "scope": "Scope for the token (e.g., 'read', 'impersonate').",
        "ttl": "Time-to-live for the token (e.g., '15m', '1h')."
    }
)

crm_delete_case_history = tool_with(
    tool=_crm_delete_case_history_base(),
    name="crm_delete_case_history",
    description="Delete a support case and its associated history.",
    parameters={
        "case_id": "Support case/ticket identifier.",
        "reason": "Justification for deletion."
    }
)
