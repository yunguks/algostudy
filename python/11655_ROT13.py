from codecs import ascii_decode, ascii_encode
import sys

# 문자를 아스키로 ord() 'A-Z' 65-90 'a-z' 97-122
# 아스키를 문자로 chr()
# output을 만들어서 print하나 , temp가 하나씩 나올 때마다 print하나 
# 메모리 크기는 똑같이 씀 / 대신 시간은 temp를 하나씩 할때가 더 빠름

line = sys.stdin.readline().rstrip('\n')

output = []

for i in line:
    temp = ord(i)
    if 64<temp<91:
        temp +=13
        if temp > 90:
            temp -=26
    elif 96<temp<123:
        temp +=13
        if temp > 122:
            temp -=26
    temp=chr(temp)
    
    output.append(temp)
print(*output,sep='')