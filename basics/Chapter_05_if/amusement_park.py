age = int(input("Please enter your age:"))

if age < 4:
    print("Your admission cost is free.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

# 注意到这里我们重复使用了 print() 函数来显示不同的消息。
# 每一次检查的条件都是年龄
# 所以考虑对年龄进行操作
if age <4:
    cost = 'free'
elif age <18:
    cost = '$5'
else:
    cost = '$10'
print(f"Your admission cost is {cost}.")