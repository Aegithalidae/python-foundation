my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  # Make a copy of the list
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
    print(f"- {food}")

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(f"- {food}")

print([food for food in my_foods]) # Print my_foods list
print([food for food in friend_foods]) # Print friend_foods list