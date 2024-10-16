s = str(input())
r = s.split('+')
list2=[]

for i in range(0,len(r)):
    list2.append(int(r[i]))
list2.sort()
result = '+'.join(map(str, list2))
print(result)