t = int(input())

medians = []

for _ in range(t):
    a, b, c = map(int, input().split())
    median = sorted([a, b, c])[1]
    medians.append(median)

for median in medians:
    print(median)
