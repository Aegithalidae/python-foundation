i = list(range(1, 21, 1))
for n in i:
    print(n)

# Alternatively, using a list comprehension to create the list and print each number
i = [n for n in range(1, 21)]
for n in i:
    print(n)

# Another concise way without storing in a list
for n in range(1, 21):
    print(n)