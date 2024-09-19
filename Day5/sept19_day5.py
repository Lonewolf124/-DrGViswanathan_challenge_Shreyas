def steps_calculator(house_cordinate):

    #choice which elephant can take 
    choice = [1,2,3,4,5]

    #steps
    steps=0

    while(house_cordinate > len(choice)) :
        
            # elephant will take 1st step as 5 
            house_cordinate -= choice[4]
            steps+=1



    for i in range(0,len(choice)) :
        
        if choice[i]==house_cordinate :
            steps+=1
        
    return steps






#input the cordinate of the friends house
house_cordinate = int(input())

result=steps_calculator(house_cordinate)
print(result)

