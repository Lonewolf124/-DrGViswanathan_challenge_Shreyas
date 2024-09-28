def check(a, b):
    if a % b == 0:
        return 0
    
    remainder = a % b
    moves = b - remainder  # The number of increments needed to make `a` divisible by `b`
    
    return moves

test_cases = int(input())
results = []

for i in range(test_cases):
    a, b = map(int, input().split())
    result = check(a, b)
    results.append(result)

for res in results:
    print(res)
