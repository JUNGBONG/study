'''
[Problem2]
구름다리를 건너는 토끼
토끼는 강을 건너기 위해 구름다리를 건너려고 합니다
구름다리의 발판에 적혀있는 숫자가 첫 번째부터 순서대로 들어있는 배열 steps가 매개변수로 주어질 때, 토끼가 구름다리를 모두 건너기 위해 필요한 점프 횟수를 반환하도록 crossBridge 함수를 작성하고자 합니다.


발판의 숫자들이 담긴 배열 steps가 주어졌을 때 토끼가 뛰어야 할 횟수를 반환하는 함수 crossBridge()의 빈칸을 채워 함수를 완성해봅시다.
예를들어 이렇게 호출하면

crossBridge([1, 1, 2, 3, 5])
다음 값이 반환됩니다.

4
설명
1번째 칸이 숫자 1이므로 1칸 점프합니다.
2번째 칸이 숫자 1이므로 1칸 점프합니다.
3번째 칸이 숫자 2이므로 2칸 점프합니다.
5번째 칸이 숫자 5이므로 5칸 점프합니다. (도착)
4번 점프했으므로 4를 반환합니다.



def crossBridge(steps):
    cnt = 0
    current = 0
    n = len(steps)
    while (/* 이곳을 채워주세요! */):
        current += /* 이곳을 채워주세요! */
        cnt += 1
    return cnt


'''


def crossBridge(steps):
    cnt = 0
    current = 0
    n = len(steps)
    while (n>=current):
        current += steps[current]
        cnt += 1
    return cnt

crossBridge([1, 1, 2, 3, 5])


#2시간 해도 안되서 소스 봐버렸습니다. ㅜㅜ



