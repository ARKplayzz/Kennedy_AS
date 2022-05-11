''' 
The purpose of this program is to...
by Andrew Kennedy
5/05/2022 
'''
# Importing modules
import math
import json

# Defining Constants
FINE_COST = [30, 80, 120, 170, 230, 300, 400, 510, 630]


WARRENTS = ['james wilson', 'helga norman', 'zachary conroy']
# Defining Functions

def get_string(question):
    string = str(input(question))
    return string

def get_integer(question):
    try:
        integer = int(input(question))
        return integer
    except:
        print

def fine_calculation(speed):

    if speed > 45:
        fine = FINE_COST[8]
    else:
        fine = FINE_COST[(math.ceil((speed + 1) / 5)-2)]

    return fine

#def enter_offences():
def check_offences(speeders_name):

    if speeders_name in WARRENTS:
        warrent_check = True
        print(f'{speeders_name.upper()} WANTED FOR ARREST')

    else:
        warrent_check = False


    return warrent_check


#def display_summary():


def main():
    user_input = get_integer('''Welcome to the "Speedy Cars" Programme
    please input below what you would like to do!
    1 - Enter Offences
    2 - Display Summary
    3 - Exit
    : ''')

    if user_input == 1:

        speeder_name = get_string('Enter name of speeder: ')

        check_offences(speeder_name.lower())

        speeder_speed = get_integer('Enter the amount over speed limit: ')
        speeder_fine = fine_calculation(speeder_speed)
        print(f"{speeder_name.title()} to be charged ${speeder_fine}")

    elif user_input == 2:
        print('based')
    elif user_input == 3:
        print('based')



# Base Programme

main()
