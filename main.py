import os
import time

os.system('clear')

Names = []

Numbers = []

while True:
    print("""
    (1) Add New Contact
    (2) Display Contacts
    (3) Search for Contacts
    (4) Exit
    """)

    choice = int(input('Choice: '))

    if choice == 1:
        name = str(input('Name: '))
        number = (input('Number: '))
        Names.append(name)
        Numbers.append(number)
        Name = ', '.join(Names)
        Number = ','.join(Numbers)
        time.sleep(1)
        os.system('clear')
        print('Contact Added!')
        time.sleep(1)
        os.system('clear')

    if choice == 2:
        os.system('clear')
        Together = Name,Number
        print('CONTACTS')
        print('\n')
        print(Together)


    if choice == 3:
        print('SEARCH FOR CONTACTS')
        print('\n')

        search = input('Name: ')
        os.system('clear')
        
        if search == name:
            print(f'Contact Found: {name} {number}')
        else:
            print('Contact not Found')
            




    if choice == 4:
        os.system('clear')
        break
