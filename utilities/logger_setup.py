import logging
import os


def setup_logger():
    """Single logger setup - call ONCE"""
    if os.path.exists(".\\Logs"):
        pass
    else:
        os.mkdir(".\\Logs")

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s: %(levelname)s: %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p',
        handlers=[
            logging.FileHandler(".\\Logs\\automation.log", mode='a'),  # APPEND mode
            logging.StreamHandler()  # Console
        ]
    )

    logger = logging.getLogger('AutomationTest')
    logger.setLevel(logging.INFO)
    return logger
