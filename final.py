import json
import webbrowser
import urllib
import requests

#API key d8aa257457ec1e26187f1410aaa7b258
api_key = 'd8aa257457ec1e26187f1410aaa7b258'
print('welcome to the program')
print('we are here to help you with all your weather related needs')

def help:
    if a.lower in help_list:
        print('To search by city and state please enter 1')
        print('to search by Zipcode please enter 2')
        main()

def menu():
    print("[1] To search by City and State")
    print("[2] To Search by Zipcode")
    print("For HELP please type help")
    print("To QUIT please type  Quit")

    return input('Which option would you like to select? ')

def add_more():
    again = input('Would you like to add another vehicle to your garage? ')
    if again in yes_list:
        print()
        main()
    elif again in no_list:
        print("Thanks for using the virtual garage builder.")
        print('Your garage consists of:')
        print(garage)
        print('Have a nice day!')
        quit()
    else:
        print('You did not provide a valid option.'
              'Please try again')
        input("Press any key to continue...")
        print()
        print()
        add_more()

def connect

quit_list = ['quit', 'q', 'end', 'no', 'n']
yes_list = ['yes', 'yeah', 'y', 'ok', 'k']
no_list = quit_list
help_list = ['help', 'h']
with open(USCIties.json) as f:
    data = json.load(f)
def main():
    while (True):
        menu_option = menu()

        if menu_option == 1:
            city = input('Which city would you like the weather for? ')
            state = input(f'Which state is {city} in (Please use the proper 2 letter abbreviation)? ')
            if city and state in data['zips']:
                #use api to get weather
                #print weather
                add_more()

            else:
                print('Sorry, that city and state combination does not exist')
                main()


        elif menu_option == 2:
            zip_code = input('What is the Zip code you would like the weather for? ')
            if zip_code in data['zips']
                # use api to get weather
                # print weather
                add_more()
            else:
                print('Sorry, that city and state combination does not exist')
                main()



        elif menu_option.lower in help_list:
            help()

        elif menu_option.lower() in quit_list:
            print("Thanks for using the weather program.")
            print('Have a great day!')

            break
        else:
            print("Invalid option, please try again")

        input("Press any key to continue...")
        main()