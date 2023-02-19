'''
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	1023	395	339	44.430%
문제
Farmer John has N hills on his farm (1 <= N <= 1,000), 
each with an integer elevation in the range 0 .. 100. In the winter,
 since there is abundant snow on these hills, FJ routinely operates a ski training camp.

Unfortunately, FJ has just found out about a new tax that will be assessed next year on farms used as ski training camps.
Upon careful reading of the law, however, 
he discovers that the official definition of a ski camp requires the difference between the highest 
and lowest hill on his property to be strictly larger than 17. 
Therefore, if he shortens his tallest hills and adds mass to increase the height of his shorter hills, 
FJ can avoid paying the tax as long as the new difference between the highest and lowest hill is at most 17.

If it costs x^2 units of money to change the height of a hill by x units,
 what is the minimum amount of money FJ will need to pay?
  FJ is only willing to change the height of each hill by an integer amount.

입력
Line 1: The integer N.
Lines 2..1+N: Each line contains the elevation of a single hill.
출력
Line 1: The minimum amount FJ needs to pay to modify the elevations of his hills so the difference between largest and smallest is at most 17 units.
예제 입력 1 
5
20
4
1
24
21
예제 출력 1 
18

예제 입력 2
5
1
1
20
21
24

예제 출력 2
24


힌트
Input Details
FJ's farm has 5 hills, with elevations 1, 4, 20, 21, and 24.

Output Details
FJ keeps the hills of heights 4, 20, and 21 as they are. 
He adds mass to the hill of height 1, bringing it to height 4 (cost = 3^2 = 9). 
He shortens the hill of height 24 to height 21, also at a cost of 3^2 = 9.
'''
import sys
import math

def info():
    N = int(sys.stdin.readline())
    mount = []
    for _ in range(N):
        num = int(sys.stdin.readline())
        mount.append(num)

    return mount

def sol(mount):
    result = 0
    min_val = min(mount)
    max_val = max(mount)
    
    min_count = math.inf
    # 줄이는 범위를 제한
    if abs(max_val-min_val) > 17:
        for i in range(min_val,max_val-17+1):
            count = 0
            for m in mount:
                if m < i:
                    count += abs(m-i)**2
                elif m > i+17:
                    count += abs(i+17-m)**2
            # print(f"[{i}-{i+17}], {count}")
            if min_count > count:
                min_count = count
        result = min_count
    return result

if __name__=="__main__":
    mount = info()
    print(sol(mount))