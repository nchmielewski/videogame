# weather.py


import engine
import date

weather_sky_dict = {0:"It's sunny.", 1:"It's partly sunny.", 2:"It's partly cloudy.", 3:"It's cloudy.", 4:"It's raining", 5:"It's snowing :3", 6:"It's hailing!!", 7:"It's thunderstorming!", 8:"THERE'S A BLIZZARD!!", 9:"THERE'S A HURRICANE!!!", 10:"It's foggy.",11:"THIS WINTER STORM IS DEADLY. MAY IT HAVE MERCY."}
weather_wind_dict = {-1:"The wind is still.", 0:"The wind is calm.", 1:"There's a light breeze."}
weather_temp_dict = {0:"The air is freezing.", 1:"The air is cold.", 2:"The air is chilly.", 4:"The air is cool.", 5:"The air is warm.", 6:"The air is hot.", 7:"The air is scorching."}

class Weather:
    def __init__(self, w):
        self.weather = w # tuple: sky, wind, temp
        
    # Args: 
    #   Weather tuple (sky int, wind int, temp int)
    #   Time string
    #   Date string
    def m_weather(self, _weather=(0,0,0), _time=str("00:00.00"), _date=str("0/0/0000")):
        sky=_weather[0]
        wind=_weather[1]        
        temp=_weather[2]
        t = _time
        d = _date

        # Sunny to cloudy works in a chain, and then weather effects can happen when it's cloudy
        # Wind is average (0-6)

        # If it's cloudy, it can turn into either rain or snow
        # Wind can pick up (0-8)

        # If it's raining and becomes cold or freezing, it can turn into hail
        # No wind change

        # If it's sunny or partly sunny shortly after rain, a rainbow can appear
        # Wind can die down (0-6)

        # If it's snowing, wind can die down (0-7)

        # If there's a blizzard, wind picks up (8-11)
        # Chance to turn deadly (subzero)

        # If there's a hurricane, wind picks up (8-12)
        
        print(self.weather_sky_dict[sky])
        print(self.weather_wind_dict[wind])
        print(self.weather_temp_dict[temp])

        return (sky, wind, temp)