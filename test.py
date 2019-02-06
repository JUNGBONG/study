def solution(num):
    num=num+1
    while 1:
        a=[]
        for i in str(num):
            a.append(i)
            
        
        if str(0) in a:
            num =num+1
            print(num)
        else:
            return num

num = 9949999
ret = solution(num)
