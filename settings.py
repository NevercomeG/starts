# settings.py
# Global Variables
global health
global armor
global stamin

class player:
    def __init__(self,userid,health,armor,stamin):
        self.userid = userid
        self.health = health
        self.armor = armor
        self.stamin = stamin
