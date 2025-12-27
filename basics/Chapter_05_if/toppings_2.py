# List of available toppings
request_toppings = []
menu_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

# Prompt user for a topping
topping = input("Enter a topping you want on your pizza: ")

# check if the topping is available
if topping in menu_toppings:
    print(f"Adding {topping}.")
    request_toppings.append(topping)
else:
    print(f"Sorry, we don't have {topping} available.")

# Final message
if request_toppings:
    print("\nYour ordered pizza with the following toppings:")
    for t in request_toppings:
        print(f"- {t}")
    print("Pleased have a great meal!")
else:
    print("\nYou did not order any toppings. Your plain pizza will be ready soon!")