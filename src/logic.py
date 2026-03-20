from math import floor

# Grab user submitted data
def get_user_data(money, price):
    return money, price

# Calculate how many frikandelbroodjes can be bought
def calculate_quantity(money, price):
    try:
        # Accept both . and , as floating point delimiter
        money = float(str(money).replace(",", "."))
        price = float(str(price).replace(",", "."))
        quantity = floor(money / price)
        return quantity

    except Exception:
        return "wrong input"


# Show the result to the user
def format_result(quantity):
    if quantity == "wrong input":
        return "Das geen getal"
    elif quantity < 0:
        return "Lol poor"
    elif quantity > 1 or quantity == 0:
        return f"{quantity} frikandelbroodjes!"
    else:
        return f"{quantity} frikandelbroodje!"
