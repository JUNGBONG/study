'''
개구리 왕자 이름 찾기
“혹시 여기에 개구리 왕자님이 계신가요?”

엘사는 수많은 개구리 중 이름이 F로 시작하는 개구리 왕자를 찾으려고 합니다.

(단, 개구리들은 개성이 넘쳐서 이름과 시작하는 알파벳이 다릅니다.)

문자열이 여러개 담긴 리스트 frogList가 매개변수로 주어졌을 때, 문자열이 'F’로 시작하면 그 이름을 return 하도록 isPrince() 함수를 작성했습니다. 그러나, 코드 일부분이 잘못되어있기 때문에 코드가 올바르게 동작하지 않습니다. 주어진 코드를 변경해서 대해 올바르게 동작하도록 수정하세요.

frogList에 담긴 문자열 중 'F’로 시작하는 값을 return 하는 isPrince 함수를 동작하도록 수정하기.
(단, frogList에는 반드시 F으로 시작하는 이름이 하나 들어있습니다.)

예를들어 이렇게 함수를 호출하면

isPrince(['Alice', 'Bob', 'Frog'])
이렇게 반환합니다.

Frog


def isPrince(frogList):
    for elem in frogList:
        if elem[0] == "F":
            pass
        return None

'''


#결과값 나오는 함수
def isPrince(frogList):
    for elem in frogList:
        if elem[0] != "F":
            continue
        return elem





'''
파이썬 pass와 continue 차이점
pass는 실행 할 것이 아무 것도 없다는 것을 의미. 따라서 아무런 동작을 하지 않고 다음 코드를 실행
continue는 다음 순번의 loop 실행
'''


