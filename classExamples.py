print("Hello World")


def printW():
    print('Hello World')


x = 2


def switch_statement():
    match x:
        case 1:
            print('Equals 1')
        case 2:
            print('Equals 2')

    if x == 1:
        print('Equals 1')
    else:
        print('Not 1')


for i in range(0, 10):
    print(i)

skibidis = ['Bruh', 'Moment']

print("Guess a year:")
year = input()
try:
    int_year = int(year)
    print(int_year)
except:
    print("Invalid")

print('end of python file')

dictionary = {}
dictionary['Matt'] = 'Awesome goober'

print(dictionary)

list = []
list.append('Matt')
list.append('Matt')
list.append('Matt')
list.append('Matt')
list.append('Matt')
list.append('Matt')

print(list)
