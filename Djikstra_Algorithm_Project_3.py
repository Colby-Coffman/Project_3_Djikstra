class Node:
    def __init__(self, name, buildingname, lowestweight = float("inf")):
        self.name = name
        self.lowestweight = lowestweight
        self.buildingname = buildingname
#Node class was created to store key values to make coding implementation easier, and building name is for the final result
class Edge:
    def __init__(self, node1, node2, weight, setweight = float("inf")):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight
        self.setweight = setweight
#Edges are just objects between 2 edges. It stores an inherent weight, and has a setweight equal to everything before it plus itself.
node_A = Node("A", "College Square")
node_B = Node("B", "Speech Language Center")
node_C = Node("C", "Lewis Science Center")
node_D = Node("D", "Prince Center")
node_E = Node("E", "Computer Science")
node_F = Node("F", "Burdick")
node_G = Node("G", "Torreyson Library")
node_H = Node("H", "Maintenace College")
node_I = Node("I", "Old Main")
node_J = Node("J", "Police Dept")
node_K = Node("K", "Fine Art")
node_L = Node("L", "McAlister Hall")
node_M = Node("M", "Student Center")
node_N = Node("N", "Student Health Center")
node_O = Node("O", "Wingo")
node_P = Node("P", "New Business Building")
node_Q = Node("Q", "Oak Tree Apt")
node_R = Node("R", "Brewer-Hedgeman")
node_S = Node("S", "Bear Village Apt.")

edge_CA = Edge(node_A, node_C, 200)
edge_BH = Edge(node_B, node_H, 120)
edge_CB = Edge(node_C, node_B, 250)
edge_DA = Edge(node_D, node_A, 300)
edge_DJ = Edge(node_D, node_J, 100)
edge_EC = Edge(node_E, node_C, 150)
edge_ED = Edge(node_E, node_D, 80)
edge_EG = Edge(node_E, node_G, 40)
edge_EF = Edge(node_E, node_F, 30)
edge_FG = Edge(node_F, node_G, 80)
edge_FB = Edge(node_F, node_B, 100)
edge_FL = Edge(node_F, node_L, 200)
edge_FH = Edge(node_F, node_H, 300)
edge_GD = Edge(node_G, node_D, 30)
edge_GI = Edge(node_G, node_I, 30)
edge_HQ = Edge(node_H, node_Q, 160)
edge_IJ = Edge(node_I, node_J, 200)
edge_IK = Edge(node_I, node_K, 90)
edge_IL = Edge(node_I, node_L, 100)
edge_JN = Edge(node_J, node_N, 100)
edge_KJ = Edge(node_K, node_J, 50)
edge_KM = Edge(node_K, node_M, 80)
edge_KL = Edge(node_K, node_L, 180)
edge_LH = Edge(node_L, node_H, 150)
edge_LM = Edge(node_L, node_M, 100)
edge_LO = Edge(node_L, node_O, 50)
edge_MN = Edge(node_M, node_N, 50)
edge_MP = Edge(node_M, node_P, 110)
edge_MO = Edge(node_M, node_O, 100)
edge_NR = Edge(node_N, node_R, 200)
edge_OH = Edge(node_O, node_H, 100)
edge_OP = Edge(node_O, node_P, 50)
edge_PH = Edge(node_P, node_H, 150)
edge_PQ = Edge(node_P, node_Q, 30)
edge_PR = Edge(node_P, node_R, 20)
edge_RQ = Edge(node_R, node_Q, 40)
edge_RS = Edge(node_R, node_S, 350)
#Above is original directed graph, and below was to make it undirected and a basic weighted graph.
edge_AC = Edge(node_C, node_A, 200)
edge_HB = Edge(node_H, node_B, 120)
edge_BC = Edge(node_B, node_C, 250)
edge_AD = Edge(node_A, node_D, 300)
edge_JD = Edge(node_J, node_D, 100)
edge_CE = Edge(node_C, node_E, 150)
edge_DE = Edge(node_D, node_E, 80)
edge_GE = Edge(node_G, node_E, 40)
edge_FE = Edge(node_F, node_E, 30)
edge_GF = Edge(node_G, node_F, 80)
edge_BF = Edge(node_B, node_F, 100)
edge_LF = Edge(node_L, node_F, 200)
edge_HF = Edge(node_H, node_F, 300)
edge_DG = Edge(node_D, node_G, 30)
edge_IG = Edge(node_I, node_G, 30)
edge_QH = Edge(node_Q, node_H, 160)
edge_JI = Edge(node_J, node_I, 200)
edge_KI = Edge(node_K, node_I, 90)
edge_LI = Edge(node_L, node_I, 100)
edge_NJ = Edge(node_N, node_J, 100)
edge_JK = Edge(node_J, node_K, 50)
edge_MK = Edge(node_M, node_K, 80)
edge_LK = Edge(node_L, node_K, 180)
edge_HL = Edge(node_H, node_L, 150)
edge_ML = Edge(node_M, node_L, 100)
edge_OL = Edge(node_O, node_L, 50)
edge_NM = Edge(node_N, node_M, 50)
edge_PM = Edge(node_P, node_M, 110)
edge_OM = Edge(node_O, node_M, 100)
edge_RN = Edge(node_R, node_N, 200)
edge_HO = Edge(node_H, node_O, 100)
edge_PO = Edge(node_P, node_O, 50)
edge_HP = Edge(node_H, node_P, 150)
edge_QP = Edge(node_Q, node_P, 30)
edge_RP = Edge(node_R, node_P, 20)
edge_QR = Edge(node_Q, node_R, 40)
edge_SR = Edge(node_S, node_R, 350)

#Undirected graph edges are essentially just the original directed graph, but point back at themselves

class NodeEdges:
    def __init__(self, node, edge1=None, edge2=None, edge3=None, edge4=None, edge5=None, edge6=None):
        self.node = node
        self.edge1 = edge1
        self.edge2 = edge2
        self.edge3 = edge3
        self.edge4 = edge4
        self.edge5 = edge5
        self.edge6 = edge6

#This NodeEdges class was created to easily communicate between nodes and edges. It also stores a maximum of 6 edges as that is the amount of edges an undirected graph would have. For a 
#directed graph, I found there to only be a required 4 edges maximum

A = NodeEdges(node_A, edge_AC, edge_AD)
B = NodeEdges(node_B, edge_BH, edge_BC, edge_BF)
C = NodeEdges(node_C, edge_CB, edge_CE, edge_CA)
D = NodeEdges(node_D, edge_DA, edge_DJ, edge_DE, edge_DG)
E = NodeEdges(node_E, edge_EF, edge_EC, edge_ED, edge_EG)
F = NodeEdges(node_F, edge_FG, edge_FL, edge_FB, edge_FH, edge_FE)
G = NodeEdges(node_G, edge_GD, edge_GI, edge_GE, edge_GF)
H = NodeEdges(node_H, edge_HQ, edge_HB, edge_HF, edge_HL, edge_HO, edge_HP)
I = NodeEdges(node_I, edge_IJ, edge_IK, edge_IL, edge_IG)
J = NodeEdges(node_J, edge_JN, edge_JD, edge_JI, edge_JK)
K = NodeEdges(node_K, edge_KJ, edge_KM, edge_KL, edge_KI)
L = NodeEdges(node_L, edge_LH, edge_LO, edge_LM, edge_LI, edge_LK, edge_LF)
M = NodeEdges(node_M, edge_MO, edge_MP, edge_MN, edge_MK, edge_ML)
N = NodeEdges(node_N, edge_NR, edge_NJ, edge_NM)
O = NodeEdges(node_O, edge_OH, edge_OP, edge_OM, edge_OL)
P = NodeEdges(node_P, edge_PQ, edge_PR, edge_PH, edge_PO, edge_PM)
Q = NodeEdges(node_Q, edge_QH, edge_QP, edge_QR)
R = NodeEdges(node_R, edge_RQ, edge_RS, edge_RP, edge_RN) 
S = NodeEdges(node_S, edge_SR)

#lists - self explanatory - visted is for implementation of undirected graph djikstra, but wasn't required for this project
queue = []
visited = []
path = []

def findEdge(nodeEdge, endingEdge):
    lightest = float("inf")
    node = nodeEdge.node.name
    edge1 = nodeEdge.edge1
    edge2 = nodeEdge.edge2
    edge3 = nodeEdge.edge3
    edge4 = nodeEdge.edge4
    edge5 = nodeEdge.edge5
    edge6 = nodeEdge.edge6
    edges = [edge1,edge2,edge3,edge4,edge5,edge6]
    for i in edges:
        if i not in queue:
            if i != None:
                if i.weight + i.node1.lowestweight < i.node2.lowestweight:
                    i.node2.lowestweight = i.weight + i.node1.lowestweight
                if i.node2.name not in visited:
                    queue.append(i)
    
#Above is in charge of adding edges to a queue. It just uses the current node and adds every edge to the queue

    if node not in visited:
        visited.append(node)

#this function stores everything about the visited nodes, which allows for it to be an undirected graph.

#Since we are only going from the computer science building, this is allowed to be a directed graph. However, it was implemented as an undirected graph...

    for x in queue:
        x.setweight = x.weight+x.node1.lowestweight

#Above is making the setweight of a edge equal to the lowestweight of the previous node and the weight of itself

    #little bubble sorter to get the lowest weight edges + total previous weight to the front of the list. It uses the setweight we got a few lines back
    if len(queue)>1:
        for x in range(0,len(queue)-1):
            for i in range(0,len(queue)-1):
                if queue[i].setweight > queue[i+1].setweight:
                    queue[i], queue[i+1] = queue[i+1], queue[i] 

    nextnode = queue[0].node2.name
    print("Current Node:", queue[0].node1.name)
    print("Next Node:", nextnode)
    print("Current Weight:", queue[0].setweight)
    #This is just a function to track each individual spot. You can comment out any of these print statements to diagnose how the program is working through.

    #Below just adds to the path the algorithm has taken. it is not the finalized path yet though
    path.append(queue[0])

#    for i in range(0,len(path)-1):
#        print(path[i].node1.name,path[i].node2.name)

#This above is also a diagnostic test to make sure the sort was working correctly

#this just pops the first item in queue. pretty self explanatory as to why we would want that
    queue.pop(0)
    
    if nextnode == endingEdge:
        for i in range(len(path)-1,0,-1):
            if path[i-1].node2 != path[i].node1:
                path.pop(i-1)
            else:
                for x in range(0, len(path)-1):
                    if path[x].node2 == path[i].node1:
                        path[i-1].node1 = path[x].node1
                        break
                    else:
                        pass

#Above was the most important part. Once we find our final path, it goes through the total path taken. It will start at the last node, and have the previous node be set to the current node.
#After this, it will recursively pop the last item in the path(besides itself) until the node before it connects to itself. Once this happens, it will go through starting at the beginning
#of the list until it reaches the same node, and assign it to be the final path. It will continue doing this for the entirety of the path list, until it comes out with the finalized
#route.

        print("\nPATH FOUND")
        print("\nThe total shortest distance from",path[0].node1.buildingname,"to", path[len(path)-1].node2.buildingname,"is",path[len(path)-1].setweight)
        print("\nThe path is:")

        #I could've made it to where it would just say where it was once by only having the node2 building name, but I feel it adds clarity to reiterate the previous and next building.
        for i in path:
            print(i.node1.buildingname,"to",i.node2.buildingname)
        print("\n")
        return 0

    if nextnode == "A":
        findEdge(A, endingEdge)
    if nextnode == "B":
        findEdge(B, endingEdge)
    if nextnode == "C":
        findEdge(C, endingEdge)
    if nextnode == "D":
        findEdge(D, endingEdge)
    if nextnode == "E":
        findEdge(E, endingEdge)
    if nextnode == "F":
        findEdge(F, endingEdge)
    if nextnode == "G":
        findEdge(G, endingEdge)
    if nextnode == "H":
        findEdge(H, endingEdge)
    if nextnode == "I":
        findEdge(I, endingEdge)
    if nextnode == "J":
        findEdge(J, endingEdge)
    if nextnode == "K":
        findEdge(K, endingEdge)
    if nextnode == "L":
        findEdge(L, endingEdge)
    if nextnode == "M":
        findEdge(M, endingEdge)
    if nextnode == "N":
        findEdge(N, endingEdge)
    if nextnode == "O":
        findEdge(O, endingEdge)
    if nextnode == "P":
        findEdge(P, endingEdge)
    if nextnode == "Q":
        findEdge(Q, endingEdge)
    if nextnode == "R":
        findEdge(R, endingEdge)
    if nextnode == "S":
        findEdge(S, endingEdge)

#Above uses the nextnode variable we get from the queue and iterates through until we reach the target.

def main():
    startingNode = E

#Made a variable above to test different starting positions. pre-set to E because that is the computer science building

    startingNode.node.lowestweight = 0
    while True:
        print("\nKey:\n")
        print("A :: College Square")
        print("C :: Lewis Science Center")
        print("D :: Prince Center")
        print("E :: Computer Science")
        print("F :: Burdick")
        print("G :: Torreyson Library")
        print("H :: Maintenace College")
        print("I :: Old Main")
        print("J :: Police Dept")
        print("K :: Fine Art")
        print("L :: McAlister Hall")
        print("M :: Student Center")
        print("N :: Student Health Center")
        print("O :: Wingo")
        print("P :: New Business Building")
        print("Q :: Oak Tree Apt")
        print("R :: Brewer-Hedgeman")
        print("S :: Bear Village Apt.")
        endingEdge = input('Enter key letter here: ')

        if 'A' <= endingEdge <= 'S':
            if startingNode.node.name != endingEdge:
                        findEdge(startingNode,endingEdge)
            else:
                print("You are already at",startingNode.node.buildingname,"so the distance is 0.")
            break
        else:
            print("\nEnter valid key letter.")
            pass
    #The main function is just responsible for receiving input, making sure its valid, then running through the findEdge function recursively until we get our desired answer
main()

#Overall, I think the implementation of objects was the best thing about this project. I do think I could've been a lot more efficient with assigning of different things and
#utilizing language features more. I also could've delegated some more functionality to more functions, but I was able to make due with just the main and findEdge function. For a larger
#graph, I think efficiency should be more at the forefront, but since we are dealing with such a small set of data, I was able to get away with a lot of inefficient but easy to implement
#stuff, such as the bubble sort for the queue. For large datasets, there could've been more efficient ways of doing things, such as using an n(logn) sorter for queue. It was made into an
#undirected graph, so you can change the location of the starting position within the code. However, for the purposes of this project, we only needed to find it from the computer science
#building, so that's what it is from now (node E). If you would like to test it out, just change the startingNode variable