def add_node(v):
    global node_count
    
    if v in nodes:
        print("v,already present in the graph")
    else:
        node_count+=1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp=[]
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)
nodes=[]
graph=[]
node_count=0
print("before addimg nodes")
print(nodes)
add_node("A")
print("after insertion")
print(nodes)


