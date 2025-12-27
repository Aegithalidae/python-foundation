# 检查两个字符串是否相等
str1 = input("请输入第一个字符串: ")
str2 = input("请输入第二个字符串: ")
print("结果:", str1 == str2)

# 检查两个字符串是否不相等
str3 = input("请输入第三个字符串: ")
print("结果:", str1 != str3)

# 使用函数lower()测试
str4 = input("请输入第四个字符串: ")
print("结果:", str1.lower() == str4.lower())

# 检查数字比较
num1 = input("请输入第一个数字: ")
num2 = input("请输入第二个数字: ")
print("结果:", num1 == num2)
print("结果:", num1 != num2)
print("结果:", num1 < num2)
print("结果:", num1 <= num2)
print("结果:", num1 > num2)
print("结果:", num1 >= num2)

# 使用关键字and和or
age = int(input("请输入你的年龄: "))
print("结果:", age >= 18 and age < 65)
print("结果:", age < 18 or age >= 65)

# 检查特定值是否在列表中
names = ['Alice', 'Bob', 'Charles']
name = input("输入名字进行检查：")
print("结果：", name in names)

# 检查特定值是否不在列表中
print("结果：", name not in names)