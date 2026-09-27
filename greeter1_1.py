def greet_user():
    """显示简单的问候语"""
    print("Hello")

greet_user()

#向函数传递信息
def greet_user(username):
    """显示简单问候的问候语"""
    print(f"Heloo, {username.title()}!")

greet_user('jesse')