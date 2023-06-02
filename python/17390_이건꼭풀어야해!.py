"""
문제
숭실골 높은 언덕 깊은 골짜기에 출제로 고통 받는 욱제가 살고 있다!

욱제는 또 출제를 해야 해서 단단히 화가 났다. 그래서 욱제는 길이 N짜리 수열 A를 만들고, A를 비내림차순으로 정렬해서 수열 B를 만들어 버렸다!! 여기서 B를 출력하기만 하면 문제가 너무 쉬우니까 하나만 더 하자. 아래와 같은 질문이 무려 Q개나 주어진다!! (ㅎㅎ;; ㅈㅅ.. ㅋㅋ!!)

L R: BL + BL+1 + ... + BR-1 + BR 을 출력한다.

욱제의 질문에 답하고 함께 엠티를 떠나자!!

입력
첫 번째 줄에 수열 A의 길이 N과 질문의 개수 Q가 공백으로 구분되어 주어진다. (1 ≤ N, Q ≤ 300,000)

두 번째 줄에 N개의 정수 A1, A2, ..., AN 이 공백으로 구분되어 주어진다. Ai 는 수열 A의 i 번째 수이다. (1 ≤ Ai ≤ 1,000)

세 번째 줄부터 Q개의 줄에 걸쳐 욱제의 질문을 의미하는 두 수 L, R이 공백으로 구분되어 주어진다. (1 ≤ L ≤ R ≤ N)

주어지는 모든 입력은 자연수이다.

출력
Q개의 줄에 걸쳐, 질문의 답을 순서대로 각각 출력한다.

예제 입력 1 
5 6
2 5 1 4 3
1 5
2 4
3 3
1 3
2 5
4 5
예제 출력 1 
15
9
3
6
14
9
[2, 5, 1, 4, 3]을 비내림차순으로 정렬하면 [1, 2, 3, 4, 5]이다.

예제 입력 2 
5 3
2 5 1 2 3
1 3
2 3
1 5
예제 출력 2 
5
4
13
"""
import sys

if __name__ == "__main__":
    N, Q = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    A = sorted(A)

    sum_list = [A[0]]
    for i in range(1, len(A)):
        sum_list.append(A[i] + sum_list[-1])
        
    for _ in range(Q):
        L, R = map(int, sys.stdin.readline().split())
        if L == 1:
            print(sum_list[R-1])
        else:
            # L번의 왼쪾에 있는 sum을 뺴야한다
            print(sum_list[R-1] - sum_list[L-1-1])