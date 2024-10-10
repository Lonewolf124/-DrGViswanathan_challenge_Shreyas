
#taking input in the form {a,b,c}
input_data =input()



#removing the curly braces and splitting by the commas 

letters = set(item.strip() for item in input_data.strip("{}").split(","))


list=[]
count=0


if input_data == "{}":
    count=0  
# print("length = " , len(letters))
else:
    for i in letters:
        if i not in list:
            count+=1

print(count)