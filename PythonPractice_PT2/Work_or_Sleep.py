# Ask the user the day of the week
# If it's a weeekend let them know they can go back to sleepy time
# I can still use straight if's so might as well . . . . .

day = int(input('What day of the week is it? '))

if day == 1:
    print("It's Monday time to get that bread!")
if day == 2:
    print("It's Tuesday time to get that bread!")
if day == 3:
    print("It's Wednesday time to get that bread!")
if day == 4:
    print("It's Thursday time to get that bread!")
if day == 5:
    print("It's Friday last day to get that bread!")
if day == 6:
    print("It's Saturday cool go back to sleep")
if day == 0:
    print("It's Sunday cool go back to sleep")