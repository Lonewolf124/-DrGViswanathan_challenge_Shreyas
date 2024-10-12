def check(list1):
    top = list1[0]
    people_in_front = 0
    for i in range(0, len(list1)):
        if list1[i] > top:
            
        

            people_in_front += 1
    return people_in_front 

test_cases = int(input())
list3 = []
for i in range(test_cases):
    taimur, a, b, c = map(int, input().split())
    values_list = [taimur, a, b, c]
    result = check(values_list)
    list3.append(result)

for i in range(len(list3)):
    print(list3[i])
