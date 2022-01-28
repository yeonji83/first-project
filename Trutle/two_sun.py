"""

Python Programing - two sun


"""


# turtle 모듈 가져오기
from turtle import *

sun = Turtle()
small_sun = Turtle()

# 선은 red 그리고 yellow 로 채우기
sun.color('red', 'yellow')
small_sun.color('yellow', 'orange')

small_sun.penup()
small_sun.back(200)
small_sun.pendown()

# 색상 채우기 시작
sun.begin_fill()
small_sun.begin_fill()

# 무한 루프
while True:

    small_sun.forward(100)
    small_sun.left(170)

    sun.forward(200)
    sun.left(170)

    if abs(position()) < 1:
        break

# 색상 채우기 끝
sun.end_fill()
small_sun.end_fill()

sun.hideturtle()
small_sun.hideturtle()

done()
    