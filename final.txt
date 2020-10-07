# Author: Eric Rottman
# Creation Date: October 6, 2020
# Below is a simple program which pulls weather data from openweathermap.org
# for additional API info feel free to look at https://openweathermap.org/current#format

# import required libraries
import json
import webbrowser
import urllib
import requests

print('welcome to the program')
print('we are here to help you with all your weather related needs')


# add more function used to allow user to loop
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


# use of try catch block to verify valid connection
def connect():
    r = requests.get('http://openweathermap.org')
    print()
    print("connecting....")
    print()
    for i in range(5):
        try:
            r.raise_for_status()
        except requests.exceptions.ConnectionError:
            print('we could not make a valid connection. Please try again')
            print('trying again up to 5 times')
        except requests.exceptions.HTTPError:
            print('no connection')
            print('trying again up to 5 times')
        except requests.exceptions.Timeout:
            print('no connection')
            print('trying again up to 5 times')


# define help info if user asks for help
def help_if_asked():
    print('Welcome to the program.')
    print('We pull weather data from openweathermap.org')
    print('Please type the corresponding number from our menu to decide how you would like to search for the weather.')
    print()
    main()


# define menu for user to choose from
def choose_option():
    print('To search by City and State please type [1]')
    print('To search by Zip code please type [2].')
    print('For help please type [3]')
    print('To QUIT please type [4]')

    return input('Please choose an option from the menu: ')


# set basic variables that will be needed for the program
api_key = 'd8aa257457ec1e26187f1410aaa7b258'
api_address = f'api.openweathermap.org/data/2.5/weather?appid={api_key}&q='
quit_list = ['quit', 'q', 'end', 'no', 'n', '4']
yes_list = ['yes', 'yeah', 'y', 'ok', 'k']
no_list = quit_list
help_list = ['help', 'h', '3']
zip_list = ['zip', 'zipcode', 'zip code', '2']
city_list = ['city', 'state', 'city state', 'city and state', '1']
accepted_entry = ['quit', 'q', 'end', 'no', 'n', '4', 'yes', 'yeah', 'y', 'ok', 'k', 'help', 'h', '3', 'zip', 'zipcode',
                  'zip code', '2', 'city', 'state', 'city state', 'city and state', '1']


# define main variable for easy looping
def main():
    chosen_option = choose_option()
    # check that chosen_option is a valid choice to continue
    if chosen_option in accepted_entry:
        print('Great Choice!')
        print()
        # if user wants to search for weather based on city and state
        if chosen_option in city_list:
            print('What is the name of the city you would like the weather for?')
            city = input()
            print(f'What state is {city} in? (Please use the full state name)')
            state = input()
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{state}&appid={api_key}&units=imperial'
            print()
            connect()
            print()
            # use try catch block in case of invalid input from the user
            try:
                json_data = requests.get(url).json()
                temp = json_data['main']['temp']
                temp = round(temp, 0)
                print(f'the weather for {city.capitalize()}, {state.capitalize()} is {temp} degrees Fahrenheit')
                add_more()
            except KeyError:
                print('we ran into an issue. please try again ')
                print()
                main()

        # if user wants to search for weather based on zip
        elif chosen_option in zip_list:
            print('What is the Zip code of the city you would like the weather for?')
            zip_code = input()
            # making sure the zip code entered is a correct length of 5 digits
            if len(zip_code) < 5 or len(zip_code) > 5:
                print('You did not enter a valid 5 digit zip code.')
                print('Would you like to try again? (Y or N)')
                go_back = input()
                if go_back in yes_list:
                    main()
                elif go_back in no_list:
                    quit()
            elif len(zip_code) == 5:
                url = f'http://api.openweathermap.org/data/2.5/weather?zip={zip_code}&appid={api_key}&units=imperial'
                connect()
                # use try catch block in case of invalid input from the user
                try:
                    json_data = requests.get(url).json()
                    temp = json_data['main']['temp']
                    temp = round(temp, 0)
                    print(f'the weather for {zip_code}is {temp} degrees Fahrenheit')
                    add_more()
                except KeyError:
                    print('we ran into an issue. please try again ')
                    print()
                    main()

        # if user asks for help
        elif chosen_option in help_list:
            print()
            help_if_asked()

        # if user wants to quit
        elif chosen_option in quit_list:
            print('Thank you for using the program')
            quit()

    # if user makes an invalid selection
    elif chosen_option not in accepted_entry:
        print('you made an invalid selection. Please try again.')
        print()
        main()


# call main function to start the program
main()
