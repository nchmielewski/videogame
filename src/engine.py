# game clock
# seconds, minutes, hours, days, weeks, months, years
# every second in real life is a minute in game
# 1/60th (0.01667) of a second in real life is a second in game, an irrational number!

# Weather can be sunny, partly sunny, partly cloudy, cloudy, raining, snowing, hailing, thunderstorming, blizzard, hurricane (0-9); wind is based on Beaufort numbers (https://www.rochesterfirst.com/weather/weather-blog/breezy-gusty-and-windy-whats-the-difference/)
# Time will track the gameclock, time, and date
# Map will track locations of places of interest, players, and NPCs


# Engine will have a loading overhead if we constantly load large lists when we're calling methods, best to create class obj to stick around

word_list = [{1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'},
                ['zero',"First","Second","Third","Fourth","Fifth","Sixth","Seventh","Eighth","Ninth","Tenth","Eleventh","Twelfth","Thirteenth","Fourteenth","Fifteenth","Sixteenth","Seventeenth","Eighteenth","Nineteenth","Twentieth","Twenty First","Twenty Second","Twenty Third","Twenty Fourth","Twenty Fifth","Twenty Sixth","Twenty Seventh","Twenty Eighth","Twenty Ninth","Thirtieth","Thirty First","Thirty Second"]
                ]

TICK_VAL = int(254)

def _Y():
    for x in range(0,TICK_VAL):
        pass


import weather

class Engine:

    def __init__(self):
        _tick = 0

    def generate_word(self):
        word_list
        return

    def tick(self):
        # Tick 0 - init
        # Check 
        
        # Increment and check next tick for weather, clock, and map
        
        # Return True if event, else False
        return
    
    def load_state(self):
        file = open("save.txt", "r")
        content = file.read()
        file.close()
        return content
    
    def write_state(self):
        file = open("save.txt", "w")
        content = file.read()
        file.close()