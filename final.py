import json
import webbrowser
import urllib
import requests

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
    # selection = input()

    return input('Which option would you like to select? ')

def add_more():
    again = input('Would you like to search for the weather of another city? ')
    if again in yes_list:
        print()
        main()
    elif again in no_list:
        print("Thanks for using the Weather program.")
        print('Have a nice day!')
        quit()
    else:
        print('You did not provide a valid option.'
              'Please try again')
        input("Press any key to continue...")
        print()
        print()
        add_more()
def connect:
    website = 'http://https://openweathermap.org/'
    error_number = 0
    try:
        r = requests.get(website)
    except requests.exeptions.ConnectionError:
        print('connection unsuccessful')
        print('retrying up to 5 times')
        error_number += 1
        if error_number <= 5:
            connect()
        elif error_number > 5:
            print('We were unable to make a connection')
            add_more()

def weather_data:
    #connection
    #read the text
    #save text to json

def full_weather:
    # temp = json data specific key for temp

api_key = 'd8aa257457ec1e26187f1410aaa7b258'
api_address = f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q='
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
                full_url = api_address + city
                weather_data()
                full_weather()
                print(temp)
                add_more()

            else:
                print('Sorry, that city and state combination does not exist')
                main()


        elif menu_option == 2:
            zip_code = input('What is the Zip code you would like the weather for? ')
            if zip_code in data['zips']
                if zip_code in data['zips']:
                    full_url = api_address + zip_code
                    weather_data()
                    full_weather()
                    print(temp)
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