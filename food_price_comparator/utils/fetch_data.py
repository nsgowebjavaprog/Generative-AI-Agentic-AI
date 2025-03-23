import requests
from config import ZOMATO_API_KEY, SWIGGY_API_KEY

def get_zomato_price(food_name, restaurant_name, city):
    url = f"https://api.zomato.com/v2/search?q={food_name}&restaurant={restaurant_name}&city={city}"
    headers = {"user-key": ZOMATO_API_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get("price", None)
    return None

def get_swiggy_price(food_name, restaurant_name, city):
    url = f"https://api.swiggy.com/v1/search?q={food_name}&restaurant={restaurant_name}&city={city}"
    headers = {"Authorization": f"Bearer {SWIGGY_API_KEY}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get("price", None)
    return None