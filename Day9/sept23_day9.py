count=0

def check(p,q):
    if (q>p and q-p>1):
       return True    


#no of rooms
no_of_rooms = int(input())
for i  in range(0,no_of_rooms):
    p , q = map(int,input().split())
    result=check(p,q)
    if result==1:
        count+=1
    



print(count)


