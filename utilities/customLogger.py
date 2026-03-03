"""import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\Logs\\automation.log",
                        format='%(asctime)s: %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger"""

import logging
import os


class LogGen:

    @staticmethod
    def loggen():
        os.makedirs("Logs", exist_ok=True)

        log_file = os.path.abspath("Logs/automation.log")

        logger = logging.getLogger("TestLogger")
        logger.setLevel(logging.INFO)

        # prevent duplicate handlers
        if logger.hasHandlers():
            logger.handlers.clear()

        file_handler = logging.FileHandler(log_file, mode="w")
        file_handler.setFormatter(
            logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')
        )

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(
            logging.Formatter('%(levelname)s : %(message)s')
        )

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        return logger





