def check(username):
    count=0
    list1=[]
    for letter in username:
        if letter not in list1:
            list1.append(letter)
        
    
    if (len(list1))%2!=0:
        return "IGNORE HIM!"
    else:
        return "CHAT WITH HER!"




username = str(input())
result = check(username.lower())
print(result)