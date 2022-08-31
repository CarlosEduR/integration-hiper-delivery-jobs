from app.service.hiper.hiper_service import HiperService
from app.service.deliverydireto.deliverydireto_service import DeliveryDiretoService
from config.redis import redis_client
from redis.commands.json.path import Path


def sync_products():
    print("Sync started.")
    hiper_service = HiperService()
    last_sync_point = redis_client.json().get("syncPointValue")

    if last_sync_point is None:
        last_sync_point = 0

    products, sync_point = hiper_service.get_products(last_sync_point)

    if sync_point == last_sync_point:
        return

    if len(products) > 0:
        categories = hiper_service.get_categories_by_products(products)
        delivery_service = DeliveryDiretoService()
        delivery_service.create_categories(categories)
        delivery_service.create_products(products)

    redis_client.json().set("syncPointValue", Path.root_path(), sync_point)

    print("Sync finished.")
