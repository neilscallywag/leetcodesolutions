def lols(s:str) -> int:
    seen= []
    s = [x for x in s]
    for i,j in enumerate(s):
        print('i=',i,'j=',j)
        if j in seen:
            print(j,'in seen',seen)
            print('prepops',s)
            seen.remove(j)
            print('postpops',s)
        else:
            print(j, 'not in seen')
            seen.append(j)
            print('seen',seen)
            
    return len(seen
               )+1

print(lols("diopdfuasdiofhdasiogfhadsiugfFWDFskjfhdsf"))
        
