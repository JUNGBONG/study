'''
[Problem3]
복소수 complex_data를 켤레복소수로 만드는 함수 complex_conjugate를 만들어주세요.

예제)
    복소수의 표기는 본래 i이므로 i로 하도록 하겠습니다.
    프로그래밍을 하는데에는 j로 사용하셔야 합니다.
    complex_conjugate(5i) => -5i
    complex_conjugate(3+7i) => (3-7i)
'''
def complex_conjugate(x):
    a = x.imag
    if a*a > 0:
        x=x
    else a*a <0:
        x=-x
    return x
complex_conjugate(5i)
complex_conjugate(3+7i)
