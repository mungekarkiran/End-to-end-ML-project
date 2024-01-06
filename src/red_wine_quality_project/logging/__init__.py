import os 
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"

log_filepath = os.path.join(log_dir, "running_log.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level = logging.INFO,
    format = logging_str,
    handlers=[
        logging.FileHandler(log_filepath), # use to print in log file 
        logging.StreamHandler(sys.stdout) # used to print on terminol
    ]
)

logger = logging.getLogger("red_wine_quality_project_logger")