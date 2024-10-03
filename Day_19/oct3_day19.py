
def check(list1):
    Tetrahedron=4 
    Cube= 6 
    Octahedron= 8
    Dodecahedron=12 
    Icosahedron=20 
    count=0
    for i in list1 :
        if i == "Tetrahedron":
            count+=Tetrahedron
        elif i == "Octahedron":
            count+=Octahedron
        elif i == "Dodecahedron":
            count+=Dodecahedron
        elif i == "Cube":
            count+=Cube
        else:
            count+=Icosahedron   

    return count 




list1 =[]
n = int(input())
for i in range(0,n):
    shape= str(input())
    list1.append(shape)

result = check(list1)
print(result)