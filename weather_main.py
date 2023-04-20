from weather_func import Weather
from gps import get_city
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

temperature = " "
humidity = " "
feelslike = " "
description = " "

words = {
    "lineWeather": "Word your tower",
    "btnLocalization": "Українська",
    "btnSearch": "🔍 Search",
    "labelTemp": "🌡️ Temperature: ",
    "labelFeelslike": "🌡️ Feels like: ",
    "labelHumidity": "💦 Humidity: ",
    "labelCity": "🏙️ City: ",
    "btnGps": "📍GPS",

    "clear sky": "☀️ Clear sky",
    "few clouds": "🌤️ Few clouds",
    "scattered clouds": "☁️ Scattered clouds",
    "broken clouds": "☁️ Broken clouds",
    "shower rain": "🌧️ Shower rain",
    "rain": "🌦️ Rain",
    "thunderstorm": "⛈️ Thunderstorm",
    "snow": "🌨️ Snow",
    "mist": "🌫️ Mist",
    "overcast clouds": "☁️ Overcast clouds",
}

app = QApplication([])
win = QWidget()
win.setWindowTitle("PyWeather")
win.resize(800, 700)

app.setStyleSheet("""
        QWidget {
            background: #25518e;
        }
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
            color: #B7B7B7;
            font-size: 25px;
        }
        """)

def WeatherPrint():
    weathersearch = lineWeather.text()
    searchweather = Weather(weathersearch)
    temperature = searchweather.temp
    feels_like = searchweather.feels_like
    humidity = searchweather.humidity
    description = searchweather.description
    labelTemp.setText(words["labelTemp"] + temperature + "°")
    labelFeelslike.setText(words["labelFeelslike"] + feels_like + "°")
    labelHumidity.setText(words["labelHumidity"] + humidity + "°")
    labelCity.setText(words["labelCity"] + weathersearch)
    labelDescription.setText(words[description])

def gpssearch():
    city = get_city()
    searchweather = Weather(city)
    temperature = searchweather.temp
    feels_like = searchweather.feels_like
    humidity = searchweather.humidity
    description = searchweather.description
    labelTemp.setText(words["labelTemp"] + temperature + "°")
    labelFeelslike.setText(words["labelFeelslike"] + feels_like + "°")
    labelHumidity.setText(words["labelHumidity"] + humidity + "°")
    labelCity.setText(words["labelCity"] + city)
    labelDescription.setText(words[description])

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

labelCity.setAlignment(Qt.AlignCenter)
labelHumidity.setAlignment(Qt.AlignCenter)
labelFeelslike.setAlignment(Qt.AlignCenter)
labelTemp.setAlignment(Qt.AlignCenter)
labelDescription.setAlignment(Qt.AlignCenter)

mainLine = QVBoxLayout()
horLine = QHBoxLayout()

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

win.setLayout(mainLine)

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

            "clear sky": "☀️ Чисте небо",
            "few clouds": "🌤️ Небагато хмар",
            "scattered clouds": "☁️ Хмарно",
            "broken clouds": "☁️ Розірвані хмари",
            "shower rain": "🌧️ Злива",
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

            "clear sky": "☀️ Clear sky",
            "few clouds": "🌤️ Few clouds",
            "scattered clouds": "☁️ Scattered clouds",
            "broken clouds": "☁️ Broken clouds",
            "shower rain": "🌧️ Shower rain",
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

btnSearch.clicked.connect(WeatherPrint)
btnLocalization.clicked.connect(localization)
btnGps.clicked.connect(gpssearch)
win.show()
app.exec_()