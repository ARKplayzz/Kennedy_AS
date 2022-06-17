'''
Password Safe - Revision three
This programme is used to meet the breif of the 2.7 Password safe programme AS91896
by Andrew Kennedy
5/05/2022
'''

# Import Modules - Modules can be used to implement external features like "random" or "json"
import json


# Defining Constants - Constants are variables that stay the same during the entirety of the programme 
USER_LOGIN = ['admin', 1234]

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

    if user == USER_LOGIN[0]:

        pin = get_pin()

        if pin == USER_LOGIN[1]:
            return True

        else:
            print(f'ALERT: That pin is incorrect for the user "{user}"')

    else:
        print(f'ALERT: "{user}" Is not currently a known username')

def menu_opt_1(): # This Function Finds the users inputted WEBSITE and provides the corresponding PASSWORD
    web_lookup = get_string('NOTICE: Enter the website you want to lookup the password for >>> ')

    # Appends the json file containing passwords to the variable: website_list
    with open ('passwords.json','r') as passwords_json: 
        website_list = json.load(passwords_json)
        passwords_json.close()

    issue_check = True

    # for every website in the json file, the programme checks for a matching website
    for counter in range(len(website_list['websites'])):

        requested_website = website_list['websites'][f'website_{counter}']['website']

        # if the programme finds a match it will proceed to the next section of the programme
        if web_lookup.lower() == requested_website.lower():

            requested_pasword = website_list['websites'][f'website_{counter}']['password']

            print(f'NOTICE: The password for the website: {requested_website} is {requested_pasword}')

            issue_check = False
    
    if issue_check != False:

        print('ALERT: Please input a Website That already has a password inputed with it!')

def menu_opt_2(): # This Function Creates a new WEBSITE along with a new PASSWORD using values provided by the User
    web_log = get_string('NOTICE: Please input the name of the website you would like to add a password for >>> ')

    # Appends the json file containing passwords to the variable: website_list
    with open ('passwords.json','r') as passwords_json: 
        website_list = json.load(passwords_json)
        passwords_json.close()

    for counter in range(len(website_list['websites'])):

        requested_website = website_list['websites'][f'website_{counter}']['website']

        if web_log.lower() == requested_website.lower():

            print(f'ALERT: The website: {web_log} is already logged whithin the programme')
            print(f'ALERT: Try selecting option [3] to edit an existing websites password')
        
        else:

            pass_log = get_pass('NOTICE: Please enter your new password, Eg. Reflection27 >>> ')

            #website_list['websites'][f'website_{counter + 1}']['website'] = web_log
            website_list['websites'] = website_list[f'website_{counter + 1}']['website'] = web_log
            website_list['websites'] = website_list[f'website_{counter + 1}']['password'] = pass_log

            print(f'NOTICE: The password {pass_log} has been saved to the website {web_log}')

            with open ('passwords.json', 'w') as file:
                json.dump(website_list, file, indent=4)
                file.close()

def menu_opt_3(): # This Function Edits an existing PASSWORD of the users provided WEBSITE using the value given

    web_log = get_string('NOTICE: Please input the name of the website you would like to edit the password for >>> ')

    # Appends the json file containing passwords to the variable: website_list
    with open ('passwords.json','r') as passwords_json: 
        website_list = json.load(passwords_json)
        passwords_json.close()

    fail_check = True

    for counter in range(len(website_list['websites'])):

        requested_website = website_list['websites'][f'website_{counter}']['website']
        
        if web_log.lower() != requested_website.lower():
            continue

        else:

            pass_log = get_pass(f'NOTICE: Please enter your new password for {web_log}, Eg. Reflection27 >>> ')

            website_list['websites'][f'website_{counter}']['password'] = pass_log

            print(f'NOTICE: The password {pass_log} has been saved to the website {web_log}')

            with open ('passwords.json', 'w') as file:
                json.dump(website_list, file, indent=4)
                file.close()
            
            fail_check = False

    if fail_check != False:
        print(f'ALERT: The website {web_log} does not exist, try selecting option [2] to add a new website & password')

def menu_opt_4(): # This Function removes an existing WEBSIT along with its PASSWORD using the users inputted value

    web_log = get_string('NOTICE: Please input the name of the website you would like to remove from the programme >>> ')

    with open ('passwords.json','r') as passwords_json: 
        website_list = json.load(passwords_json)
        passwords_json.close()

    issue_check = True

    for counter in range(len(website_list['websites'])):

        requested_website = website_list['websites'][f'website_{counter}']['website']
        
        if web_log.lower() != requested_website.lower():
            continue           

        else:

            del(website_list['websites'][f'website_{counter}']) #include in documentation
            print(f'NOTICE: The website: {web_log} has been successfuly removed from the programme')

            with open ('passwords.json', 'w') as file:
                json.dump(website_list, file, indent=4)
                file.close()
            
            issue_check = False

    if issue_check != False:
        print(f'ALERT: The website {web_log} does not exist, try selecting option [2] to add a new website & password')

def menu_opt_6(): 
    print('NOTICE: Here are all the currently stored Websites and Passwords in the Password Safe Programme') 

    with open ('passwords.json','r') as passwords_json:  
        website_list = json.load(passwords_json) 
        passwords_json.close() 
          
    for counter in range(len(website_list['websites'])): 
         
        requested_website = website_list['websites'][f'website_{counter}']['website'] 
        requested_password = website_list['websites'][f'website_{counter}']['password'] 

        print(f'NOTICE: The Website "{requested_website}" has the Password "{requested_password}"') 

# Main Programme -  This is where the base programme will run

print('PROGRAMME: Welcome to the "Password Safe" programme')

roadblock = False
while roadblock != True: # Roadblock refers to the user needing to login before performing an action (fix this later on without a while true)

    roadblock = pass_login()

print('NOTICE: Welcome to the programme, you passed the roadblock')

quit_checker = False
while quit_checker != True:

    print('''
    ----------------MENU---------------
    1. Find the password for an existing website/app
    2. Add a new website/app and new password for it
    3. Change an existing password for an existing website/app
    4. Remove an existing website/app and its password
    5. Exit
    6. Display all know Websites along with their passwords
    ''')
    menu_input = get_integer('>>> ')

    if menu_input == 1:
        menu_opt_1()

    elif menu_input == 2:
        menu_opt_2()

    elif menu_input == 3:
        menu_opt_3()

    elif menu_input == 4:
        menu_opt_4()

    elif menu_input == 5:
        quit_checker = True

    elif menu_input == 6:
        menu_opt_6()

print('NOTICE: Thanks for using the Password Safe programme!')
