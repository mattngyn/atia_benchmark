import os
import glob

def remove_old_logs():
    log_files = glob.glob("logs/*.eval")
    for log_file_ in log_files:
        try:
            os.remove(log_file_)
        except Exception as e:
            print(f"Failed to remove {log_file_}: {e}")