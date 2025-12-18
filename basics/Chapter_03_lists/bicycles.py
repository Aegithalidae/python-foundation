bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])  # 索引从0开始而非1
print(bicycles[2])
print(bicycles[3])
print(bicycles[-1])  # 访问最后一个元素
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)