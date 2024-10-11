def check(list1, list2):
    length1 = len(list1)
    length2 = len(list2)

    
   
    for i in range(length1):
        
        if list1[i] != list2[length2 - i - 1]:
            return "NO"
    
    return "YES"

def input1(s1, s2):
    list1 = []
    list2 = []

    
    for i in s1:
        list1.append(i)

    for i in s2:
        list2.append(i)
    
    if len(list1) == len(list2):
        
        result = check(list1, list2)  
        print(result)
    else :
        print("NO")

s1 = input()    
s2 = input()
input1(s1, s2)
