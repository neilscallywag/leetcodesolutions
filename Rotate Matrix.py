import numpy as np
matrix = [[1,2,3],[4,5,6],[7,8,9]]

def rotate(m):
    
    m.reverse()
    print(np.matrix(m))
    
    #for every Kij element of row replace it with Kji of cloumn (Transpose)
    for y in range(len(m)):
        
        for x in range(len(m[y])):
           m[y][x] ,m[x][y] = m[x][y], m[y][x]
           
        return m
    
    

print(np.matrix(matrix))
print(np.matrix(rotate(matrix)))


