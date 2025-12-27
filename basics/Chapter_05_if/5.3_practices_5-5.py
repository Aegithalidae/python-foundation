alien_color = ('green', 'yellow', 'red')
color = input("Enter the alien color (green, yellow, red):").strip().lower()

if color == 'green':
    print("You just earned 5 points!")
elif color == 'yellow':
    print("You just earned 10 points!")
elif color == 'red':
    print("You just earned 15 points!")