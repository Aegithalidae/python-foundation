cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse = True)
print(cars)
cars.sort(key = len) # 可以输入函数，按函数结果排序
print(cars)

print("\n")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)
print("\n")
print(len(cars))