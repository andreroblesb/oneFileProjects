"""
magic triangle problem. We have the triangle below and must fill the nodes with the numbers 1 to 6, in ascendent order, so that the vertices sum 10. Search entity must move along the graph asigning the numbers.

We will use the two most popular uninformed search algorithm (BFS & DFS).

"""
# problem graph is:
r'''
      A
     / \
    /   \
   B     C
  /       \
 /         \
D-----E-----F
'''
# is it overengineered? yes, do we care? no, if it's for the sake of learning

# BFS search entity
class BFS():
    def __init__(self, start, graph):
        self.numbers : list[int] = [x for x in range(7, 1)]
        self.visited : set[Node] = ()
        self.state : Node = start
        self.graph : Graph = graph
    
    def state_proof(self):
        # proof if we are done
        if sum(self.graph.nodes["A"].value and self.graph.nodes["D"].value and self.graph.nodes["F"].value) == 10:
            print("done")
            

class Node():
    def __init__(self, name, edge):
        self.value : int = None
        self.name : str = name
        self.connections : list[Node] = []
        self.edge : bool = edge

class Graph():
    """
    create an adjacency matrix
    """
    
    def __init__(self, **kwargs : Node):
        self.nodes : dict[str, Node] = kwargs
        self.edges : list[tuple[str]] = []
    
    def edge(self, edge):
        self.edges.append(edge)
        return
        

# setting the problem graph
start = Node("A", True)
graph = Graph(A=start, B=Node("B", False), C=Node("C", False), D=Node("D", True), E=Node("E", False), F=Node("F", True))
graph.edge(("A", "B"))
graph.edge(("B", "D"))
graph.edge(("D", "E"))
graph.edge(("E", "F"))
graph.edge(("F", "C"))
graph.edge(("C", "A"))

# perform BFS
