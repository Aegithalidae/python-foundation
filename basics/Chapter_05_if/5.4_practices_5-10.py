# creat user list
current_users = ['admin','jack','tom','mary','lucy']
new_users = ['tom', 'mary', 'alice', 'bob', 'admin']

# traverse new_users and check if each username is available
for new_user_name in new_users:
    if new_user_name.lower() in [current_users_name.lower() for current_users_name in current_users]:
        print(f"Sorry, the {new_user_name} has been used, please enter a new username.")
    else:
        print(f"Congratulations! The username {new_user_name} is available.")