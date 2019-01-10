'''
Problem3
관리자가 아래의 자료 두개를 하나로 만들어 달라고 한다. 제출할 이름은 submit_result이다.

예시)
data_f1 = {'a':"apple", 'b':"banana", 'c':'cherry'}
data_f2 = {'o':"orange", 'p':"pineapple"}

결과)
submit_result = {'a':"apple", 'b':"banana", 'c':'cherry', 'o':"orange", 'p':"pineapple"}
'''
data_f1 = {'a':"apple", 'b':"banana", 'c':'cherry'}
data_f2 = {'o':"orange", 'p':"pineapple"}

data_f1.update((data_f2))
print(data_f1)
