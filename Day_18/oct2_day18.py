def Pangram(string_char):
    
    alphabet_set = set("abcdefghijklmnopqrstuvwxyz")
    
    
    input_set = set(string_char.lower())
    
   
    if alphabet_set.issubset(input_set):
        print("YES")
    else:
        print("NO")

number_of_char = int(input())
string_char = input()


if number_of_char == len(string_char):
    Pangram(string_char)
else:
    print("NO")