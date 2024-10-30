
n = int(input())


current_passengers = 0
max_capacity = 0


for _ in range(n):
    a, b = map(int, input().split())  
    current_passengers -= a           
    current_passengers += b           
    max_capacity = max(max_capacity, current_passengers)  

print(max_capacity)
