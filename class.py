a = int(input('Enter a number: '))

if 10 < a < 20:
    b = int(input('Enter another number: '))

c = (a * b)

print('The sum of these two numbers is: ' + float(c))

if c > 100:
    print('That is a large sum!')
