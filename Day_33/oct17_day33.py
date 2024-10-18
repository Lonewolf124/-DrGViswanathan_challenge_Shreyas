lst = [" that I hate", " that I love"]

def check(n):
    if n == 1:
        string1 = "I hate"
    else:
        string1 = "I hate" 
        for i in range(2, n + 1):
            if i % 2 == 0:
                string1 += lst[1]  
            else: 
                string1 += lst[0]  
    
    result = string1 + " it"
    print(result)

n = int(input())
check(n)
