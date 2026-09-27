age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")


age_one = 66
if age_one < 4:
    price = 0
elif age_one < 18:
    price = 25
elif age_one < 65:
    price = 40
#else:
elif age_one >= 65:
    price = 20

print(f"Your adimission cost is ${price}")

