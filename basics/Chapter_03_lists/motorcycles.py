motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)  # 改变了第一个元素

motorcycles.append('ducati')
print(motorcycles)  # 在列表末尾添加了一个新元素

del motorcycles[0]
print(motorcycles)