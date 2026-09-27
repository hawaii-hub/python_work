# 测试多个条件运行

requested_toppings = [
    'mushrooms',
    'green peppers',
    'extra cheese'
    ]
#if 'mushrooms' in requested_toppings:
    #print('Adding mushrooms.')
#if 'pepperoni' in requested_toppings:
    #print('Adding pepperroni.')
#if 'extra cheese' in requested_toppings:
    #print('Adding extra cheese.')

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, wo are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
    
print("\nFinished making your pizza!")

# 确定列表非空
print('\n5.4.2 Determine if a list is not empty')

requested_toppings = []

if requested_toppings:
    for ruquestede_topping in requested_toppings:
        print(f'Adding {requested_topping}.')
    print('\nFinished making your pizza!')
else:
    print('Are you sure you want a plain pizza?')

# 使用多个列表
print('\n5.4.3Working with multiple lists')

available_toppings = ['mushroom', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushroom', 'french fires', 'extra cheese']                

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'Adding {requested_topping}')
    else:
        print(f"Sorry, we don't have {requested_topping}")

print('\nFinished making your pizza!')