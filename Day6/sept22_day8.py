def who_won(num1,str1):
    list1 = []
    Anton = 0
    Danik = 0
    for i in str1:
        list1.append(i)
    for i in list1 :
        if i=="A":
            Anton+=1
        elif i=="D":
            Danik+=1
        else:
            pass
    if Anton>Danik:
        print("Anton")
    elif Anton<Danik:
        print("Danik")
    else:
        print("Friendship")

num1 = int(input())
str1 = input()
who_won(num1,str1)
