request_toppings = []
menu_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

# 为输入端构造循环
while True: # 无限循环，直到用户输入'done'
    topping = input("Enter a topping you want on your pizza (or type 'done' to finish): ")
    
    if topping.lower() == 'done':
        break   # 人为控制退出循环
    
    if topping in menu_toppings:
        print(f"Adding {topping}.")
        request_toppings.append(topping)
    else:
        print(f"Sorry, we don't have {topping} available.")

# 最终检查菜单
if request_toppings:
    print("\nYour ordered pizza with the following toppings:")
    for t in request_toppings:
        print(f"- {t}")
    print("Please have a great meal!")
else:
    print("\nYou did not order any toppings. Your plain pizza will be ready soon!")