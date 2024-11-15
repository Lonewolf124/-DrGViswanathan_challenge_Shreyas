l1=[]
k=int(input())
l=int(input())
m=int(input())
n=int(input())
d=int(input())
for i in range(1,d+1):
    if i % k == 0:
        l1.append(i)  # Add multiples of k
    if i % l == 0:
        l1.append(i)  # Add multiples of l
    if i % m == 0:
        l1.append(i)  # Add multiples of m
    if i % n == 0:
        l1.append(i)  # Add multiples of n
# print(l1)
s=set(l1)
print(len(s))
