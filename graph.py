import path

def parse_weighted_graph(path: str):
    graph = Graph()
    try:
        with open(path) as file:
            lines = file.readlines()
        found_nodes = False
        found_edges = False
        node_count = 0
        edge_table = {}
        for line in lines:
            if line == "Nodes:\n":
                found_nodes = True
                continue
            if line == "Edges:\n":
                found_edges = True
                continue
            if found_edges == True and found_nodes == True:
                edge = line.split('; ')
                if edge[0] == "d":
                    edge = edge[1].split(", ")
                    graph.add_edge(Edge(edge[0], edge[1].split(": ")[0], int(edge[1].split(": ")[1].strip("\n"))))
                    #graph[edge_table[edge[0]]].append((edge[1].split(": ")[0], int(edge[1].split(": ")[1].strip("\n"))))
                if edge[0] == "ud":
                    edge = edge[1].split(", ")
                    graph.add_edge(Edge(edge[0], edge[1].split(": ")[0], int(edge[1].split(": ")[1].strip("\n"))))
                    graph.add_edge(Edge(edge[1].split(": ")[0], edge[0], int(edge[1].split(": ")[1].strip("\n"))))
                    #graph[edge_table[edge[0]]].append((edge[1].split(": ")[0], int(edge[1].split(": ")[1].strip("\n"))))
                    #graph[edge_table[edge[1].split(": ")[0]]].append((edge[0], int(edge[1].split(": ")[1].strip("\n"))))
                continue
            if found_nodes == True:
                node = line.strip("\n")
                if len(node) == 0:
                    continue
                graph.add_node(Node(node))
    except OSError:
        print("The graph file could not be found")
    return graph

class Graph():
    def __init__(self, nodes=[], edges=[], type="adjlist"):
        self._nodes = nodes
        self._edges = edges
        self._graph = self.make_graph(self._nodes, self._edges)
        self.type = type
        self._edge_table = {}
        self._count = 0
    
    def make_graph(self, nodes, edges):
        edge_table = {}
        graph = []
        node_count = 0
        for node in nodes:
            graph.append(node)
            edge_table[node] = node_count
            node_count += 1
        try:
            for edge in edges:
                graph[edge_table[edge.src_node]].new_weighted_edge(edge)
        except KeyError:
            print("The nodes in the edge must already be in the nodes list")
        return graph
    
    def get_graph(self):
        return self._graph

    def add_node(self, node):
        self._count += 1
        self._edge_table[node] = self._count - 1
        self._graph.append(node)
    
    def add_edge(self, edge):
        try:
            self._graph[self._edge_table[edge.src_node]].new_weighted_edge(edge)
        except KeyError:
            print("The nodes in the edge must already be in the nodes list")
        

class Node():
    def __init__(self, name):
        self.name = name
        self.edges = []
    
    def new_weighted_edge(self, weighted_edge):
        self.edges.append(weighted_edge)
    
    def __hash__(self):
        return hash((self.name))
    
    def __eq__(self, other):
        return self.__hash__() == other.__hash__()
    
    def __repr__(self):
        return self.name
    
    def __lt__(self, other):
        return self.__hash__() < other.__hash__()
        

class Edge():
    def __init__(self, src_node_name, dest_node_name, weight=1):
        self.src_node = src_node_name
        self.dest_node = dest_node_name
        self.weight = weight
    
    def __repr__(self):
        return "(" + str(self.src_node) + ", " + str(self.dest_node) + ", " + str(self.weight) + ")"
    
    def __str__(self):
        return "(" + str(self.src_node) + ", " + str(self.dest_node) + ", " + str(self.weight) + ")"