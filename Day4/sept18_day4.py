def check(s):

    # Initialize a new list to store the result
    new_list = []
    removed_list=[]

    # Add the first stone to the list
    if len(s) > 0:
        new_list.append(s[0])

    
    for i in range(1, len(s)):
        # If the current stone is not the same as the previous one then add it to the new_list
        if s[i] != s[i-1]:
            new_list.append(s[i])
        else:
            removed_list.append(s[i])

    return len(removed_list) 


# input the no of stones 
stones = int(input())

# Input string representing the colors of the stones
s = input()  



if len(s)==stones:
    result = check(s)
    print(result)
else:
    pass

