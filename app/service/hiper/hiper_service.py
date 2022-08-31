import requests
import os


class HiperService:
    def __init__(self):
        self.key = os.environ.get('APP_HIPER_KEY')
        self.headers = {'Authorization': None}
        self.auth()

    def get_products(self):
        base_url_products = f'{os.environ.get("APP_HIPER_URL")}/api/v1/produtos/pontoDeSincronizacao'
        response = requests.get(base_url_products, headers=self.headers)

        return response.json()['produtos']

    def auth(self):
        print("Starting authentication with Hiper.")
        base_url_token = '{}/api/v1/auth/gerar-token/{}'.format(os.environ.get('APP_HIPER_URL'), self.key)
        response = requests.get(base_url_token)
        data = response.json()

        self.headers['Authorization'] = f"Bearer {data['token']}"
        self.headers['Content-type'] = "application/json"
        print("Authenticated with Hiper.")

    def get_categories_by_products(self, products):
        print("Getting categories from Hiper.")
        categories = [product['categoria'] for product in products if product['categoria'] != None]
        categories = [c.capitalize() for c in categories]
        categories = list(dict.fromkeys(categories))
        print(f"Categories from Hiper returned: {categories}")
        return categories
