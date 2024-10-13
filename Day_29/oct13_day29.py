def check(ticket_string):
    
    if sum(map(int, ticket_string[:3])) == sum(map(int, ticket_string[3:])):
        return "YES"
    else:
        return "NO"

test_cases = int(input()) 
results = []

for _ in range(test_cases):
    ticket_string = input().strip() 
    if len(ticket_string) == 6: 
        results.append(check(ticket_string))


     
for result in results:
    print(result)
