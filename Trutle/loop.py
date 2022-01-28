from turtle import *
speed(10)
shape("turtle")

penLength = 5
colorIndex = 0
#Pen Length, Color Index 초기값 설정
 
color = ["black", "orange", "red", "yellow", "purple", "green", "blue", "grey", "cyan"]
#Color 리스트의 각 Index에 색상을 저장

#for Loop 0~199까지 반복
for x in range(200):
    pencolor(color[colorIndex]) #Pen color를 color 리스트의 color Index에 해당하는 Index에 자장된 색상으로 설정 
    right(90)   #turtle 오른쪽으로 90도 회전
    forward(penLength)  #penLength만큼 forward

    penLength = penLength + 5   #penLength에 5를 더해 다음 루트에서 5만큼 앞으로 가게 함
    colorIndex = colorIndex + 1 #colorIndex에 1을 더해서 color 리스트에서 그 다음 색 설정
    if colorIndex >= 9: #colorIndex가 9이상이면 다시 0으로 돌아가도록 설정
        colorIndex = 0

hideturtle()
done()