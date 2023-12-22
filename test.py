from collections import deque
def add_node(v):
    global node_count
    if v in nodes:
        print(v,"already present")
    else:
        node_count+=1
        nodes.append(v)
        for i in graph:
            i.append(0)
        temp=[]
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)
def add_edge(v1,v2):
    if v1 not in nodes:
        print(v1," not present in nodes")
    if v2 not in nodes:
        print(v2,"not present in nodes")
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=1
        graph[index2][index1]=1
def DFS(start_node,visited):
    if start_node not in nodes:
        print("node not present")
    index=nodes.index(start_node)
    visited[index]=True
    print(start_node,end=" ")
    for i in range(node_count):
        if graph[index][i]==1 and not visited[i]:
            DFS(nodes[i],visited)
def BFS(start_node,visited):
    if start_node not in nodes:
        print("node not present")
    queue=deque()
    queue.append(start_node)
    while queue:
        current=queue.popleft()
        print(current,end=" ")
        index=[nodes.index(current)]
        visited[index]=True
        for i in range(node_count):
            if graph[index][i]==1 and not visited[i]:
                queue.append(nodes[i])
                visited[i]=1
nodes=[]
graph=[]
node_count=0