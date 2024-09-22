
def subtraction (n,k) :
    steps=0
    while (steps!=k):
        last_digit = n%10
        
        # print(last_digit)
        if last_digit==0 :
            n = n // 10 ;    
            steps+=1
        else :
            n-=1
            steps+=1
    print(n)  
      



n , k = map (int,input().split())
subtraction(n,k)







