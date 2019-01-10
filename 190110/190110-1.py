'''
Problem1
사원 J씨가 자료를 정리하다가 모든 글자를 소문자로 만들었는데 관리자가 앞글자는 모두 대문자로 만들어 달라고 한다.
그리고 모든 자료들을 리스트로 만들어서 오름차순을 진행한다.
J씨를 도와 문제를 해결해주시길 바랍니다.
submit_list에 담아 보여주세요

예시)
str_data = "james justine martine mary unix linux java cotline tomas script moonjaein"
submit_list = []

결과)
['James', 'Justine', 'Martine', 'Mary', 'Unix', 'Linux', 'Java', 'Cotline', 'Tomas', 'Script', 'Moonjaein']
'''
str_data = "james justine martine mary unix linux java cotline tomas script moonjaein"
submit_list = str_data.split()
print(submit_list)
