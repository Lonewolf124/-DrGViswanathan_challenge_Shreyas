perfect = []  
levels = int(input())

for i in range(1, levels + 1):
    perfect.append(i)


input_line1 = input()
parts1 = input_line1.split()
num_cases1 = int(parts1[0]) 
x_cases = list(map(int, parts1[1:]))


input_line2 = input()
parts2 = input_line2.split()
num_cases2 = int(parts2[0])
y_cases = list(map(int, parts2[1:]))


if len(x_cases) == num_cases1 and len(y_cases) == num_cases2:
    
    combined_cases = x_cases + y_cases

    
    combined_cases = list(set(combined_cases))

   
    combined_cases.sort()

    
    if combined_cases == perfect:
        print("I become the guy.")
    else:
        print("Oh, my keyboard!")
