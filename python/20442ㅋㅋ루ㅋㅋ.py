"""
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	1024 MB	744	277	194	35.401%
문제
ㅋㅋ루ㅋㅋ 문자열은 다음과 같이 정의한다.

R로만 이루어진 문자열은 ㅋㅋ루ㅋㅋ 문자열이다. 단, 빈 문자열은 ㅋㅋ루ㅋㅋ 문자열이 아니다.
ㅋㅋ루ㅋㅋ 문자열 양 끝에 K를 하나씩 붙인 문자열은 ㅋㅋ루ㅋㅋ 문자열이다.
입력
첫째 줄에 K와 R로만 이루어진 문자열이 주어진다. 문자열의 길이는 최대 3,000,000이다.

출력
주어진 문자열의 부분 수열 중 가장 긴 ㅋㅋ루ㅋㅋ 문자열의 길이를 출력한다. 부분 수열 중 ㅋㅋ루ㅋㅋ인 문자열이 없는 경우, 0을 출력한다.

예제 입력 1 
KKRKK
예제 출력 1 
5
예제 입력 2 
RRKRR
예제 출력 2 
4
"""
import sys
from collections import Counter
if __name__=="__main__":
    string = sys.stdin.readline().rstrip()
    # R만 뽑을 경우
    result = Counter(string)['R']
    Rcount = result
    length = len(string)
    left = 0
    right = 1
    Kleft = 0
    Kright = 0 
    # KRK 로 확인하기
    while True:
        # R이 없다면 종료
        if length < (left+right) or Rcount < 1:
            break
        # 왼쪽 K가 더 많을 경우
        if Kleft > Kright:
            if string[-right]=="K":
                Kright +=1
            else:
                Rcount -=1
            right +=1
        # 같거나 오른쪽 K가 더 많을 경우 
        else:
            if string[left] == "K":
                Kleft +=1
            else:
                Rcount -=1
            left+=1
        # 양쪽의 K의 개수가 같을 때 문자열 길이 계산
        if Kright == Kleft:
            result = max(result, 2*Kleft+Rcount)

    print(result)