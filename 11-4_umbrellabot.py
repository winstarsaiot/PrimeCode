from pystubit_iot import *
from pyatcrobo2.parts import Servomotor, UltrasonicSensor
from pystubit.board import display, Image
import time, json

sv13 = Servomotor('P13')
sv14 = Servomotor('P14')
us = UltrasonicSensor("P0")

WIFI_SSID = ""
WIFI_PWD = ""
response = wifi_connect(WIFI_SSID, WIFI_PWD, trytime=3)

CITY_ID = 1

WORDS_FINE = {"No Rain", "Fine", "Sunny", "Clear", "Clearing", "Bright",
                "Fair", "Mild"}
WORDS_RAINY = {"Thunderstorms", "Thundershowers", "Storm", "Showers",
                "Heavy Showers", "Rainshower", "Occasional Showers",
                "Scattered Showers", "Isolated Showers", "Light Showers",
                "Freezing Rain", "Rain", "Drizzle", "Light Rain", "Squall"}
WORDS_CLOUDY = {"Cloudy", "Partly Cloudy", "Sunny Intervals",
                "Mostly Cloudy", "Partly Bright"}
WORDS_SNOWY = {"Snow", "Flurries", "Heavy Snow", "Snowfall", "Light Snow",
                "Blizzard", "Blowing Snow", "Hail", "Snow Showers",
                "Snowstorm", "Snowdrift"}

IMG_FINE = Image("01110:11111:11111:11111:01110:", color=(30, 10, 0))
IMG_RAINY = Image("00100:01110:11111:00100:01100:", color=(0, 10, 30))
IMG_CLOUDY = Image("00000:01110:11111:01110:00000:", color=(15, 15, 15))
IMG_SNOWY = Image("10101:01110:11011:01110:10101:", color=(30, 30, 30))
IMG_OTHER = Image("00000:00000:01110:00000:00000:", color=(10, 5, 15))

# User define
def give_umbrella():
    sv13.set_angle(45)
    sv14.set_angle(135)
    time.sleep(3)
    sv13.set_angle(90)
    sv14.set_angle(90)

def get_icon(weather):
    if weather in WORDS_FINE:
        img = IMG_FINE
    elif weather in WORDS_RAINY:
        img = IMG_RAINY
    elif weather in WORDS_CLOUDY:
        img = IMG_CLOUDY
    elif weather in WORDS_SNOWY:
        img = IMG_SNOWY
    else:
        img = IMG_OTHER
    return img

def get_forecast():
    url_format = "https://worldweather.wmo.int/en/json/[City ID]_en.json"
    url = url_format.replace("[City ID]", str(CITY_ID))
    res = json.loads(get_request(url))
    weather = res["city"]["forecast"]["forecastDay"][0]["weather"]
    hi_temp = res["city"]["forecast"]["forecastDay"][0]["maxTemp"]
    lo_temp = res["city"]["forecast"]["forecastDay"][0]["minTemp"]
    img = get_icon(weather)
    display.show(img, delay=3000)
    display.scroll("Hi: " + hi_temp, delay=25, color=(31, 0, 0))
    display.scroll("Lo: " + lo_temp, delay=25, color=(0, 0, 31))
    if weather in WORDS_RAINY:
        give_umbrella()

# main program
sv13.set_angle(90)
sv14.set_angle(90)
while True:
    d = us.get_distance()
    if d > 0 and d < 30:
        get_forecast()
