import json
with open(USCities.json) as f:
    data = json.load(f)

for city in data['zip_code_directory']:
    print(city['city'])
