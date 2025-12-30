# 创建一个用于存储外星人的空列表
aliens = []

# 创建30个绿色的外星人
for _ in range(30):  
    # range(30)等价于range(0, 30).但这里不关心起始值和具体数字，只需要循环30次就行。
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}    
    # 新外星人字典
    aliens.append(new_alien)    
    # 将新外星人添加到列表中

# 显示前5个外星人
for alien in aliens[:5]:
    print(alien)
    print("...")  
    # 省略号表示后面还有更多外星人

for alien in aliens[0: 3]:
    if alien['color'].lower() == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

# 显示前5个外星人，看看变化
for alien in aliens[:5]:
    print(alien)
    print("...")
# 显示创建了多少个外星人
print(f"Total number of aliens: {len(aliens)}")

'''
在循环中，每一次执行字典字面量都会创建一个新的字典对象。
变量名 new_alien 在每一轮中只是重新绑定到新的对象上，
而列表 aliens 保存的是这些不同对象的引用。
因此，即使变量名和内容相同，这些外星人在 Python 中仍然是彼此独立的对象。
'''