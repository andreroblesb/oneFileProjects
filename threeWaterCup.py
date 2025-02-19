'''
En el problema de las tres jarras se plantea una situación en la que se tienen tres jarras o contenedores de capacidades A, B y C litros (números enteros) con A > B > C y A par. Inicialmente, la jarra mayor está llena y las otras dos vacías. 

El **objetivo** es repartir por igual el contenido inicial entre las dos jarras mayores transvasando correctamente el agua entre las jarras. 

Por ejemplo, para el problema A = 8, B = 5, y C = 3, inicialmente hay 8 litros en la jarra A, y el resto de las jarras están vacías. Luego, al final, las jarras A y B quedarían con 4 litros y la jarra C estaría vacía.

Para este problema:

El ejercicio es interpretar el ejercicio como un problema de búsqueda no informado, y determinar la secuencia de traspases de agua, que no tienen restricción de cantidad.

Se va a usar el algoritmo no informado DFS.

Repitamos las retricciones:

A > B > C
A % 2 == 0

heuristica que se me ocurre para solucionar el problema (aunque no lo vayamos a usar por querer utilizar un algoritmo desinformado):

Parte el agua de A hasta que quepa en B, rellena primero C y cuando se llene empiezas a llenar B, cuando el agua en A ya quepa en B mueves de C a B lo necesario
'''
import copy

class Node():
    def __init__(self, capacity, value):
        self.capacity : int = capacity
        self.value : int = value
    
    def __str__(self):
        return self.value

class State():
    def __init__(self, **kwargs):
        self.state : dict[str, Node] = kwargs
        self.path : list[Move] = []
        self.moves: list[Move] = []
        self.cost : int = 0
    
    def create_moves(self):
        self.moves.clear()
        for key1, node1 in self.state.items():
            for key2, node2 in self.state.items():
                if node1.value > 0 and node2.value < node2.capacity:
                    max_transfer = min(node1.value, node2.capacity - node2.value)
                    move = Move(key1, key2, max_transfer)
                    self.moves.append(move)
        return self.moves
    
    def __str__(self):
        return f"A: {self.state['A'].value}, B: {self.state['B'].value}, C: {self.state['C'].value}"

class DFS():
    def __init__(self):
        self.visited : set[(int, int, int)] = set()
    
    def copy_state(self, state):
        # return State(A=state.state["A"], B=state.state["B"], C=state.state["C"])
        return copy.deepcopy(state)
    
    def dfs(self, state, path):
        state_tuple = (state.state["A"].value, state.state["B"].value, state.state["C"].value)
        if state_tuple in self.visited:
            return False
        self.visited.add(state_tuple)

        if state.state["A"].value == state.state["B"].value:
            print("Solution found:", path)
            print("Final state:", state)
            print("Cost:", state.cost)
            return True

        moves = state.create_moves()
        for move in moves:
            new_state = self.copy_state(state)
            move.make_exchange(new_state)
            new_state.cost += 1
            if self.dfs(new_state, path + [move]):
                return True
        return False
    
    def __str__(self):
        return f"A: {self.state['A'].value}, B: {self.state['B'].value}, C: {self.state['C'].value}"


class Move():
    # to express a water transaction from node 1 to node 2
    def __init__(self, node1, node2, exchange):
        self.node1 : str = node1
        self.node2 : str = node2
        self.exchange : int = exchange
    
    def make_exchange(self, state):         
        state.state[self.node1].value -= self.exchange
        state.state[self.node2].value += self.exchange
        return 
    
    def __eq__(self, other):
        if isinstance(other, Move):
            return self.node1 == other.node1 and self.node2 == other.node2 and self.exchange == other.exchange
        return False
    
    def __str__(self):
        return f"from {self.node1} to {self.node2}: {self.exchange}"

    def __repr__(self):
        return self.__str__()


def main():
    initial_state = State(
        A= Node(8, 8),  
        B= Node(5, 0),
        C= Node(3, 0))
    
    search_entity = DFS()
    search_entity.dfs(initial_state, [])
    
if __name__ == "__main__":
    main()