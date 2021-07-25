def sum(l,t):
    hm=dict()
    for i in range(len(l)):
        e = t-l[i]
        print("complement",e)
        if e in hm:
            return[l[i],hm[e]]
        hm[l[i]] = l[i]
        print("hm",hm[l[i]])
        print(hm)

print(sum([1,2,3,4,5,6,7,8,9,10,12,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26],24))
