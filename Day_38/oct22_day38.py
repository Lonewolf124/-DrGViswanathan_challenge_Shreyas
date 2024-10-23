import math 

def check(n,m,a):
    length_stones =math.ceil( n/a)
    width_stones = math.ceil( m/a)
    return length_stones * width_stones


n,m,a = map(int,input().split())

result =  check(n,m,a)
print(result)