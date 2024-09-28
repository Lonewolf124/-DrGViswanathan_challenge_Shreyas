had_shoes = list(map(int, input().split()))
actual_shoe = []
unique_shoes = set()

for shoe in had_shoes:
    if shoe not in unique_shoes:
        unique_shoes.add(shoe)
        actual_shoe.append(shoe)

# print( actual_shoe)
count = 4
remaining_count = count - len(actual_shoe)
print(remaining_count)