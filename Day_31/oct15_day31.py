def check(a, b, c):
    if a + b == c:
        return '+'
    else:
        return '-'


test_cases = int(input())
result = []


for _ in range(test_cases):
    a, b, c = map(int, input().split())
    result.append(check(a, b, c))

for res in result:
    print(res)
