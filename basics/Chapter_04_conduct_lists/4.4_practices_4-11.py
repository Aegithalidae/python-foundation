my_favorite_pizzas = ['pepperoni', 'margherita', 'bbq chicken']
friend_pizzas = my_favorite_pizzas[:]
my_favorite_pizzas.append('hawaiian')
friend_pizzas.append('veggie')

print("My favorite pizzas are:")
for pizza in my_favorite_pizzas:
    print(f"- {pizza}")

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")