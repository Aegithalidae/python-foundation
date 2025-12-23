squares = list()
for value in range(1, 11):
    # square = value ** 2
    # squares.append(square)
    squares.append(value ** 2)  # More concise way
print(squares)

squares = [value **2 for value in range(1, 11)]  # List comprehension
print(squares)

