from collections import Counter

guest_name = input().strip()
host_name = input().strip()
pile_of_letters = input().strip()

combined_names = guest_name + host_name

combined_count = Counter(combined_names)
pile_count = Counter(pile_of_letters)


if combined_count == pile_count:
    print("YES")
else:
    print("NO")

