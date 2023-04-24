#імпорт
from weather_func import Weather
from gps import get_city
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from datetime import datetime
from PyQt5.QtGui import QBrush, QPixmap, QPalette


#пусті зміні
temperature = " "
humidity = " "
feelslike = " "
description = " "

#словник
words = {
    "lineWeather": "Write your city",
    "btnLocalization": "Українська",
    "btnSearch": "🔍 Search",
    "labelTemp": "🌡️ Temperature: ",
    "labelFeelslike": "🌡️ Feels like: ",
    "labelHumidity": "💦 Humidity: ",
    "labelCity": "🏙️ City: ",
    "btnGps": "📍GPS",
    "labelTime": "🕘As of: ",
    "labelError": "⛔ Error, you probably entered the name of the city incorrectly.",
    "labelError2": "⛔ Error.",

    "clear sky": "☀️ Clear sky",
    "few clouds": "🌤️ Few clouds",
    "scattered clouds": "☁️ Scattered clouds",
    "broken clouds": "☁️ Broken clouds",
    "overcast clouds": "☁️ Overcast clouds",

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

    "light snow": "🌨️ Light snow",
    "snow": "🌨️ Snow",
    "heavy snow": "🌨️ Heavy snow",
    "sleet": "🌨️ Sleet",
    "light shower sleet": "🌨️ Light shower sleet",
    "shower sleet": "🌨️ Shower sleet",
    "light rain and snow": "🌨️ Light rain and snow",
    "rain and snow": "🌨️ Rain and snow",
    "light shower snow": "🌨️ Light shower snow",
    "shower snow": "🌨️ Shower snow",
    "heavy shower snow": "🌨️ Heavy shower snow",

    "mist": "🌫️ Mist",
    "smoke": "🌫️ Smoke",
    "haze": "🌫️ Haze",
    "sand/dust whirls": "🌫️ Dust",
    "dust whirls": "🌫️ Dust",
    "fog": "🌫️ Fog",
    "sand": "🌫️ Sand",
    "dust": "🌫️ Dust",
    "volcanic ash": "🌫️ Ash",
    "squalls": "🌫️ Squalls",
    "tornado": "🌫️ Tornado",
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

def ClearText():
    labelTime.setText(" ")
    labelTemp.setText(" ")
    labelFeelslike.setText(" ")
    labelHumidity.setText(" ")
    labelCity.setText(" ")
    labelDescription.setText(" ")

#функція виводу погоди по назві міста
def WeatherPrint():
    try:
        location = lineWeather.text()
        weathersearch = Weather(location)
        temperature = weathersearch.temp
        feels_like = weathersearch.feels_like
        humidity = weathersearch.humidity
        description = weathersearch.description
        now = datetime.now()
        current_time = now.strftime("%x, %X")
        labelTime.setText(words["labelTime"] + current_time)
        labelTemp.setText(words["labelTemp"] + temperature + "°")
        labelFeelslike.setText(words["labelFeelslike"] + feels_like + "°")
        labelHumidity.setText(words["labelHumidity"] + humidity + "°")
        labelCity.setText(words["labelCity"] + location)
        labelDescription.setText(words[description])
    except:
        labelCity.setText(words["labelError"])
        ClearText()

#функція виводу погоди по gps
def gpssearch():
    try:
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
    except:
        labelCity.setText(words["labelError2"])
        ClearText()

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
            "labelError": "⛔ Помилка, ймовірно, ви неправильно ввели назву міста.",
            "labelError2": "⛔ Помилка.",

            "clear sky": "☀️ Чисте небо",
            "few clouds": "🌤️ Небагато хмар",
            "scattered clouds": "☁️ Хмарно",
            "broken clouds": "☁️ Розірвані хмари",
            "overcast clouds": "☁️ Похмурні хмари",

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

            "light snow": "🌨️ Дрібний сніг",
            "snow": "🌨️ Сніг",
            "heavy snow": "🌨️ Сильний сніг",
            "sleet": "🌨️ Мокрий сніг",
            "light shower sleet": "🌨️ Сніг",
            "shower sleet": "🌨️ Сніг",
            "light rain and snow": "🌨️ Дрібний дощ зі снігом",
            "rain and snow": "🌨️ Дощ і сніг",
            "light shower snow": "🌨️ Невеликий сніг",
            "shower snow": "🌨️ Снігова злива",
            "heavy shower snow": "🌨️ Сильний сніг",

            "mist": "🌫️ Туман",
            "smoke": "🌫️ Дим",
            "haze": "🌫️ Туман",
            "sand/dust whirls": "🌫️ Кружляє пил",
            "dust whirls": "🌫️ Кружляє пил",
            "fog": "🌫️ Туман",
            "sand": "🌫️ Пісок",
            "dust": "🌫️ Кружляє пил",
            "volcanic ash": "🌫️ Вулканічний попіл",
            "squalls": "🌫️ Шквали",
            "tornado": "🌫️ Торнадо",
        }
    else:
        words = {
            "lineWeather": "Write your city",
            "btnLocalization": "Українська",
            "btnSearch": "🔍 Search",
            "labelTemp": "🌡️ Temperature: ",
            "labelFeelslike": "🌡️ Feels like: ",
            "labelHumidity": "💦 Humidity: ",
            "labelCity": "🏙️ City: ",
            "btnGps": "📍GPS",
            "labelTime": "🕘As of: ",
            "labelError": "⛔ Error, you probably entered the name of the city incorrectly.",
            "labelError2": "⛔ Error.",

            "clear sky": "☀️ Clear sky",
            "few clouds": "🌤️ Few clouds",
            "scattered clouds": "☁️ Scattered clouds",
            "broken clouds": "☁️ Broken clouds",
            "overcast clouds": "☁️ Overcast clouds",

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

            "light snow": "🌨️ Light snow",
            "snow": "🌨️ Snow",
            "heavy snow": "🌨️ Heavy snow",
            "sleet": "🌨️ Sleet",
            "light shower sleet": "🌨️ Light shower sleet",
            "shower sleet": "🌨️ Shower sleet",
            "light rain and snow": "🌨️ Light rain and snow",
            "rain and snow": "🌨️ Rain and snow",
            "light shower snow": "🌨️ Light shower snow",
            "shower snow": "🌨️ Shower snow",
            "heavy shower snow": "🌨️ Heavy shower snow",

            "mist": "🌫️ Mist",
            "smoke": "🌫️ Smoke",
            "haze": "🌫️ Haze",
            "sand/dust whirls": "🌫️ Dust",
            "dust whirls": "🌫️ Dust",
            "fog": "🌫️ Fog",
            "sand": "🌫️ Sand",
            "dust": "🌫️ Dust",
            "volcanic ash": "🌫️ Ash",
            "squalls": "🌫️ Squalls",
            "tornado": "🌫️ Tornado",
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
