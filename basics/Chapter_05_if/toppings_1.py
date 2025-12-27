requested_topping = ['pepperoni', 'mushrooms', 'extra cheese']

for topping in requested_topping:
    if topping == 'pepperoni':
        print(f"Sorry, we have ran out of {topping}.")
    else:
        print(f"Adding {topping}.")

print("\nFinished making your pizza!")