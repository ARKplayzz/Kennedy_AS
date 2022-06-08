'''
Password Safe - Revision one
This programme is used to meet the breif of the 2.7 Password safe programme AS91896
by Andrew Kennedy
5/05/2022
'''

# Import Modules - Modules can be used to implement external features like "random" or "json"


# Defining Constants - Constants are variables that stay the same during the entirety of the programme 
USER_LOGIN = [['admin', 1234],['ARKennedy', 3605]]
WEBSITE_LIST = [['website', 'Password123'],['ssh','Reflection27']]

PASS_MAX_LENGTH = 16
PASS_MIN_LENGTH = 4
PASS_MIN_NUMBERS = 1
PIN_LENGTH = 4

# Defining Functions - Functions and programmes that may be called anywhere in the main programme

def get_string(question): # This Function takes a question from the programme and gains a STRING from the user providing it back to the programme
    string = str(input(question))

    return string

def get_integer(question): # This Function takes a question from the programme and gains a INTEGER from the user providing it back to the programme
    try:
        integer = int(input(question))
        return integer
    except:
        print('ALERT: Please make sure to input a valid integer')

def get_pin(): # This Function gains an INTEGER from the user providing it back to the programme only if it meets the requirements of a PIN
    try:
        pin = int(input('NOTICE: Please enter your pin, Eg. 1234 >>> '))
        while len(str(pin)) != PIN_LENGTH:
            pin = int(input('ALERT: Please make sure to enter a 4 digit pin >>> '))

        return pin
    except ValueError:
        print('ALERT: Please make sure to input a 4 digit pin')
        
def get_pass(question): # This Function gains an STRING from the user providing it back to the programme only if it meets the requirements of a PASSWORD
    try:
        password = str(input(question))
        while len((password)) > PASS_MAX_LENGTH or len(str(password)) < PASS_MIN_LENGTH or password.isalpha() == True:
            password = str(input(f'ALERT: Please ensure to input a password between {PASS_MIN_LENGTH} & {PASS_MAX_LENGTH} charecters & contain at least {PASS_MIN_NUMBERS} numbers >>> '))

        return password
    except ValueError:
        print(f'ALERT: Please make sure to input a password at least {PASS_MIN_LENGTH} and contain at least {PASS_MIN_NUMBERS} numbers')
    
def pass_login(): # This Function runs a login proccedure for the user and returns back TRUE weather or not the user has successfuly logged in

    user = get_string('NOTICE: Please input your username >>> ')

    for i in range(len(USER_LOGIN)):

        if user == USER_LOGIN[i][0]:

            pin = get_pin()

            if pin == USER_LOGIN[i][1]:
                return True

            else:
                print(f'ALERT: That pin is incorrect for the user "{user}"')
                break

        else:
            print(f'ALERT: "{user}" Is not currently a known username')
            break


# Main Programme -  This is where the base programme will run

print('PROGRAMME: Welcome to the "Password Safe" programme')

roadblock = False
while roadblock != True: # Roadblock refers to the user needing to login before performing an action (fix this later on without a while true)

    roadblock = pass_login()

print('NOTICE: Welcome to the programme, you passed the roadblock')

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
    web_lookup = get_string('NOTICE: Enter the website you want to lookup the password for >>> ')

    for website in range(len(WEBSITE_LIST)):
        if web_lookup.lower() == WEBSITE_LIST[website][0].lower():
            print(f'NOTICE: The password for the website: {WEBSITE_LIST[website][0]} is { WEBSITE_LIST[website][1]}')

    print('ALERT: Please input a Website That already has a password inputed with it!')

elif menu_input == 2:
    web_log = get_string('NOTICE: Please input the name of the website you would like to add a password for >>> ')

    for website in range(len(WEBSITE_LIST)):
        if web_log.lower() == WEBSITE_LIST[website][0].lower():
            print(f'ALERT: The website: {WEBSITE_LIST[website][0]} is already logged whithin the programme')
            print(f'ALERT: Try selecting option [3] to edit an existing websites password')

    pass_log = get_pass('NOTICE: Please enter your new password, Eg. Reflection27 >>> ')

    WEBSITE_LIST.append([web_log, pass_log])

    print(f'NOTICE: The password {pass_log} has been saved to the website {web_log}')

elif menu_input == 3:
    web_log = get_string('NOTICE: Please input the name of the website you would like to edit the password for >>> ')

    for website in range(len(WEBSITE_LIST)):
        
        if web_log.lower() != WEBSITE_LIST[website][0].lower():
            print(f'ALERT: The website {web_log} does not exist, try selecting option [2] to add a new website & password')

    pass_log = get_pass(f'NOTICE: Please enter your new password for {web_log}, Eg. Reflection27 >>> ')
    WEBSITE_LIST[website][1] = pass_log
    print(WEBSITE_LIST[website][1])
    print(WEBSITE_LIST)

    print(f'NOTICE: The password {pass_log} has been saved to the website {web_log}')

elif menu_input == 4:
    web_log = get_string('NOTICE: Please input the name of the website you would like to remove from the programme >>> ')

    for website in range(len(WEBSITE_LIST)):
        
        if web_log.lower() != WEBSITE_LIST[website][0].lower():
            print(f'ALERT: The website {web_log} does not exist, try selecting option [2] to add a new website & password')

    
    del(WEBSITE_LIST[website])
    print(WEBSITE_LIST)

    print(f'NOTICE: The website: {web_log} has been successfult removed from the programme')

elif menu_input == 5:
    print('NOTICE: Goodbye!')
