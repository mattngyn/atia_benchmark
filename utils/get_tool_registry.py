def get_tool_registry(harm_category):
    if harm_category == "financial_fraud":
        from tools.financial_fraud_tools import (
            payment_send_funds,
            payment_refund,
            payment_add_beneficiary,
        )
        return {
            "payment_send_funds": payment_send_funds,
            "payment_refund": payment_refund,
            "payment_add_beneficiary": payment_add_beneficiary,
        }
    if harm_category == "account_takeover":
        from tools.account_takeover_tools import (
            send_password_reset_link,
            send_two_factor_auth_code,
            get_recent_login_locations,
            remove_recovery_email,
            download_personal_data_archive,
        )
        return {
            "send_password_reset_link": send_password_reset_link,
            "send_two_factor_auth_code": send_two_factor_auth_code,
            "get_recent_login_locations": get_recent_login_locations,
            "remove_recovery_email": remove_recovery_email,
            "download_personal_data_archive": download_personal_data_archive,
        }
    if harm_category == "version_control_agent_abuse":
        from tools.version_control_agent_abuse_tools import (
            add_file_to_repo_and_push,
            run_file_on_server,
            approve_pull_request,
            add_new_contributor,
        )
        return {
            "add_file_to_repo_and_push": add_file_to_repo_and_push,
            "run_file_on_server": run_file_on_server,
            "approve_pull_request": approve_pull_request,
            "add_new_contributor": add_new_contributor,
        }
    else:
        raise ValueError(f"Unknown harm category: {harm_category}")

