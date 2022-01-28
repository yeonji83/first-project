
from turtle import *
shape("turtle")  # 터틀의 모양을 설정 tt. > 터틀에서 제공하는 함수

count = 50  #count에 50 저장
bgcolor("black") # 배경색 검정
color("blue")    # 그리는 색 파랑
speed(0) # 그리는 속도 설정 0이 가장 빠름, 1이 제일 느림

for x in range(count):  # 반복문 50번 반복
    circle(80)       # 반지름이 80픽셀인 원을 그림
    left(360/count)  # 360/50 = 7.2도 만큼 왼쪽으로 회전함

hideturtle() # 터틀 숨기기

done()   #화면을 붙잡아두기

