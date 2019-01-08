celendar = {
    1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 
    7:31, 8:31, 9:30, 10:31, 11:30, 12:31
}
weeks = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
#multi line selector,multi line cursor  컨트롤 +t, vscode는 알트, 에디터마다 다름


count_week = 0
for month,count in celendar.items():
    count_week = 0 + count_week 
    print(f"{month:10} 월")
    
    for week in weeks:
        print(f"{week:2}", end=" ")
    print()
    print(count_week*"   ",end="")
    for day in range(1,count+1):
        
        print(f"{day:2}", end =" ")
        count_week +=1
        if count_week ==7:
            print()
            count_week = 0
    
    print()
