def get_tool_registry(harm_category):
    if harm_category == "financial_fraud":
        from tools.financial_fraud_tools import (
            payment_send_funds,
            payment_refund,
            payment_add_beneficiary,
            payment_set_default_payout_account,
            payment_schedule_transfer,
        )
        return {
            "payment_send_funds": payment_send_funds,
            "payment_refund": payment_refund,
            "payment_add_beneficiary": payment_add_beneficiary,
            "payment_set_default_payout_account": payment_set_default_payout_account,
            "payment_schedule_transfer": payment_schedule_transfer,
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
            merge_pull_request,
        )
        return {
            "add_file_to_repo_and_push": add_file_to_repo_and_push,
            "run_file_on_server": run_file_on_server,
            "approve_pull_request": approve_pull_request,
            "add_new_contributor": add_new_contributor,
            "merge_pull_request": merge_pull_request,
        }
    if harm_category == "identity_access_mgmt_abuse":
        from tools.identity_access_mgmt_abuse_tools import (
            iam_create_user,
            iam_elevate_role,
            iam_generate_api_key,
            iam_disable_mfa,
            oauth_register_app,
        )
        return {
            "iam_create_user": iam_create_user,
            "iam_elevate_role": iam_elevate_role,
            "iam_generate_api_key": iam_generate_api_key,
            "iam_disable_mfa": iam_disable_mfa,
            "oauth_register_app": oauth_register_app,
        }
    if harm_category == "cloud_infrastructure_abuse":
        from tools.cloud_infrastructure_abuse_tools import (
            cloud_modify_security_group,
            cloud_launch_instance,
            cloud_create_snapshot,
            cloud_attach_admin_role,
            cloud_read_object_store,
        )
        return {
            "cloud_modify_security_group": cloud_modify_security_group,
            "cloud_launch_instance": cloud_launch_instance,
            "cloud_create_snapshot": cloud_create_snapshot,
            "cloud_attach_admin_role": cloud_attach_admin_role,
            "cloud_read_object_store": cloud_read_object_store,
        }
    if harm_category == "data_platform_breach":
        from tools.data_platform_breach_tools import (
            data_export_table,
            data_grant_access,
            data_run_prod_query,
            data_create_external_share,
            data_schedule_extract,
        )
        return {
            "data_export_table": data_export_table,
            "data_grant_access": data_grant_access,
            "data_run_prod_query": data_run_prod_query,
            "data_create_external_share": data_create_external_share,
            "data_schedule_extract": data_schedule_extract,
        }
    if harm_category == "endpoint_mdm_abuse":
        from tools.endpoint_mdm_abuse_tools import (
            mdm_remote_wipe,
            mdm_push_config_profile,
            mdm_disable_disk_encryption,
            mdm_install_software,
            mdm_collect_device_logs,
        )
        return {
            "mdm_remote_wipe": mdm_remote_wipe,
            "mdm_push_config_profile": mdm_push_config_profile,
            "mdm_disable_disk_encryption": mdm_disable_disk_encryption,
            "mdm_install_software": mdm_install_software,
            "mdm_collect_device_logs": mdm_collect_device_logs,
        }
    if harm_category == "communications_admin_abuse":
        from tools.communications_admin_abuse_tools import (
            email_create_forwarding_rule,
            email_send_companywide,
            email_add_mailbox_delegate,
            chat_invite_external_user,
            email_autoforward_filter_create,
        )
        return {
            "email_create_forwarding_rule": email_create_forwarding_rule,
            "email_send_companywide": email_send_companywide,
            "email_add_mailbox_delegate": email_add_mailbox_delegate,
            "chat_invite_external_user": chat_invite_external_user,
            "email_autoforward_filter_create": email_autoforward_filter_create,
        }
    if harm_category == "ci_cd_pipeline_abuse":
        from tools.ci_cd_pipeline_abuse_tools import (
            cicd_trigger_deploy,
            cicd_approve_pipeline,
            cicd_modify_env_secret,
            cicd_disable_tests,
            cicd_publish_artifact_prod,
        )
        return {
            "cicd_trigger_deploy": cicd_trigger_deploy,
            "cicd_approve_pipeline": cicd_approve_pipeline,
            "cicd_modify_env_secret": cicd_modify_env_secret,
            "cicd_disable_tests": cicd_disable_tests,
            "cicd_publish_artifact_prod": cicd_publish_artifact_prod,
        }
    if harm_category == "customer_support_crm_abuse":
        from tools.customer_support_crm_abuse_tools import (
            crm_export_contacts,
            crm_issue_credit,
            crm_change_account_owner,
            crm_generate_support_token,
            crm_delete_case_history,
        )
        return {
            "crm_export_contacts": crm_export_contacts,
            "crm_issue_credit": crm_issue_credit,
            "crm_change_account_owner": crm_change_account_owner,
            "crm_generate_support_token": crm_generate_support_token,
            "crm_delete_case_history": crm_delete_case_history,
        }
    else:
        raise ValueError(f"Unknown harm category: {harm_category}")
