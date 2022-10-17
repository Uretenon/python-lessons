import math
print('Task 1\n ')
while True:
    try:
        day = int(input('type in the day of the week: '))
        assert 1 <= day <= 7
    except ValueError:
        print('It has to be a valid number.')
    except AssertionError:
        print('Please enter a valid day of the week.')
    else:
        break
if day == 6 or day == 7:
    print("weekend")
else:
    print('not a weekend')

print("\nTask 2\n")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            print (not(x or y or z) == (not(x) and not(y) and not(z)), end = " ")

print("\nTask 3\n")
while True:
    try:
        x, y = map(int, input('enter coordinates x and y with spaces in between: ').split())
        assert x, y != 0
    except AssertionError:
        print('Coordinates cannot be zero.')
    else:
        break

if x and y > 0:
    print("1st quarter")
elif x < 0 and y > 0:
    print("2nd quarter")
elif x < 0 and y < 0:
    print("3rd quarter")
else:
    print("4th quarter")

print("\nTask 4\n")
while True:
    try:
        quarter = int(input("enter the quarter number: "))
        assert 1 <= quarter <= 4
    except AssertionError:
        print('Quarter is 1 through 4')
    else:
        break
if quarter == 1:
    print("x > 0 and y > 0")
elif quarter == 2:
    print("x < 0 and y > 0")
elif quarter == 3:
    print("x < 0 and y < 0")
else:
    print("x > 0 and y < 0")

print('\nTask 5\n')

x1, y1 = map(int, input('enter coordinates x and y of the first dot with spaces in between: ').split())
x2, y2 = map(int, input('enter coordinates x and y of the second dot with spaces in between: ').split())
distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print("distance is %.3f" % distance)