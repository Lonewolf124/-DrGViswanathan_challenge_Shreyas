def check(n, k, l, c, d, p, nl, np):
    
    total_ml = k * l
    toasts_from_drinks = total_ml // nl
    toasts_from_limes = c * d
    toasts_from_salt = p // np
    
    
    min_toasts = min(toasts_from_drinks, toasts_from_limes, toasts_from_salt)
    
    
    return min_toasts // n


n, k, l, c, d, p, nl, np = map(int, input().split())
result = check(n, k, l, c, d, p, nl, np)
print(result)
