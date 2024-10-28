import math
t = int(input())
res = []
for i in range(t):
    n = int(input())
    x,y = map(int, input().split())
    t = 0
    c = y
    if(x >= y):
        t = n/y
        res.append(math.ceil(t))
        continue
    else:
        t = n/x
        res.append(math.ceil(t))
        
    
for i in res:
    print(i)
