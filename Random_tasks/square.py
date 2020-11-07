import math

def square(side):
    params = []
    
    P = 4 * side
    S = side**2
    d = side * math.sqrt(2) 
    
    params.append(P)
    params.append(S)
    params.append(d)
    
    return params

print(square(4))