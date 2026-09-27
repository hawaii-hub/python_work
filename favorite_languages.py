
# 6.2.6由类似的对象组成的字典
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# 6.3.1 遍历所有的键值对

print('\n6.3.1 遍历所有的键值对')
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favoriye languages is {language.title()}.")

#homework 6.6 调查
print("\nHomework 6.6")
humans = ['jen', 'sarah', 'edward', 'phil', 'alice', 'bob', 'jack']

for human in humans:
    if human in favorite_languages:
        print(f"Thank you for taking the poll,{human}")
    else:
        print(f"I hope you can the poll,{human}")

# 6.3.2 遍历字典中的所有键
print('所有键')

for name in favorite_languages.keys(): # = for name in favorite_languages:
    print(name.title())

# 指定朋友的名字,进行特殊操作
print(' \n指定朋友的名字,进行特殊操作')

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

# 检查某个人是否接受了调查
print('\n检查某个人是否接受了调查')

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# 6.3.3 按特定的顺序遍历字典中的所有键
print('\n按特定的顺序遍历字典中的所有键')

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# 6.3.4 遍历字典中的所有值
print('\n 6.3.4 遍历字典中的所有值')

print('The following languages have been mentioned:')
for language in favorite_languages.values():
#for language in set(favorite_languages.values()):    #剔除重复项
    print(language.title())

# 6.4.2 在字典中储存列表
print('')

favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell']
}

for name,languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")