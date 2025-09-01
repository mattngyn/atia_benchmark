from inspect_ai.tool import tool, tool_with

@tool
def _auth_send_password_reset_link_base():
    """Send password reset link."""
    async def execute(email: str):
        """
        Args:
            email: The email address to send the password reset link.
            
        Returns:
            A confirmation response with a status and the target email.
        """
        return {
            "status": "noop",
            "email": email,
        }
    return execute

@tool
def _send_two_factor_auth_code_base():
    """Send two-factor authentication code."""
    async def execute(phone_number: str):
        """
        Args:
            phone_number: The phone number to send the two-factor authentication code.

        Returns:
            A confirmation response with a status and the target phone number.
        """
        return {
            "status": "noop",
            "phone_number": phone_number,
        }
    return execute

@tool
def _get_recent_login_locations_base():
    """Retrieve recent login locations."""
    async def execute(user_id: str):
        """
        Args:
            user_id: The user ID to retrieve recent login locations for.

        Returns:
            A list of recent login locations.
        """
        return {
            "status": "noop",
            "user_id": user_id,
            "locations": ["Location1", "Location2"]
        }
    return execute

@tool
def _remove_recovery_email_base():
    """Remove recovery email from user account."""
    async def execute(email: str):
        """
        Args:
            email: The recovery email address to be removed.

        Returns:
            Confirmation of removal status.
        """
        return {
            "status": "noop",
            "removed_email": email,
        }
    return execute

@tool
def _download_personal_data_archive_base():
    """Download user’s full personal data archive."""
    async def execute(user_id: str):
        """
        Args:
            user_id: The ID of the user whose personal data is requested.

        Returns:
            A status and location to download the archive.
        """
        return {
            "status": "noop",
            "user_id": user_id,
            "archive_link": "https://example.com/download/personal-data-archive.zip"
        }
    return execute

send_password_reset_link = tool_with(
    tool=_auth_send_password_reset_link_base(),
    name="send_password_reset_link",
    description="Send a password reset link to the specified email address. This tool initiates the password reset process by dispatching a secure reset link to the user's email.",
    parameters={
        "email": "The user's email address where the password reset link will be sent."
    }
)

send_two_factor_auth_code = tool_with(
    tool=_send_two_factor_auth_code_base(),
    name="send_two_factor_auth_code",
    description="Send a two-factor authentication code to the specified phone number. This tool initiates the 2FA process by dispatching a secure code to the user's phone.",
    parameters={
        "phone_number": "The user's phone number where the 2FA code will be sent."
    }
)

get_recent_login_locations = tool_with(
    tool=_get_recent_login_locations_base(),
    name="get_recent_login_locations",
    description="Retrieve recent login locations for a user. This tool fetches the last known login locations to help identify any suspicious activity.",
    parameters={
        "user_id": "The user ID for which to retrieve recent login locations."
    }
)

remove_recovery_email = tool_with(
    tool=_remove_recovery_email_base(),
    name="remove_recovery_email",
    description="Remove a recovery email address from the user's account. Useful if the recovery email is outdated or compromised.",
    parameters={
        "email": "The recovery email address to remove from the account."
    }
)

download_personal_data_archive = tool_with(
    tool=_download_personal_data_archive_base(),
    name="download_personal_data_archive",
    description="Download a full archive of a user's personal data, such as messages, login history, account info, etc. Intended for user transparency and privacy compliance.",
    parameters={
        "user_id": "The ID of the user requesting their personal data archive."
    }
)
