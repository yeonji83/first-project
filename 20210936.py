from turtle import * # turtle 모듈 가져오기
circle_ = Turtle()  # circle_ 객체 생성
circle_.shape("classic") # 터틀의 모양을 설정 ( 화살촉 모양 )
triangle_ = Turtle()    # triangle_ 객체 생성
triangle_.shape("classic")  # 터틀의 모양을 설정 ( 화살촉 모양 )
square_ = Turtle()  # square_ 객체 생성
square_.shape("classic")    # 터틀의 모양을 설정 ( 화살촉 모양 )
bgcolor("black") # 배경색 검정
xy = [[-300,0],[100,-100],[300,0]] # 시작좌표 리스트에 저장
colors = ('red', 'yellow', 'blue') # 색깔 tuple에 저장


circle_.color(colors[0])    # 선색을 tuple에 저장된 색깔로 colors[0] 이므로 'red'
square_.color(colors[2])    # 'blue'
circle_.hideturtle() # 터틀 사라짐 
square_.hideturtle()
circle_.penup() # 펜을 올림( 그림 안 그림 )
square_.penup()
circle_.goto(xy[0]) # 리스트에 저장된 x, y값 좌표로 이동 xy[0] 이므로 [-300,0]
square_.goto(xy[2]) # xy[2] 이므로 [300,0]
circle_.showturtle()    # 터틀 나타남
square_.showturtle()
circle_.pendown()   # 펜을 내림( 그림을 그림 )
square_.pendown()
circle_.speed(0)    # 그리는 속도 설정 0이 가장 빠름, 1이 제일 느림
square_.speed(0) 
for x in range(50):  # 반복문 50번 반복 
    circle_.circle(60)  # 반지름이 60픽셀인 원을 그림
    square_.forward(1)       # 앞으로 1 픽셀 만큼 이동.
    circle_.left(360/50)    # 각도를 7.2도 왼쪽으로 튼다.
    square_.right(90)   # 오른쪽으로 90도 회전
    square_.forward(4*x)  # 앞으로 4*x 픽셀 만큼 이동.

triangle_.color(colors[1], colors[1]) # 선과 채우기를 colors[1] 이므로 'yellow'
triangle_.penup()   # 펜을 올림( 그림 안 그림 )
triangle_.goto(xy[1])   # 리스트에 저장된 x, y값 좌표로 이동 xy[1] 이므로 [100,-100]
triangle_.pendown()  # 펜을 내림( 그림을 그림 )
triangle_.speed(0)  # 그리는 속도 설정 0이 가장 빠름, 1이 제일 느림
triangle_.begin_fill()  # 색상 채우기 시작
for y in range(3):  # 3번 반복
    triangle_.left(120) # 왼쪽 방향으로 120도 회전
    triangle_.forward(200)  # 앞으로 200픽셀 만큼 이동
triangle_.end_fill()    # 색상 채우기 끝

circle_.hideturtle() # 터틀 숨기기
triangle_.hideturtle()
square_.hideturtle()

done()   #화면을 붙잡아두기

