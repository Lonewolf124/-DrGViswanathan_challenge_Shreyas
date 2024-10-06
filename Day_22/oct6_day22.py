no_events = int(input()) 
events = list(map(int, input().split())) 
police = 0  
crime = 0 

if len(events) == no_events:
    for i in range(len(events)): 
        if events[i] == -1: 
            if police > 0: 
                police -= 1 
            else:
                crime += 1 
        else:
            police += events[i]  


print(crime)