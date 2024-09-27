# Read the number of friends
n = int(input())

# Read the list of friends who gave gifts
givers = list(map(int, input().split()))

# Initialize a list to store the results (who received gifts)
receivers = [0] * n

# Fill the receivers list
for i in range(n):
   
    receivers[givers[i] - 1] = i + 1 

# Print the result
print(" ".join(map(str, receivers)))
