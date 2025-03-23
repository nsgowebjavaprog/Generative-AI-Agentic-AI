from utils.fetch_data import get_zomato_price, get_swiggy_price

def compare_prices(food_name, restaurant_name, city):
    zomato_price = get_zomato_price(food_name, restaurant_name, city)
    swiggy_price = get_swiggy_price(food_name, restaurant_name, city)

    if zomato_price is None and swiggy_price is None:
        return "Price not found for both platforms."

    if zomato_price is None:
        return f"Swiggy offers the best price: ₹{swiggy_price}"

    if swiggy_price is None:
        return f"Zomato offers the best price: ₹{zomato_price}"

    if zomato_price < swiggy_price:
        return f"Zomato is cheaper at ₹{zomato_price}"
    else:
        return f"Swiggy is cheaper at ₹{swiggy_price}"