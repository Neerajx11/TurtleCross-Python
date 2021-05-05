import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()

score = Scoreboard()
player = Player()
car = CarManager()

screen.onkey(player.moveForward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # create car and make them move
    car.createCar()
    car.moveCar()

    # detect collision
    for c in car.carList:
        if c.distance(player) < 20:
            game_is_on = False
            score.gameOver()

    # detect succ crossing
    if player.isAtFinishLine():
        player.gotoStart()
        car.levelUp()
        score.levelUp()
        score.updateScoreboard()


screen.exitonclick()
