name = "ada lovelace"
print(name.title()) #   方法.title()单词首字母大写，具体规则见笔记
print(name.upper()) #   方法.upper()字符串大写
print(name.lower()) #   方法.lower()字符串小写
print(name.capitalize()) #  方法.capitalize()字符串首字母大写

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name #  合并字符串，也叫拼接
print(full_name)
print("Hello, " + full_name.title() + "!") #    拼接适用

message = "Hello, " + full_name.title() + "!" # 拼接结果赋给变量
print(message)