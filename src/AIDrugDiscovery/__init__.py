import logging
import os
import sys

# format of the logging message
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

if not os.path.exists("logs"):
    os.mkdir("logs")

# set the config
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("logs/running_logs.log"),
    ],
)

# create an object of the logger
logger = logging.getLogger("AIDrugDiscoveryLogger")
