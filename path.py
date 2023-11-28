import myqueue as myq

def dijkstras(graph, start_node):
    """
    A function implementing Dijkstras path algorithm. The myqueue module is a dependency.

    args:
        graph (Graph): A graph object from the graph module that represents the
        graph to be traversed

        start_node (Node): A Node object representing the start node of the traversal.
        the Node object may only contain a valid name in graph. All other attributes are
        not used
    returns:
        [distance, prev_node table] (list): returns a list  with its first element
        being a dictionary of distances from start_node. The keys are strings representing
        the node names, the values are the distances from the node (if the node cannot be
        reached from the start node the value is float('inf')). The second element is a dictionary
        whos keys are strings representing any node in graph and whos value is a string representing
        the previous node in the path to the start node. start_node and any node not reachable
        by start_node has None as it's value
    """
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
    """
    A function implementing a Bellam-Ford path algorithm

    args:
        graph (Graph): A graph object from the graph module that represents the
        graph to be traversed

        start_node (Node): A Node object representing the start node of the traversal.
        the Node object may only contain a valid name in graph. All other attributes are
        not used
    returns:
        [distance, prev_node table] (list): returns a list  with its first element
        being a dictionary of distances from start_node. The keys are strings representing
        the node names, the values are the distances from the node (if the node cannot be
        reached from the start node the value is float('inf')). The second element is a dictionary
        whos keys are strings representing any node in graph and whos value is a string representing
        the previous node in the path to the start node. start_node and any node not reachable
        by start_node has None as it's value
    """
    distance = {}
    prevnode_table = {}
    node_table = {}
    for node in graph:
        distance[node] = float("inf")
        if node == start_node:
            distance[node] = 0
        prevnode_table[node] = None
        node_table[node.name] = node
    for _ in range(len(graph) - 1):
        for node in graph:
            for edge in node.edges:
                if distance[edge.dest_node] > distance[edge.src_node] + edge.weight:
                    distance[edge.dest_node] = distance[edge.src_node] + edge.weight
                    prevnode_table[edge.dest_node] = edge.src_node
    return [distance, prevnode_table]