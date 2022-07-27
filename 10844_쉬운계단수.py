'''
문제
45656이란 수를 보자.

이 수는 인접한 모든 자리의 차이가 1이다. 이런 수를 계단 수라고 한다.

N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구해보자. 0으로 시작하는 수는 계단수가 아니다.

입력
첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.

출력
첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.

예제 입력 1 
1
예제 출력 1 
9
예제 입력 2 
2
예제 출력 2 
17
'''
import sys

n = int(sys.stdin.readline())
count = [0,1,1,1,1,1,1,1,1,1]

if n==1:
    count_sum=9

for i in range(2,n+1):
    temp=[0,0,0,0,0,0,0,0,0,0]
    temp[0]=count[1]%1000000000
    temp[1]=count[0]+count[2]%1000000000
    temp[2]=count[1]+count[3]%1000000000
    temp[3]=count[2]+count[4]%1000000000
    temp[4]=count[3]+count[5]%1000000000
    temp[5]=count[4]+count[6]%1000000000
    temp[6]=count[5]+count[7]%1000000000
    temp[7]=count[6]+count[8]%1000000000
    temp[8]=count[7]+count[9]%1000000000
    temp[9]=count[8]%1000000000
    count=temp
print(sum(count)%1000000000)
    
        