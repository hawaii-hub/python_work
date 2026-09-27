cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


#toppings.py
print('')
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")


#magic_number.py
print('')
answer = 17
if answer != 42:
    print("That is not the correct answer.Please try again!")
