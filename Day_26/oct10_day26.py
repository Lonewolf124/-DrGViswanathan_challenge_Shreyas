test_cases = int(input())
list=[]
for i in range(0,test_cases):
    word =str(input())
   
    if len(word)==3:
        word = word.upper()
        if word == "YES":
            list.append("YES")
        else:
            list.append("NO")
for i in list:
    print(i)
    