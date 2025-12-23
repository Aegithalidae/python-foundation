simple_foods = ('bread', 'butter', 'jam', 'pancakes', 'waffles', 'eggs', 'bacon')
for food in simple_foods:
    print(food)
print(id(simple_foods))

simple_foods += ('sausage', 'fruit')  # This creates a new tuple; original remains unchanged
print("\nUpdated buffet menu:")
for food in simple_foods:   
    print(food)
print(id(simple_foods))
# simple_foods[0] = 'bagel'  # This will raise a TypeError because tuples are immutable