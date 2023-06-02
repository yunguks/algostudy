"""
꿀 따기 서브태스크
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	512 MB	6443	2259	1759	37.983%
문제
아래와 같이 좌우로 
$N$개의 장소가 있다.

장소들 중 서로 다른 두 곳을 골라서 벌을 한 마리씩 둔다. 또, 다른 한 장소를 골라서 벌통을 둔다. 
아래 그림에서 연한 회색의 장소는 벌이 있는 장소이고 진한 회색의 장소는 벌통이 있는 장소이다.

두 마리 벌은 벌통으로 똑바로 날아가면서 지나가는 모든 칸에서 꿀을 딴다. 각 장소에 적힌 숫자는 벌이 지나가면서 꿀을 딸 수 있는 양이다.

두 마리가 모두 지나간 장소에서는 두 마리 모두 표시된 양 만큼의 꿀을 딴다. (벌통이 있는 장소에서도 같다.)
벌이 시작한 장소에서는 어떤 벌도 꿀을 딸 수 없다.
위의 그림과 같이 배치된 경우 두 마리의 벌 모두 
$4 + 1 + 4 + 9 + 9 = 27$의 꿀을 따서, 전체 꿀의 양은 54가 된다.

위의 그림과 같이 배치된 경우 왼쪽 장소에서 출발한 벌은 
$9 + 4 + 4 + 9 + 9 = 35$의 꿀을 따고 오른쪽 장소에서 출발한 벌은 
$4 + 9 + 9 = 22$의 꿀을 따므로, 전체 꿀의 양은 
$57$이 된다.

위의 그림과 같은 경우는 전체 꿀의 양이 31이 된다.

장소들의 꿀 양을 입력으로 받아 벌들이 딸 수 있는 가능한 최대의 꿀의 양을 계산하는 프로그램을 작성하라.

입력
첫 번째 줄에 장소의 수 
$N$이 주어진다.

다음 줄에 왼쪽부터 각 장소에서 꿀을 딸 수 있는 양이 공백 하나씩을 사이에 두고 주어진다.

출력
첫 번째 줄에 가능한 최대의 꿀의 양을 출력한다.

제한
각 장소의 꿀의 양은 
$1$ 이상 
$10~000$ 이하의 정수이다.
서브태스크
번호	배점	제한
1	11	

2	13	

3	31	

4	45	
추가적인 제한이 없음.

예제 입력 1 
7
9 9 4 1 4 9 9
예제 출력 1 
57
예제 입력 2 
7
4 4 9 1 9 4 4
예제 출력 2 
54
예제 입력 3 
3
2 5 4
예제 출력 3 
10
"""
import sys

if __name__=="__main__":
    N = int(sys.stdin.readline().rstrip())
    honey = list(map(int,sys.stdin.readline().split()))
    # 미리 합을 구해두고 시작
    sum_honey = [honey[0]]
    for i in range(1,len(honey)):
        sum_honey.append(sum_honey[-1]+honey[i])
    # print(sum_honey)
    # 중간값에서 꿀
    result = sum_honey[-1] - honey[0]-honey[-1]+max(honey)
    # print(first,honey[1:-1])

    # 왼쪽에서 오른쪽 ->
    for i in range(1,N-1):
        # print("second")
        # print(honey[1:i],honey[i+1:])
        result = max(result, sum_honey[-1] - honey[0] -honey[i] + sum_honey[-1]-sum_honey[i])

    # 오른쪽에서 왼쪽 <-
    # print("third")
    for i in range(1,N-1):
        # print(honey[i+1:-1], honey[:i])
        result = max(result, sum_honey[-1]-honey[-1]-honey[i] +sum_honey[i-1])
    
    print(result)