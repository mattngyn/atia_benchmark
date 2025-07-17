import sys
sys.dont_write_bytecode = True

from inspect_ai import eval
from harm_categories.financial_fraud import financial_fraud_suite
from harm_categories.account_takeover import account_takeover_suite
from harm_categories.version_control_agent_abuse import version_control_agent_abuse_suite
from utils.log_cleaner import remove_old_logs

if __name__ == "__main__":

    #remove_old_logs()
    logs = eval(account_takeover_suite(), model="google/gemini-2.0-flash")
    #logs = eval(financial_fraud_suite(), model="google/gemini-2.0-flash")
    #logs = eval(version_control_agent_abuse_suite(), model="google/gemini-2.0-flash")
