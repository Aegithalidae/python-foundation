# 定义外星人状态，包括坐标和速度
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# 根据外星人速度来调整横坐标。这里只考虑x轴移动。
if alien_0['speed'] == 'slow':
    alien_0['x_position'] += 1
elif alien_0['speed'] == 'medium':
    alien_0['x_position'] += 2
else:
    alien_0['x_position'] += 3

# 输出外星人新的横坐标
print(f"New position: {alien_0['x_position']}")