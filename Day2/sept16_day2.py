limark,bob= map(int,input().split())


for i in range(1,100):
    limark=limark*3
    bob=bob*2
    if limark>bob:
        num = i
        break
print(i)