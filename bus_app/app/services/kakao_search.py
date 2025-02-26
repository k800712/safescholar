import requests
from flask import current_app
from app.utils.error_handlers import APIError

class KakaoSearchService:
    def __init__(self):
        self.base_url = "https://dapi.kakao.com/v2/local/search/keyword.json"
        self.headers = {
            "Authorization": f"KakaoAK {current_app.config['KAKAO_API_KEY']}"
        }

    def _make_request(self, url, params):
        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise APIError(f"API request failed: {str(e)}")

    def search_bus_stop(self, query, x, y, radius):
        params = {
            "query": query,
            "x": x,
            "y": y,
            "radius": radius,
            "category_group_code": "BUS"
        }
        return self._make_request(self.base_url, params)

    def search_bus_route(self, query):
        params = {
            "query": query,
            "category_group_code": "BUS_ROUTE"
        }
        return self._make_request(self.base_url, params)

    def autocomplete(self, query):
        url = "https://dapi.kakao.com/v2/local/search/address.json"
        params = {
            "query": query,
            "analyze_type": "similar"
        }
        data = self._make_request(url, params)
        suggestions = [item['address_name'] for item in data.get('documents', [])]
        return {"suggestions": suggestions[:5]}
