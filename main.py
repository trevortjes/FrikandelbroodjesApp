from math import floor

# Grab user submitted data
def get_user_data():

    money = money_entry.get()  # Store value from money entry
    price = price_entry.get()  # Store value from price entry

    calculate_quantity(money, price)

# Calculation of how many frikandelbroodjes can be bought
def calculate_quantity(money, price):

    try:
        aantal = floor(float(money)/float(price)) # hoeveel broodjes gekocht kunnen worden
        show_result(aantal)

    except:
        # tell the user to input a number
        result.config(text="Das geen getal")

# Show the result to the user
def show_result(quantity):
    if quantity > 1 or quantity == 0:
        result.configure(text=str(quantity) + " frikandelbroodjes!")
    elif quantity < 0:
        result.config(text="Lol poor")
    else:
        result.configure(text=str(quantity) + " frikandelbroodje!")




root.mainloop()