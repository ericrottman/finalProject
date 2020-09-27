import json
import webbrowser
import urllib
import requests
#This program is a draft
# It pulls weather info from openweathermap.org
print('welcome to the program')
print('we are here to help you with all your weather related needs')

#add more function used to allow user to loop
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
    r = requests.get('http://openweathermap.org')
    print("connecting....")
    for i in range(5):
        try:
            r.raise_for_status()
        except requests.exceptions.ConnectionError:
            print('we could not make a valid connection. Please try again')
            print('trying again up to 5 times')
        except requests.exceptions.HTTPError:
            print('no connection')
            print('trying again up to 5 times')

#still in progress....
def connect_2():
    url = 'http://openweathermap.org'
    for i in range(5):
        try:
            requests.get(url)
        except requests.ConnectionError:
            print('connection unsuccessful')
            print('retrying up to 5 times')
        print('Please check you connection and try again')
        add_more()

# set basic variables that will be needed for the program
api_key = 'd8aa257457ec1e26187f1410aaa7b258'
api_address = f'api.openweathermap.org/data/2.5/weather?appid={api_key}&q='
quit_list = ['quit', 'q', 'end', 'no', 'n']
yes_list = ['yes', 'yeah', 'y', 'ok', 'k']
no_list = quit_list
help_list = ['help', 'h']


def main():
    print('To search by City and State please type [1]')
    print('To search by Zip code please type [2].')
    data_type = input() #allows the user to choose what type of data they want to search by
    #attempt to limit input to just what is wanted or give error message for incorrect input. still in progress
    # if data_type != str('1') or str('2'):
    #     print('you made an invalid selection. Please try again/n')
    #     main()
    if data_type == str('1'):
        print('What is the name of the city you would like the weather for?')
        city = input()
        print(f'What state is {city} in? (Please use the full state name)')
        state = input()
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{state}&appid={api_key}&units=imperial'
        connect()
        json_data = requests.get(url).json()
        if json_data['message'] == 'Invalid API key. Please see http://openweathermap.org/faq#error401 for more info.':
            print('we encountered an error.')
            add_more()
        else:
            temp = json_data['main']['temp']
            temp = round(temp, 0)
            print(f'the weather for {city.capitalize()}, {state.capitalize()} is {temp} degrees Fahrenheit')
            add_more()

    elif data_type == str(2):
        print('What is the Zip code of the city you would like the weather for?')
        zip_code = input()
        #making sure the zip code entered is a correct length of 5 digits
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
            json_data = requests.get(url).json()
            temp = json_data['main']['temp']
            temp = round(temp, 0)
            print(f'the weather for {zip_code} is {temp} degrees Fahrenheit')
            add_more()


main()
