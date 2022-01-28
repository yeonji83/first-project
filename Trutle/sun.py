
# turtle 모듈 가져오기
from turtle import *

# 선은 red 그리고 yellow 로 채우기
color('red', 'yellow')

# 색상 채우기 시작
begin_fill()

# 무한 루프
while True:
    forward(200)
    left(170)

    if abs(position()) < 1:
        break

# 색상 채우기 끝
end_fill()

hideturtle()

done()
    