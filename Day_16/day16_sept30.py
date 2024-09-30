results = []

def check_sum(a, b, c):
    if a + b == c or a + c == b or b + c == a:
        results.append("YES")
    else:
        results.append("NO")

test_cases = int(input())
for _ in range(test_cases):
    a, b, c = map(int, input().split())
    if 0 <= a <= 20 and 0 <= b <= 20 and 0 <= c <= 20:
        check_sum(a, b, c)

for result in results:
    print(result)