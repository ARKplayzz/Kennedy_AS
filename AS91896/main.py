'''
Password Safe - Revision one
This programme is used to meet the breif of the 2.7 Password safe programme AS91896
by Andrew Kennedy
5/05/2022
'''

# Import Modules - Modules can be used to implement external features like "random" or "json"


# Defining Constants - Constants are variables that stay the same during the entirety of the programme 
USER_LOGIN = [['admin', 1234],['ARKennedy', 3605]]
WEBSITE_LIST = [['website', 'Password123']]


# Defining Functions - Functions and programmes that may be called anywhere in the main programme

def get_string(question):
    string = str(input(question))

    return string

def get_integer(question):
    try:
        integer = int(input(question))
        return integer
    except:
        print('Please make sure to input a valid integer')

def get_pin():
    try:
        pin = int(input('Please enter your pin, Eg. 1234 >>> '))
        while len(str(pin)) != 4:
            pin = int(input('Please make sure to enter a 4 digit pin >>> '))

        return pin
    except ValueError:
        print('Please make sure to input a 4 digit pin')

    
def pass_login():

    user = get_string('Please input your username >>> ')

    for i in range(len(USER_LOGIN)):

        if user == USER_LOGIN[i][0]:

            print(f'ur username is {USER_LOGIN[i][0]}')
            pin = get_pin()

            if pin == USER_LOGIN[i][1]:
                print(f'ur pin is {USER_LOGIN[i][1]}')
                return True

            else:
                print(f'That pin is incorrect for the user "{user}"')
                break

        else:
            print(f'"{user}" Is not currently a known username')
            break


    



            


# Main Programme -  This is where the base programme will run

print('Welcome to the "Password Safe" programme')

roadblock = False
while roadblock != True: # Roadblock refers to the user needing to login before performing an action (fix this later on without a while true)
    
    print(len(USER_LOGIN))
    roadblock = pass_login()

print('welcome to the programme, you passed the roadblock')

print('''
----------------MENU---------------
1. Find the password for an existing website/app
2. Add a new website/app and new password for it
3. Change an existing password for an existing website/app
4. Remove an existing website/app and its password
5. Exit
6.
''')
menu_input = get_integer('>>> ')

if menu_input == 1:
    web_lookup = get_string('')
    for website in range():
        if web_lookup.lower() == WEBSITE_LIST[website][0]:
            print('POGGOR')

elif menu_input == 2:
    print('1')

elif menu_input == 3:
    print('1')

elif menu_input == 4:
    print('1')

elif menu_input == 5:
    print('1')
