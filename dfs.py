
graph = { 'a': ['c','b'], 'b': ['d'],'c':['e'],'d':['f'],'e':[],'f':[] }
graph2 = {
    'i':['j','k'],
    'j':['i'],
    'k':['i','m','l'],
    'm':['k'],
    'l':['k'],
    'o':['n'],
    'n':['o']
    }

def dfs(graph,node):
    stack = [node]
    while(len(stack) > 0):
        curr = stack.pop()
        print(curr)
        for x in graph[curr]:
            stack.append(x)


dfs(graph,'a')

#acyclic graph
def haspath(graph,src,dst):
    if src == dst:
        return True
    for x in graph[src]:
        if haspath(graph,x,dst) == True:
            return True
    return False


print(haspath(graph,'f','a'))

#cyclic graph

def haspath2(graph2,src,dst,visited=[]):
    if src in visited:
        return False
    if src == dst:
        return True
    visited.append(src)

    for x in graph2[src]:
        if haspath2(graph2,x,dst,visited)== True:
            return True
    return False

print(haspath2(graph2,'i','l',visited=[]))

