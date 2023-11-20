import myqueue as myq

def dijkstras(graph, start_node):
    distance = {}
    prevnode_table = {}
    node_table = {}
    heap = myq.PriorityQueue()
    for node in graph:
        distance[node] = float("inf")
        if node == start_node:
            distance[node] = 0
        prevnode_table[node] = None
        node_table[node.name] = node
        heap.add_item(node, distance[node])
    while True:
        node = heap.pop()
        if node == None:
            break
        for edge in node.edges:
            if distance[edge.dest_node] > distance[edge.src_node] + edge.weight:
                dist = distance[edge.src_node] + edge.weight
                distance[edge.dest_node] = dist
                prevnode_table[edge.dest_node] = edge.src_node
                heap.add_item(node_table[edge.dest_node], dist)
    return [distance, prevnode_table]

def bellam_ford(graph, start_node):
    distance = {}
    prevnode_table = {}
    node_table = {}
    for node in graph:
        distance[node] = float("inf")
        if node == start_node:
            distance[node] = 0
        prevnode_table[node] = None
        node_table[node.name] = node
    for _ in range(len(graph)):
        for node in graph:
            for edge in node.edges:
                if distance[edge.dest_node] > distance[edge.src_node] + edge.weight:
                    distance[edge.dest_node] = distance[edge.src_node] + edge.weight
                    prevnode_table[edge.dest_node] = edge.src_node
    return [distance, prevnode_table]