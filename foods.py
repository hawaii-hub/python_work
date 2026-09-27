my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

my_foods.append('cannoli')
friends_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friends_foods)

#这个行不通
print('')
her_foods = ['scallion', 'beef noodles', 'eggplant bibimbap']

liu_foods = her_foods

her_foods.append('watermelon platter')
liu_foods.append('signature-style eggplant')

print("Her favorite foods are:")
print(her_foods)

print("\nMy friend's favorite foods are:")
print(liu_foods)

#4.10 使用多个循环
print("My favorite food list is:")
for my_food in my_foods:
    print(my_food)

print("My friend's favotite food list is:")
for friend_food in friends_foods:
    print(friend_food)