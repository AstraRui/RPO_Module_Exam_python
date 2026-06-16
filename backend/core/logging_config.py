import logging
import os
LOG_DIR = "./logs" #Изменили путь (ранее использовалась защищенная системой папка)
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.WARNING, # Изменили на WARNING, чтобы логгер пропускал ВСЕ уровни логов
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler(f"{LOG_DIR}/app.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("nexus")