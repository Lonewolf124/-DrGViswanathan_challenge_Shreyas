def capitalization(string):
    for i in string:
        
        a=i.capitalize()
        break;
    return a+string[1:]
word = input()
capitalized_word = capitalization(word)
print(capitalized_word)