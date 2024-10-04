def check(r, b):
  
    diff_socks_days = min(r, b)

   
   
    r -= diff_socks_days
    b -= diff_socks_days

  
    same_socks_days = (r // 2) + (b // 2)

    return diff_socks_days, same_socks_days


r, b = map(int, input().split())

a, s = check(r, b)


print(a, s)
