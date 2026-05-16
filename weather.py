import requests
def get_weather(city):
    api_key = "f5b5eb6d9deadf23ea2e0c1772acf5ec"
    url = f"http://openweathermap.org{city}&appid={api_key}&units=metric"