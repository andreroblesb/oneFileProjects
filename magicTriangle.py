"""
magic triangle problem. We have the triangle below and must fill the nodes with the numbers 1 to 6, in ascendent order, so that the vertices sum 10. Search entity must therefore not move along the explicit graph, but search on the space of available nodes.

We are assuming:
- All nodes should have assigned a number from 1 to 6 in order to the result to be valid.
- ALL NODES ARE CONNECTED (implicitly)

We will use the two most popular uninformed search algorithm (BFS & DFS).
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

class Queue():
    def __init__(self, id):
        self.numbers : list[int] = [x for x in range(1, 7)]
        self.queue : list[str] = []
        self.graph : Graph = Graph(A=0, B=0, C=0, D=0, E=0, F=0)
        self.current : str = None
        self.id : str = id
    
    def update(self):
        # add moves to queue
        options : list = self.graph.return_unassigned()
        for node in options:
            self.queue.append(node)
    
    def check(self):
        # check if done
        if len(self.numbers) == 0:
            if self.graph.constraint_proof():
                return True, self.graph
            else:
                print("Configuration does not pass constraint.")
                self.numbers.append(self.graph.nodes[self.current])
                self.graph.nodes[self.current] = 0
        return None, None 
             
    def move(self):          
        # assign first-in
        number = self.numbers.pop()
        self.current = self.queue.pop(0)
        if self.graph.nodes[self.current] != 0:
            self.numbers.append(self.graph.nodes[self.current])
        self.graph.nodes[self.current] = number
        print(f"Assigned {number} to {self.current}")

# BFS search entity
class BFS():
    def __init__(self, queues):
        self.queues : list[Queue] = queues
        self.done : bool = False
        self.current : Queue = None
    
    def solve(self):
        print("Starting BFS search")
        # add moves to queue
        while not self.done:
            for branch in self.queues:
                branch.update()
                flag, graph = branch.check()
                if flag:
                    print("\n First succesfully completed queue found!")
                    print(graph)
                    self.done = True
                    break
                branch.move()

class DFS():
    def __init__(self, graph):
        self.numbers : list[int] = [x for x in range(1, 7)]
        self.stack : list[str] = []
        self.graph : Graph = graph
        self.done : bool = False
        self.current : str = None
    
    # use LIFO principle (stack)
    
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
                    print(self.graph)
                    continue
                else:
                    self.numbers.append(self.graph.nodes[self.current])
                    self.graph.nodes[self.current] = 0
                    print(f"Constraint not met")
                    continue
            
            # assign last-in
            self.current = self.stack.pop()
            number = self.numbers.pop()
            if self.graph.nodes[self.current] != 0:
                self.numbers.append(self.graph.nodes[self.current])
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

def main():
    # setting the problem graph
    graph = Graph(A=0, B=0, C=0, D=0, E=0, F=0)

    # perform DFS
    search_entity = DFS(graph)
    search_entity.solve()

    # perform  BFS
    queues = [
        Queue(id="1"), 
        Queue(id="2"), 
        Queue(id="3"), 
        Queue(id="4"), 
        Queue(id="5"), 
        Queue(id="6")
    ]
    search_entity = BFS(queues)
    search_entity.solve()

if __name__ == "__main__":
    main()
