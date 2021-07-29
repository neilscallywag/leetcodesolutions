#You're  given  an  unsorted  array  of  integers  where  every  integer  appears  exactly 
#twice, except  for  one  integer  which  appears  only  once.  Write  an algorithm  (in  a 
#language  of  your  choice) that  finds  the  integer  that  appears  only  once.

def findint(a):
    hm=set()
    s = 0
    for i,j in enumerate(a):
        if j in hm:
            s -= j
        else:
            hm.add(j)
            s +=j  
    return s
    
    



print(findint([1,1,2,2,3,4,4]))
            
