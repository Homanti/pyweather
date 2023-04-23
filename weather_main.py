#імпорт
from weather_func import Weather
from gps import get_city
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from datetime import datetime
from PyQt5.QtGui import QBrush, QPixmap, QPalette
print('hello')


#пусті зміні
temperature = " "
humidity = " "
feelslike = " "
description = " "

#словник
words = {
    "lineWeather": "Word your tower",
    "btnLocalization": "Українська",
    "btnSearch": "🔍 Search",
    "labelTemp": "🌡️ Temperature: ",
    "labelFeelslike": "🌡️ Feels like: ",
    "labelHumidity": "💦 Humidity: ",
    "labelCity": "🏙️ City: ",
    "btnGps": "📍GPS",
    "labelTime": "🕘As of: ",

    "clear sky": "☀️ Clear sky",
    "few clouds": "🌤️ Few clouds",
    "scattered clouds": "☁️ Scattered clouds",
    "broken clouds": "☁️ Broken clouds",
    "shower rain": "🌧️ Shower rain",
    "light rain": "🌦️ Light rain",
    "heavy intensity rain": "🌦️ Heavy intensity rain",
    "very heavy rain": "🌦️ Very heavy rain",
    "extreme rain": "🌦️ Extreme rain",
    "freezing rain": "🌦️ Freezing rain",
    "light intensity shower rain": "🌦️ Light intensity shower rain",
    "heavy intensity shower rain": "🌦️ Heavy intensity shower rain",
    "ragged shower rain": "🌦️ Ragged shower rain",
    "rain": "🌦️ Rain",
    "moderate rain": "🌦️ Moderate rain",
    "thunderstorm": "⛈️ Thunderstorm",
    "snow": "🌨️ Snow",
    "mist": "🌫️ Mist",
    "overcast clouds": "☁️ Overcast clouds",
}

#створення вікна
app = QApplication([])
win = QWidget()
win.setWindowTitle("PyWeather")
win.resize(800, 700)

#додаєм фон
pixmap = QPixmap("data/background.png")
brush = QBrush(pixmap)
palette = QPalette()
palette.setBrush(QPalette.Background, brush)
win.setPalette(palette)

#css
app.setStyleSheet("""
        QLineEdit {
            background: #404040;
            border-radius: 5px;
            color: #B7B7B7;
            min-height: 50px;
            min-width: 100px;
            margin: 0px;
        }
        QPushButton {
            background: #1b6eb7;
            color: #B7B7B7;
            min-height: 50px;
            min-width: 110px;
            border-radius: 5px;
            margin: 0px;
        }
        QGroupBox {
            background: #242424;
            min-height: 100px;
            min-width: 600px;           
            border-radius: 5px;
            margin: 0px;
        }
        QLabel {
            color: #555555;
            font-size: 25px;
        }
        """)

#функція виводу погоди
def WeatherPrint():
    weathersearch = lineWeather.text()
    searchweather = Weather(weathersearch)
    temperature = searchweather.temp
    feels_like = searchweather.feels_like
    humidity = searchweather.humidity
    description = searchweather.description
    now = datetime.now()
    current_time = now.strftime("%x, %X")
    labelTime.setText(words["labelTime"] + current_time)
    labelTemp.setText(words["labelTemp"] + temperature + "°")
    labelFeelslike.setText(words["labelFeelslike"] + feels_like + "°")
    labelHumidity.setText(words["labelHumidity"] + humidity + "°")
    labelCity.setText(words["labelCity"] + weathersearch)
    labelDescription.setText(words[description])

#функція виводу погоди по gps
def gpssearch():
    city = get_city()
    searchweather = Weather(city)
    temperature = searchweather.temp
    feels_like = searchweather.feels_like
    humidity = searchweather.humidity
    description = searchweather.description
    now = datetime.now()
    current_time = now.strftime("%x, %X")
    labelTime.setText(words["labelTime"] + current_time)
    labelTemp.setText(words["labelTemp"] + temperature + "°")
    labelFeelslike.setText(words["labelFeelslike"] + feels_like + "°")
    labelHumidity.setText(words["labelHumidity"] + humidity + "°")
    labelCity.setText(words["labelCity"] + city)
    labelDescription.setText(words[description])

#створення віджетів
lineWeather = QLineEdit("")
lineWeather.setPlaceholderText(words["lineWeather"])
btnLocalization = QPushButton(words["btnLocalization"])
btnLocalization.setObjectName("btnLocalization")
btnSearch = QPushButton(words["btnSearch"])
btnGps = QPushButton(words["btnGps"])
groupBackground = QGroupBox(" ")
labelWeather = QLabel()
labelTemp = QLabel(" ")
labelFeelslike = QLabel(" ")
labelHumidity = QLabel(" ")
labelCity = QLabel(" ")
labelDescription = QLabel(" ")
labelTime = QLabel(" ")

#відцентрування тексту
labelTime.setAlignment(Qt.AlignCenter)
labelCity.setAlignment(Qt.AlignCenter)
labelHumidity.setAlignment(Qt.AlignCenter)
labelFeelslike.setAlignment(Qt.AlignCenter)
labelTemp.setAlignment(Qt.AlignCenter)
labelDescription.setAlignment(Qt.AlignCenter)

#створення ліній
mainLine = QVBoxLayout()
horLine = QHBoxLayout()

#розміщення віджетів на лінії
mainLine.addWidget(labelTime)
mainLine.addWidget(labelCity)
mainLine.addWidget(labelTemp)
mainLine.addWidget(labelFeelslike)
mainLine.addWidget(labelHumidity)
mainLine.addWidget(labelDescription)
mainLine.addStretch()

groupBackground.setLayout(horLine)
mainLine.addWidget(groupBackground)
horLine.addWidget(lineWeather)
horLine.addWidget(btnSearch)
horLine.addWidget(btnGps)
horLine.addWidget(btnLocalization)

#розміщення головної лінії
win.setLayout(mainLine)

#функція локалізації
def localization():
    global words
    if words["btnLocalization"] == "Українська":
        words = {
            "lineWeather": "Напиши своє місто",
            "btnLocalization": "English",
            "btnSearch": "🔍 Пошук",
            "labelTemp": "🌡️ Температура: ",
            "labelFeelslike": "🌡️ Відчуваєтся як: ",
            "labelHumidity": "💦 Вологість: ",
            "labelCity": "🏙️ Місто: ",
            "btnGps": "📍Пошук по геолокації",
            "labelTime": "🕘Станом на: ",

            "clear sky": "☀️ Чисте небо",
            "few clouds": "🌤️ Небагато хмар",
            "scattered clouds": "☁️ Хмарно",
            "broken clouds": "☁️ Розірвані хмари",
            "light rain": "🌦️ Невеликий дощ",
            "moderate rain": "🌦️ Помірний дощ",
            "heavy intensity rain": "🌦️ Сильний дощ",
            "very heavy rain": "🌦️ Дуже сильний дощ",
            "extreme rain": "🌦️ Екстрімальний дощ",
            "freezing rain": "🌦️ Крижаний дощ",
            "light intensity shower rain": "🌦️ Дощ легкої інтенсивності",
            "shower rain": "🌧️ Злива",
            "heavy intensity shower rain": "🌦️ Дощ",
            "ragged shower rain": "🌦️ Сильний зливовий дощ",
            "rain": "🌦️ Дощ",
            "thunderstorm": "⛈️ Гроза",
            "snow": "🌨️ Сніг",
            "mist": "🌫️ Туман",
            "overcast clouds": "☁️ Похмурні хмари",
        }
    else:
        words = {
            "lineWeather": "Word your tower",
            "btnLocalization": "Українська",
            "btnSearch": "🔍 Search",
            "labelTemp": "🌡️ Temperature: ",
            "labelFeelslike": "🌡️ Feels like: ",
            "labelHumidity": "💦 Humidity: ",
            "labelCity": "🏙️ City: ",
            "btnGps": "📍GPS",
            "labelTime": "🕘As of: ",

            "clear sky": "☀️ Clear sky",
            "few clouds": "🌤️ Few clouds",
            "scattered clouds": "☁️ Scattered clouds",
            "broken clouds": "☁️ Broken clouds",
            "light rain": "🌦️ Light rain",
            "moderate rain": "🌦️ Moderate rain",
            "heavy intensity rain": "🌦️ Heavy intensity rain",
            "very heavy rain": "🌦️ Very heavy rain",
            "extreme rain": "🌦️ Extreme rain",
            "freezing rain": "🌦️ Freezing rain",
            "light intensity shower rain": "🌦️ Light intensity shower rain",
            "shower rain": "🌧️ Shower rain",
            "heavy intensity shower rain": "🌦️ Heavy intensity shower rain",
            "ragged shower rain": "🌦️ Ragged shower rain",
            "rain": "🌦️ Rain",
            "thunderstorm": "⛈️ Thunderstorm",
            "snow": "🌨️ Snow",
            "mist": "🌫️ Mist",
            "overcast clouds": "☁️ Overcast clouds",
        }

    lineWeather.setPlaceholderText(words["lineWeather"])
    btnLocalization.setText(words["btnLocalization"])
    btnSearch.setText(words["btnSearch"])
    btnGps.setText(words["btnGps"])

#прив'язання кнопок до функцій
btnSearch.clicked.connect(WeatherPrint)
btnLocalization.clicked.connect(localization)
btnGps.clicked.connect(gpssearch)

#кінець)
win.show()
app.exec_()
