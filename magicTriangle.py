"""
magic triangle problem. We have the triangle below and must fill the nodes with the numbers 1 to 6, in ascendent order, so that the vertices sum 10. Search entity must move along the graph asigning the numbers.

We will use the two most popular uninformed search algorithm (BFS & DFS).

We are assuming:
- We can go back from node to node
- We can reasign the number of a node
- Numbers are put in ascending order
- ALL NODES ARE CONNECTED (implicitly)

"""
# problem graph given is:
r'''
      A
     /|\
    / | \
   B _|_ C
  / \ | / \
 /   \|/   \
D-----E-----F
'''
# is it overengineered? yes, because the understanding of the assignment changed during the development of the solution. Graph does not apply in the traditional sense.

# BFS search entity
class BFS():
    def __init__(self, start, graph):
        self.numbers : list[int] = [x for x in range(1, 7)]
        self.stack : list[str] = []
        self.graph : Graph = graph
        self.done : bool = False
        self.current : str = None
    
    def solve(self):
        

class DFS():
    def __init__(self, graph):
        self.numbers : list[int] = [x for x in range(1, 7)]
        self.stack : list[str] = []
        self.graph : Graph = graph
        self.done : bool = False
        self.current : str = None
    
    # use FIFO principle (stack)
    
    def solve(self):
        print("Initiating DFS search")
        # add moves to stack
        options : list = self.graph.return_unassigned()
        for node in options:
            self.stack.append(node)
        while not self.done:
            # check if done
            if len(self.numbers) == 0:
                if self.graph.constraint_proof():
                    self.done = True
                    print("Done!")
                    continue
                else:
                    print("Configuration does not pass constraint.")
                    self.numbers.append(self.graph.nodes[self.current])
                    self.graph.nodes[self.current] = 0
            
            # assign last-in
            number = self.numbers.pop()
            self.current = self.stack.pop()
            self.graph.nodes[self.current] = number
            print(f"Assigned {number} to {self.current}")
            
            # add moves to stack
            options : list = self.graph.return_unassigned()
            for node in options:
                self.stack.append(node)

class Graph():
    def __init__(self, **kwargs : int):
        self.nodes : dict[str, int] = kwargs
    
    def constraint_proof(self):
        # proof if we are done
        if sum([self.nodes["A"], self.nodes["D"], self.nodes["F"]]) == 10:
            return True
        else: return False
    
    def return_unassigned(self):
        assigned = []
        for node, value in self.nodes.items():
            if value == 0:
                assigned.append(node)
        return assigned

    def __str__(self):
        printing = ""
        for node, value in self.nodes.items():
            printing += f"{node} : {value} \n"
        return printing

# setting the problem graph
graph = Graph(A=0, B=0, C=0, D=0, E=0, F=0)

# perform BFS
search_entity = DFS(graph)
search_entity.solve()
print(graph)
