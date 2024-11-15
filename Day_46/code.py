n = int(input())
c = input()
i = 1

while n > 1:
    a = input()
    if c[1] == a[0]:
        i += 1
        c = a  
    n -= 1

print(i)
