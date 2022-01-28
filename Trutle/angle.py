import turtle as tt # turtle모듈을 가져오고 tt로 부른다

tt.shape("turtle")

angle = 89
tt.bgcolor("black")
tt.color("peachpuff")
tt.speed(0)

for x in range(200):    # x거리 만큼 직선을 그리고 89도 꺽는다 > x 1 증가 200번 반복
    tt.forward(x)
    tt.left(angle)

tt.hideturtle()

tt.done()