def print_pattern(n, m):
    
    direction_right = True

    for row in range(1, n + 1):
        if row % 2 != 0:
            
            print('#' * m)
        else:
            if direction_right:
                
                print('.' * (m - 1) + '#')
            else:
               
                print('#' + '.' * (m - 1))
            
            direction_right = not direction_right

a , b  = map(int,input().split())
print_pattern(a,b)
