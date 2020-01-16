# User inputs a number and from the numbrer inputed gets the day of the week 
# EX: 0 For Sunday, 1 for Monday .. etc 
# Why use else if I can use straight If's? 
day = int(input('What day of the week is it? '))

if day == 0:
    print("Today is Sunday")
if day == 1:
    print("Today is Monday")
if day == 2:
    print("Today is Tuesday")
if day == 3:
    print("Today is Wednesday")
if day == 4:
    print("Today is Thursday")
if day == 5:
    print("Today is Friday")
if day == 6:
    print("Today is Saturday")