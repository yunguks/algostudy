'''
문제
Given a sequence of integers, a1, a2, …, an, we define its sign matrix S such that, for 1 ≤ i ≤ j ≤ n, Sij="+" if ai + … + aj > 0; Sij="−" if ai + … + aj < 0; and Sij="0" otherwise. 

For example, if (a1, a2, a3, a4)=( −1, 5, −4, 2), then its sign matrix S is a 4×4 matrix: 

 	1	2	3	4
1	-	+	0	+
2	 	+	+	+
3	 	 	-	-
4	 	 	 	+
We say that the sequence (−1, 5, −4, 2) generates the sign matrix. A sign matrix is valid if it can be generated by a sequence of integers. 

Given a sequence of integers, it is easy to compute its sign matrix. This problem is about the opposite direction: Given a valid sign matrix, find a sequence of integers that generates the sign matrix. Note that two or more different sequences of integers can generate the same sign matrix. For example, the sequence (−2, 5, −3, 1) generates the same sign matrix as the sequence (−1,5, −4,2). 

Write a program that, given a valid sign matrix, can find a sequence of integers that generates the sign matrix. You may assume that every integer in a sequence is between −10 and 10, both inclusive. 

입력
The first line contains an integer n(1 ≤ n ≤ 10), where n is the length of a sequence of integers. The second line contains a string of n(n+1)/2 characters such that the first n characters correspond to the first row of the sign matrix, the next n−1 characters  to the second row, ..., and the last character to the n-th row. 

출력
Output exactly one line containing a sequence of n integers which generates the sign matrix. If more than one sequence generates the sign matrix, you may output any one of them. Every integer in the sequence must be between −10 and 10, both inclusive.

예제 입력 1 
4
-+0++++--+
예제 출력 1 
-2 5 -3 1
예제 입력 2 
2
+++
예제 출력 2 
3 4
예제 입력 3 
5
++0+-+-+--+-+--
예제 출력 3 
1 2 -3 4 -5
'''
# pypy3 로 풀어서 시간맞춤..
import sys
# 중복하여서 들어 올 수 있다.
def check(numbers,k):
    global matrix
    s = 0
    # k개가 들어온다면 k번째 열 확인
    for i in range(k,-1,-1):
        s += numbers[i]
    
        # 한 열 씩만 확인하면 된다.
        if matrix[i][k]==0 and s !=0:
            return 0
        elif matrix[i][k]==1 and s <=0:
            return 0
        elif matrix[i][k]==-1 and s >=0:
            return 0
    return 1

def make_number(input):
    global n
    global matrix
    k = len(input)

    if k==n:
        print(*input)
        return 1

    temp = matrix[k][k]

    if temp==0:
        input.append(0)
        if make_number(input):
            return 1
        input.pop()
    else:
        for i in range(1,11):
            input.append(i*temp)
            if check(input,k) and make_number(input):
                return 1
            input.pop()

    return 0
input = sys.stdin.readline
n=int(input())
line = list(input().rstrip())

matrix = [[0 for i in range(n)]for j in range(n)]

for i in range(n):
    for j in range(i,n):
        temp = line.pop(0)
        if temp =='+':
            matrix[i][j]=1
        elif temp =='-':
            matrix[i][j]=-1

make_number([])

'''
# 시간 초과한 문제 , check를 그때 그때 한다면?
def check(numbers, matrix):

    s_matrix = [[0 for _ in range(len(numbers))] for _ in range(len(numbers))]
    for i in range(len(matrix)):
        s_matrix[i][i] = numbers[i]
        for j in range(0,i):
            temp = s_matrix[j][i-1]+numbers[i]
            s_matrix[j][i]=temp
            oper = matrix[j][i]
            if oper=='+':
                if temp <=0:
                    return 0
            elif oper=='-':
                if temp >=0:
                    return 0
            elif oper=='0':
                if temp !=0:
                    return 0

    return 1

def make_number(input,plus,minus):
    global n
    global matrix
    if len(input)==n:
        if check(input,matrix):
            print(*input)
        return 0
    x = matrix[len(input)][len(input)]
    if x=='+':
        for i in range(len(plus)):
            input.append(plus[i])
            plus.pop(i)
            make_number(input,plus,minus)
            plus.append(input.pop())
    elif x=='-':
        for i in range(len(minus)):
            input.append(minus[i])
            minus.pop(i)
            make_number(input,plus,minus)
            minus.append(input.pop())
    elif x=='0':
        input.append(0)
        make_number(input,plus,minus)
        input.pop()

input = sys.stdin.readline
n=int(input())
line = list(input().rstrip())

matrix = [['x' for i in range(n)]for j in range(n)]

for i in range(n):
    for j in range(i,n):
        matrix[i][j] =line.pop(0)

plus = [i for i in range(1,11)]
minus = [i for i in range(-1,-11,-1)]

make_number([],plus,minus)
'''