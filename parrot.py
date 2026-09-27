# input()函数的工作原理
#message = input("Tell me something, and I will repeat it back to you:")
#print(message)


# 7.2.2 让用户选择何时退出

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

#message = " "
#while message != 'quit':
    #message = input(prompt)
    
    #if message != 'quit': #在显示消息前将做简单的检查，仅在消息不是退出值时才打印它
        #print(message)

# 添加标志
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)