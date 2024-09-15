#no of people who will give their opinions 

n = int(input())
a=[]


# opinions

opinions= input().split()   
# print(opinions)
status=0
if len(opinions)==n:
    
    for i in range(0,len(opinions)):
        if opinions[i]=='0' or opinions[i]=='1':
            if opinions[i]=='1':
                status+=1
                break;
    
    if status==0:
            print("EASY")
    else :
            print("HARD")

