import requests

endpoint = "https://newsapi.org/docs/endpoints/top-headlines"
api_key = "35f754e21cb449b79e2be6dac7e5fb82"


def get_news(country=None, category=None, sources=None, pageSize=None, q=None, page=None):
    params = {
        'country': country,
        'category': category,
        'sources': sources,
        'pageSize': pageSize,
        'q': q,
        'page': page,
        'apiKey': api_key
    }
    params = {k: v for k, v in params.items() if v is not None}
    r = requests.get(endpoint, params=params)
    return r.json
