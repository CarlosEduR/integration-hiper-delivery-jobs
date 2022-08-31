import time
import schedule
from dotenv import load_dotenv

from app import synchronization_service

load_dotenv()

schedule.every().minute.do(synchronization_service.sync_products)
while True:
    schedule.run_pending()
    time.sleep(1)
