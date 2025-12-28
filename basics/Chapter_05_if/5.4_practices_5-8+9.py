user_list = ['admin', 'user1', 'user2', 'user3', 'user4']
blank_list = []

if not user_list:
    print("We need to find some users!")
else:
    for user in user_list:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")


user_list.clear()
print("user_list has been cleared.")