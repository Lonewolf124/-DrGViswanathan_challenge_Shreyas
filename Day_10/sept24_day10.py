
def distinct_digits(year):
   
    year_str = str(year)
    return len(set(year_str)) == len(year_str)

def next_distinct_year(year):
    year += 1
    while not distinct_digits(year):
        year += 1
    return year


y = int(input())

print(next_distinct_year(y))
