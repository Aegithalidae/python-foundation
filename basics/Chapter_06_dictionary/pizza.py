# 储存所点披萨配料信息
pizza_toppings = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# 概述所点披萨
print(f"You ordered a {pizza_toppings['crust']}-crust pizza "
      "with the following toppings:")
for topping in pizza_toppings['toppings']:
    print(f"- {topping}")