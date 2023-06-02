'''
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	512 MB	3456	1389	1012	39.362%
문제
고양이는 너무 귀엽다. 사람들은 고양이를 너무 귀여워했고, 결국 고양이와 더욱 가까워지고 싶어 고양이와의 소통을 위한 고양이 말 번역기를 발명하기로 했다. 이 번역기는 사람의 언어를 고양이의 언어로, 고양이의 언어를 사람의 언어로 바꾸어 주는 희대의 발명품이 될 것이다.

현재 고양이말 번역기의 베타버전이 나왔다. 그러나 이 베타버전은 완전 엉망진창이다. 베타버전의 번역기는 문자열을 주면 그 중에서 최대 N개의 종류의 알파벳을 가진 연속된 문자열밖에 인식하지 못한다. 굉장히 별로지만 그나마 이게 최선이라고 사람들은 생각했다. 그리고 문자열이 주어졌을 때 이 번역기가 인식할 수 있는 최대 문자열의 길이는 얼마인지가 궁금해졌다.

고양이와 소통할 수 있도록 우리도 함께 노력해보자.

입력
첫째 줄에는 인식할 수 있는 알파벳의 종류의 최대 개수 N이 입력된다. (1 < N ≤ 26)

둘째 줄에는 문자열이 주어진다. (1 ≤ 문자열의 길이 ≤ 100,000) 단, 문자열에는 알파벳 소문자만이 포함된다.

출력
첫째 줄에 번역기가 인식할 수 있는 문자열의 최대길이를 출력한다. 

예제 입력 1 
2
abbcaccba
예제 출력 1 
4
'''
import sys
if __name__=="__main__":
    N = int(sys.stdin.readline().rstrip())
    lines = sys.stdin.readline().rstrip()
    result = 0
    len_lines = len(lines)
    count_dict = {}
    start = 0
    end = 0
    if N==1:
        result = 1
    elif N >= len(set(lines)):
        result = len_lines
    else:
        while True:
            if end == len_lines:
                break
            # 딕셔너리 확인, 크면 앞에서 부터 빼기
            if len(count_dict) > N:
                count_dict[lines[start]] -=1
                if count_dict[lines[start]] == 0:
                    del count_dict[lines[start]]
                start+=1
            else:
                # 딕셔너리에 추가
                result = max(result, end-start)
                
                if lines[end] in count_dict.keys():
                    count_dict[lines[end]] +=1
                else:
                    count_dict[lines[end]] = 1
                end+=1
            # print(start, end, len(count_dict), result, count_dict, lines[start:end])
                
    print(result)

