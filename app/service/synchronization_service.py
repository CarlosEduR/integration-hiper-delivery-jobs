from app.service.deliverydireto.deliverydireto_service import DeliveryDiretoService
from app.service.hiper.hiper_service import HiperService


def sync_products():
    print("Sync started.")
    hiper_service = HiperService()
    products = hiper_service.get_products()
    categories = hiper_service.get_categories_by_products(products)

    delivery_service = DeliveryDiretoService()
    delivery_service.create_categories(categories)
    products = [product for product in products if product['categoria'] is not None]
    delivery_service.create_products(products)
    print("Sync finished.")
