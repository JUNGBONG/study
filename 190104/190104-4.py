'''
[Problem4]
토끼와 거북이의 달리기 경주
토끼와 거북이가 달리기 경주를 시작했습니다.

토끼는 N분에 한번 휴식을 하고 거북이는 M분에 한번 휴식을 한다고 합니다.

토끼와 거북이가 처음으로 같은 타이밍에 쉬는 시간은 언제일까요?

토끼의 휴식시간 N과 거북이의 휴식시간 M이 매게 변수로 주어졌을때, 토끼와 거북이가 동시에 휴식하는 최초의 시간을 출력하는 프로그램을 작성해봅시다.
예를들어 다음 입력이 주어지면

3 5
이렇게 출력됩니다.

15
'''

def run(n,m):
    answer =0
    temp1 =0
    temp3 = 0
    temp2 =0
    if n > m:
        n,m = m,n
        temp2 =m%n
    else:
        temp2 =m%n
    while temp2!=0:
       temp4 =int(m/n)
       answer =temp4/temp2
       temp2 =temp4%temp2
    return n*m/answer

#뭔가 배울때 더 짧았던거 같은데 기분탓인가??
#음수처리 추가해야겠다.
   
