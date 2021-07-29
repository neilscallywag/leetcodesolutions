
s = "df  dsfdsf dg dfg fdh fsdf sf weew dsfdsgfdsg "

def lenS(s:str):
    n =[]
    for y in s.split(" "):
        if y != "":
            n.append(y)
            
    return print(len(n[-1]))
   

lenS(s)
    
