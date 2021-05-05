from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.carList = []
        self.carSpeed = STARTING_MOVE_DISTANCE

    def createCar(self):
        ranChance = random.randint(1, 6)
        if ranChance == 1:
            newCar = Turtle("square")
            newCar.shapesize(stretch_len=2, stretch_wid=1)
            newCar.color(random.choice(COLORS))
            newCar.penup()
            randYCor = random.randint(-250, 250)
            newCar.setpos(300, randYCor)
            newCar.setheading(180)
            self.carList.append(newCar)

    def moveCar(self):
        for car in self.carList:
            car.forward(self.carSpeed)

    def levelUp(self):
        self.carSpeed += MOVE_INCREMENT
