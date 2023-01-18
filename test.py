import webbrowser
class House:
    def __init__(self, mapurl) -> None:
        self.mapurl = mapurl

    def ShowMap(self):
        webbrowser.open(self.mapurl, new=2)
        
#Main program
myHouse = House("https://www.google.com/maps/place/The+Peanut/@38.8871376,-94.593401,15z/data=!4m5!3m4!1s0x0:0x870965017c19f4a5!8m2!3d38.8925689!4d-94.6073517")
myHouse.ShowMap()