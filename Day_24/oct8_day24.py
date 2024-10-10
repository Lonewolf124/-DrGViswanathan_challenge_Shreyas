list1=[]
upper=[]
lower=[]
def change1(word):
    
    
    for i in range(0,len(word)):
        list1.append(word[i])

    
    count(list1)
    
   
def count(list1):
    for i in list1:

        if i.isupper()==True:
            upper.append(i)
        else:
            lower.append(i)
    
    check()
def check():
    if len(upper)>len(lower):
        print(word.upper())
    else:
        print(word.lower())
word = input()
change1(word)

    
    
