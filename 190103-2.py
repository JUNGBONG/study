'''
*오늘 배운 문제에서 점수에 따른 학점을 print해주는 문제를 심화해보겠습니다.
문제는 java의 조건문인 switch문을 알아야하기에 이미지를 참조해주세요.
이해를 못하시는 분은 >=가 아닌 ==으로 나오게 하는거라고 이해하셔도 됩니다.(다만, 100점일때 처리가 필요하긴 합니다)

[Problem002]
'''
score = int(input("점수(숫자만) 입력해주세요"))
result = ""

'''
90점 이상은 "A"
 95점 이상은 "+"를 붙여서 A+을 출력해주세요.
80점 이상은 "B"
 85점 이상은 "+"를 붙여서 B+을 출력해주세요.
70점 이상은 "C"
 75점 이상은 "+"를 붙여서 C+을 출력해주세요.
70점 미만은 "F"
'''
valuec = "C"
if score >= 90:
    if score >= 95:
        print("A+")
    else:
        print("A")
elif score >= 80:
    if score >= 85:
        print("B+")
    else:
        print("B")
elif score >= 70:
    if score >=75:
        print(f"{valuec}"+"+")
    else:
        print(f"{valuec}")
else:
    print("F")

