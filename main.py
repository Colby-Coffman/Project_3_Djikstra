import graph as gr
import time
import path as pth

if __name__ == "__main__":
    while True:
        graph = gr.parse_weighted_graph("graph.txt").get_graph()
        node_name_table = {}
        for node in graph:
            node_name_table[node.name.upper()] = node
        print("Locations on campus: ")
        for node in graph:
            print("\t", node)
        try:
            start_node = node_name_table[input("\n" + "Choose a start location: ").upper()]
        except KeyError:
            print("Start location not on campus\n")
            continue
        # if str(start_node).upper() not in map(lambda x: str(x).upper(), graph):
        #     print("Start location not on campus\n")
        #     continue
        try:
            end_node = node_name_table[input("Choose a end location: ").upper()]
        except KeyError:
            print("End location not on campus")
            continue
        # if str(end_node).upper() not in map(lambda x: str(x).upper(), graph):
        #     print("End location not on campus")
        #     continue
        print("\nPath algorithms available:\nDijkstras\nBellam-Ford")
        path_algorithm = input("Choose a path algorithm: ").upper()
        path_info = None
        elapsetime = None
        if path_algorithm == "DIJKSTRAS":
            start = time.time()
            path_info = pth.dijkstras(graph, start_node)
            elapsetime = time.time() - start
        elif path_algorithm == "BELLAM-FORD":
            start = time.time()
            path_info = pth.bellam_ford(graph, start_node)
            elapsetime = time.time() - start
        else:
            print(path_algorithm + " not available")
            continue
        path_exists = True
        if path_info[0][end_node] == float("inf"):
            print("It is not possible to get from", start_node, "to", end_node)
            path_exists = False
        if path_exists:
            print("\nPath found in", elapsetime, "seconds")
            print("Distance from", start_node, "to", end_node, ":", path_info[0][end_node])
            reconstruct = input("Reconstruct path? [Y/N]: ").upper()
        if reconstruct == "Y" and path_exists:
            reconstructed_path = []
            reconstructed_path.append(str(end_node))
            node = path_info[1][end_node]
            while True:
                if (node == start_node):
                    reconstructed_path.append(node)
                    break
                reconstructed_path.append(node)
                node = path_info[1][node]
            reconstructed_path.reverse()
            print("\nReconstructed path: ")
            for path in reconstructed_path:
                print(path)
        repeat = input("\nFind another path? [Y/N]: ").upper()
        if repeat == "Y":
            continue
        else:
            break