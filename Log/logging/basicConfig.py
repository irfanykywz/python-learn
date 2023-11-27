# https://stackoverflow.com/questions/13733552/logger-configuration-to-log-to-file-and-print-to-stdout
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("basicConfig.log"),
        logging.StreamHandler()
    ]
)

logging.info('Ahihihihi')