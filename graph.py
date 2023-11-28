import path

def parse_weighted_graph(path: str):
    """
    A function to parse a graph file to a Graph object

    args:
        path (str): A path to the graph file.
    returns:
        graph (Graph): A graph object created from the grath file pointed to by path
    """
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
                if edge[0] == "ud":
                    edge = edge[1].split(", ")
                    graph.add_edge(Edge(edge[0], edge[1].split(": ")[0], int(edge[1].split(": ")[1].strip("\n"))))
                    graph.add_edge(Edge(edge[1].split(": ")[0], edge[0], int(edge[1].split(": ")[1].strip("\n"))))
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
    """
    An object representing a directed graph with an adjacency list representation
    """
    def __init__(self, nodes=[], edges=[]):
        """
        Constructs a Graph object

        args:
            nodes (list): A keyword argument to pass nodes in the graph on construction.
            All node names must be unique. The elements must be Node objects
            edges (list): A keyword argument to pass edges in the graph on construction.
            All the nodes of the edges must be in the nodes list. The elements must be Edge
            objects.
        """
        self._nodes = nodes # private
        self._edges = edges # private
        self._graph = self._make_graph(self._nodes, self._edges) # private
        self._edge_table = {} # private
        self._count = 0 # private
    
    def _make_graph(self, nodes, edges):
        """
        Private function to generate a Graph object.
        """
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
        """
        Getter function for the graph object list representation

        returns:
            _graph (list): A list representing the Graph object where each element 
            is the nodes of the Graph.
        """
        return self._graph

    def add_node(self, node):
        """
        A function to add a node to the Graph

        args:
            node (Node): A Node object to be added to the graph
        """
        self._count += 1
        self._edge_table[node] = self._count - 1
        self._graph.append(node)
    
    def add_edge(self, edge):
        """
        A function to add an edge to a node in the graph. The nodes of the edge must
        already be in the graph.

        args:
            edge (Edge): An Edge object to be added to the graph.
        """
        try:
            self._graph[self._edge_table[edge.src_node]].new_weighted_edge(edge)
        except KeyError:
            print("The nodes in the edge must already be in the nodes list")
        

class Node():
    """
    A class representing the nodes of a Graph
    
    attributes:
        name (str): The name of the node
        edges (list): A list of tuples containing the edges the node has. Each element is
        an Edge object.
    """
    def __init__(self, name):
        """
        A constructor for the Node

        args:
            name (str): The name of the node
        """
        self.name = name
        self.edges = []
    
    def new_weighted_edge(self, weighted_edge):
        """
        Adds a weighted edge to the node

        args:
            weighted_edge (Edge): The weighted edge to be added
        """
        self.edges.append(weighted_edge)
    
    def __hash__(self):
        """
        The hashing function for the object is the hash of the Node's name
        """
        return hash((self.name))
    
    def __eq__(self, other):
        """
        Two nodes are equal if they share the same name
        """
        return self.__hash__() == other.__hash__()
    
    def __repr__(self):
        return self.name
    
    def __lt__(self, other):
        """
        Nodes are sorted based off alphabetical order
        """
        return self.__hash__() < other.__hash__()
        

class Edge():
    """
    A class representing the directed edges of a node

    attributes:
        src_node (str): The name of the starting node
        dest_node (str): The name of the destination node
        weight (int): The weight of an edge
    """
    def __init__(self, src_node_name, dest_node_name, weight=1):
        """
        Constructs an Edge object

        args:
            src_node_name (str): The name of the starting node
            dest_node_name (str): The name of the ending node
            weight=1 (int): Keyword argument for the weight of the edge
        """
        self.src_node = src_node_name
        self.dest_node = dest_node_name
        self.weight = weight
    
    def __repr__(self):
        return "(" + str(self.src_node) + ", " + str(self.dest_node) + ", " + str(self.weight) + ")"
    
    def __str__(self):
        return "(" + str(self.src_node) + ", " + str(self.dest_node) + ", " + str(self.weight) + ")"