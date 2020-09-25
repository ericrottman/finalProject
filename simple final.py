import json
import webbrowser
import urllib
import requests

print('welcome to the program')
print('we are here to help you with all your weather related needs')

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
def connect():
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

def weather_data():
    connect()
    #connection
    #read the text
    #save text to json

def full_weather():
    # temp = read from json data specific key for temp

api_key = 'd8aa257457ec1e26187f1410aaa7b258'
api_address = f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q='
quit_list = ['quit', 'q', 'end', 'no', 'n']
yes_list = ['yes', 'yeah', 'y', 'ok', 'k']
no_list = quit_list
help_list = ['help', 'h']

def main():
    print('To enter a city name please type [1]. To enter a Zip code please type [2].')
    data_type = input()
    if data_type == str('1'):
        print('What is the name of the city you would like the weather for?')
        city = input()
    elif data_type == str(2):
        print('What is the Zip code of the city you would like the weather for?')
        zip_code = input()
        if len(zip_code) < 5 :
            print('You did not enter a valid 5 digit zip code.')
            print('Would you like to try again? (Y or N)')
            go_back = input()
            if go_back in yes_list:
                    main()
            elif go_back in no_list:
                quit()
    connect()
    weather_data()
    full_weather()
    add_more()

main()