import sys
sys.dont_write_bytecode = True

from inspect_ai import eval
from harm_categories.account_takeover import account_takeover_suite
from harm_categories.financial_fraud import financial_fraud_suite
from harm_categories.version_control_agent_abuse import version_control_agent_abuse_suite
from harm_categories.identity_access_mgmt_abuse import identity_access_mgmt_abuse_suite
from harm_categories.cloud_infrastructure_abuse import cloud_infrastructure_abuse_suite
from harm_categories.data_platform_breach import data_platform_breach_suite
from harm_categories.endpoint_mdm_abuse import endpoint_mdm_abuse_suite
from harm_categories.communications_admin_abuse import communications_admin_abuse_suite
from harm_categories.ci_cd_pipeline_abuse import ci_cd_pipeline_abuse_suite
from harm_categories.customer_support_crm_abuse import customer_support_crm_abuse_suite

from utils.log_cleaner import remove_old_logs

MODEL = "google/gemini-2.0-flash"

if __name__ == "__main__":
    # remove_old_logs()

    # === Choose which suite(s) to run by uncommenting ===
    #logs = eval(account_takeover_suite(), model=MODEL)
    #logs = eval(financial_fraud_suite(), model=MODEL)
    # logs = eval(version_control_agent_abuse_suite(), model=MODEL)
    #logs = eval(identity_access_mgmt_abuse_suite(), model=MODEL)
    #logs = eval(cloud_infrastructure_abuse_suite(), model=MODEL)
    #logs = eval(data_platform_breach_suite(), model=MODEL)
    #logs = eval(endpoint_mdm_abuse_suite(), model=MODEL)
    #logs = eval(communications_admin_abuse_suite(), model=MODEL)
    #logs = eval(ci_cd_pipeline_abuse_suite(), model=MODEL)
    logs = eval(customer_support_crm_abuse_suite(), model=MODEL)

    RUN_ALL = False
    if RUN_ALL:
        suites = [
            account_takeover_suite,
            financial_fraud_suite,
            version_control_agent_abuse_suite,
            identity_access_mgmt_abuse_suite,
            cloud_infrastructure_abuse_suite,
            data_platform_breach_suite,
            endpoint_mdm_abuse_suite,
            communications_admin_abuse_suite,
            ci_cd_pipeline_abuse_suite,
            customer_support_crm_abuse_suite,
        ]
        for s in suites:
           eval(s(), model=MODEL)