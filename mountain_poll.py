responses = {}
# 设置一个标志， 指出调查是否继续
polling_active = True

while polling_active:
    # 提示输入被调查者的名字和回答
    name = input("\nWhat is you name? ")
    response = input("While mountain would ypu like to climb somebody? ")

    # 将回答储存在字典中
    responses[name] = response

    # 看看有人是否还需要调查
    repeat = input("Would you like to let anther person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

#调查结束， 显示结果
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")