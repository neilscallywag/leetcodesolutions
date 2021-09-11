points = [[0,0],[2,2],[3,10],[5,2],[7,0]]


def cpp(points):
    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
            print("find","edge",x,"parent",parent[x])
        return parent[x]
    
    parent = list(range(len(points)))
    print("parent",parent)
    g = []
    print("g",g)
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            g.append((i, j, abs(points[j][1]-points[i][1]) + abs(points[j][0]-points[i][0])))

    print("foruvw",sorted(g, key=lambda x:x[2]))
    
    cost = 0
    print(cost)
    for u, v, w in sorted(g, key=lambda x:x[2]):
  
        ru, rv = find(u), find(v)
        print("Edge X",ru,"Edge Y",rv)
        if ru == rv:    # u and v must not be connected for now
            continue
        parent[ru] = rv
        print("Pedge X",parent[ru], "Edge Y", rv)
        cost += w
        print(cost)
    
    return cost

print(cpp(points))
