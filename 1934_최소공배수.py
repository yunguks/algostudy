from calendar import c
import sys

lines = int(sys.stdin.readline())

def gcd(a,b):
    if a < b:
        a, b = b, a
    while b!=0:
        c = a%b
        a = b
        b = c
    return a


for _ in range(lines):
    a, b = map(int,sys.stdin.readline().split())
    print(a*b//gcd(a,b))