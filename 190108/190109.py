def MY_factorial(n,r):
    facto = 1
    facto2 = 1
    facto3 = 1
    for i in range(1,n+1):
        facto = facto*i
    for j in range(1,r+1):
        facto2 = facto2*j
    for k in range(1,n-r):
        facto3 = facto3*k
    return facto/(facto2*facto3)
print(MY_factorial(3,2))

#재귀함수로 짜고 싶은데 재귀함수를 잘모르겠습니다. ㅜ.ㅜ
