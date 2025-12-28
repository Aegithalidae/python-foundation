number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in number_list:
    print(f"\nNumber:{number} is available in the list.")
    if number == 1:
        print("This is 1st")
    elif number == 2:
        print("This is 2nd")
    elif number == 3:
        print("This is 3rd")
    else:
        print(f"This is {number}th")