import logging

# Setup logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(filename)s - %(name)s -   %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)
