import pygame

class Ship:
    def __init__(self, health:int=1, score:int=0, speed:int=10) -> None:
        self.health = health
        self.score = score
        self.speed = speed

    def getHealth(self) -> int:
        return self.health
    
    def addHealth(self, val:int) -> None:
        self.health += val
    
    def getScore(self) -> int:
        return self.score
    
    def setScore(self, val:int) -> None:
        self.score = val
    
    def addScore(self, val:int) -> None:
        self.score += val

    def getSpeed(self) -> int:
        return self.speed
    
    def setSpeed(self, val:int) -> None:
        self.speed = val
    
    def getImage():
        return pygame.image.load('images/spaceship.png')
    