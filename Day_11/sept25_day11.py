def check(a,b,c):
    if (a==1 and b==1):
        return True
    elif(a==1 and c==1):
        return True
    elif(b==1 and c==1):
        return True
    else:
        return False

no_of_prb = int(input())
count=0
for i in range(0,no_of_prb):
    a ,b ,c = map(int,input().split())
    result=check(a,b,c)    
    if result==True:
        count+=1

print(count)