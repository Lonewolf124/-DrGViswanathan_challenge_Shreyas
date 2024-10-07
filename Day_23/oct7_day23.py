
n, k = map(int, input().split())
scores = list(map(int, input().split()))


threshold_score = scores[k - 1]


advancers = sum(1 for score in scores if score >= threshold_score and score > 0)

print(advancers)
