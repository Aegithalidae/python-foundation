million = list(range(1, 10 * (10 ** 5) + 1))
for value in million:
    print(value)

million = [value for value in range(1, 10 * (10 ** 5) + 1)] # List comprehension
for value in million:
    print(value)