import requests

class Weather:
    def __init__(self, city):
        API = 'your api'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp'] - 273.15
            feels_like = data['main']['feels_like'] - 273.15
            humidity = data['main']['humidity']
            description = data['weather'][0]['description']

            self.temp = str(round(temp))
            self.feels_like = str(round(feels_like))
            self.humidity = str(round(humidity))
            self.description = description

        else:
            print('Error')