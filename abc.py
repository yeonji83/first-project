sum = 0

for x in range(1,100,1):
    
    if x % 7 != 0:
     sum = sum+x
    
    if sum>1000:
        break

print("1+2+3+...n의 합계(7의 배수는 제외)가 최초로 1000이 넘게 하는 숫자 n은 %d입니다" %x)