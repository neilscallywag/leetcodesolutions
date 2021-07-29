def bs(x,mi,ma):
    l = mi
    r = ma/2
    accuracy = 1/1000000
    while l < r:
        m = (l+r)/2
        if m*m > x:
            r = m - accuracy
        elif m*m < x:
            l = m+accuracy 
    return m
    
        
            

print(bs(3000,1,3000))
    
    
