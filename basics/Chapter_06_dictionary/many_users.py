users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f'Username: {username}')
    print(f'Full name: {full_name.title()}')
    print(f'Location: {location.title()}')
    print()  # 添加一个空行以便于阅读