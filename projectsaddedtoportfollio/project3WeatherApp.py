import requests

def weather_retreive(prompt1, prompt2):
    try:
        latitude = float(input(prompt1))
        longitude = float(input(prompt2))
    except ValueError:
        print('Invalid response, give a decimal response(eg: 31.912 or 78.986). Please rerun the program to try again')
        return

    url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        current = data['current_weather']
        print(f"Tempurature is: {current['temperature']}°C")
        print(f"Weather code is: {current['weathercode']}. Search it up to find the conditions.")

weather_retreive('What is the latitude of the place you want to get weather data from? ', 'What is the longditude you want to get weather data from? ')