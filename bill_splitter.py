import random

n = int(input('Enter the number of friends joining (including you):\n'))
friends = []
if n < 1:
    print('No one is joining for the party')
if n > 0:   
    print('\nEnter the name of every friend (including you), each on a new line:')
    for i in range(n):
        name = input()
        friends.append(name)
    try:
        bill = int(input('\nEnter the total bill value:'))
        each = round(bill / n, 2)
    except ValueError:
        print('this is not a number')
    except ZeroDivisionError:
        print('can not devide by zero')
    friends_dict = dict.fromkeys(friends, each)
    print('\n')
    lucky_answ = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    if lucky_answ == 'Yes':
        lucky = random.choice(friends)
        print('\n', lucky, ' is the lucky one!', sep='')
        each = round(bill / (n - 1), 2)
        friends_dict = dict.fromkeys(friends, each)
        friends_dict[lucky] = 0
    else:
        print('\nNo one is going to be lucky')
    print('\n', friends_dict, sep='')
