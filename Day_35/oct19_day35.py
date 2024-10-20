def check(char_input):
    word = ['c', 'o', 'd', 'e', 'f', 'r', 's']
    for i in range(len(word)):
        if char_input == word[i]:
            
            return "YES"
    return "NO"

test_Cases = int(input())
list1 = []

for i in range(test_Cases):
    char_input = str(input())
    result = check(char_input)
    list1.append(result)


for result in list1:
    print(result)
