"""
In this problem we try to find a solution to the eight queen problem, were we are required to put eight queens in a chess board without making each other attack itself.

A state in this sense is a board with an nth queen, in a position that may or may not be valid. In this sense, we can imagine it being computationally expensive to think about all the possible scenarios, were technically without restrictions we are searching in a space of: 64x63x62x61x60x59x58x57. Therefore an efficient algorithm is extremely necessary.

The cost function represents the amount of restrictions met (two queens attacking each other).

Lastly, we will generate states by representing them with a single list of size n, by index, which relates to the queen and its "column", and a number which represents the "row" where the queen is located.

[1, 2, 3]
- index: column (0-indexed)
- integer: row (0-indexed)

Given this, we will implement the following local search algorithms:
- Random search
- Greedy search
- Simulated annealing search

Which do not operate in the traditional sense of searching by the next state (like putting one queen at a time), but instead at complete states. We can imagine this search over a function, trying to find the maximum or minimum. A last annotation is that these algorithm implementations by nature DO NOT guarantee the absolute minimum (allocating all queens correctly), but it a matter of exploration vs exploitation. They just try to IMPROVE the current state. Another thing to notice is that they are iterative strategies, not recursive.

"""
import random 
import numpy as np
import matplotlib.pyplot as plt

def state(n):
    return random.choices([x for x in range(n)], k=n)

def cost(state, n):
    cost = 0
    # calculate restrictions met by rows (do not count redundant row restrictions)
    row_cost = len(state) - len(set(state))
    # print("Row cost", row_cost)
    cost += row_cost
    for i, row in enumerate(state, start=0):
        # solo verifica las diagonales de cada reina hacia la derecha
        change = 1
        for column in range(i, n-1):
            if state[column+1] in (row+change, row-change):
                cost += 1
            change += 1
    return cost

def random_local_search(n, iterations):
    stored_costs = []
    best_cost = float('inf')
    for _ in range(iterations):
        current_state = state(n)
        current_cost = cost(current_state, n)
        stored_costs.append(current_cost)
        # print(current_cost, current_state)
        if current_cost < best_cost:
            best_cost = current_cost
            best_state = current_state
    print("Done! Best found for random search: cost ->", best_cost, " with state ->", best_state)
    return stored_costs
    
def greedy_local_search(n, iterations):
    stored_costs = []
    best_cost = float('inf')
    best_state = state(n)
    for _ in range(iterations):
        costs_queue = []
        states_queue = []
        for i in range(len(best_state)):
            if best_state[i] > 0:
                substate_low = best_state.copy()
                substate_low[i] -= 1    
                substate_low_cost = cost(substate_low, n)
                
                costs_queue.append(substate_low_cost)  
                states_queue.append(substate_low)             

            if best_state[i] < (n-1):
                substate_high = best_state.copy()
                substate_high[i] += 1
                substate_high_cost = cost(substate_high, n)
                
                costs_queue.append(substate_high_cost)  
                states_queue.append(substate_high)
        
        index = costs_queue.index(min(costs_queue))
        iteration_cost = costs_queue[index]
        stored_costs.append(iteration_cost)
        if iteration_cost < best_cost:
            best_cost = iteration_cost
            best_state= states_queue[index]         
                    
    print("Done! Best found for greedy search: cost ->", best_cost, " with state ->", best_state)
    return stored_costs

def simulated_annealing(n, iterations, temperature, cooling):
    best_cost = float('inf')
    best_state = state(n)
    stored_costs = []
    
    current_state = best_state
    current_cost = cost(current_state, n)
    
    for _ in range(iterations):
        random_index = random.randint(0, n-1)
        random_choice = random.choice([-1, 1])
        if current_state[random_index] + random_choice < 0 or current_state[random_index] + random_choice >= n:
            continue
        new_state = current_state.copy()
        new_state[random_index] += random_choice
        
        new_cost = cost(new_state, n)
        acceptance = np.exp((current_cost - new_cost) / temperature)


        if random.uniform(0, 1) <= acceptance:
            current_cost = new_cost
            current_state = new_state
            stored_costs.append(current_cost)
            
            if current_cost < best_cost:
                best_cost = current_cost
                best_state = current_state.copy()
        
        temperature *= cooling        
                
    print("Done! Best found for simulated annealing search: cost ->", best_cost, " with state ->", best_state)
    return stored_costs
    
def plotting(random_results, greedy_results, annealing_results, n):
    iterations = [x for x in range(n)]
    annealing_iterations = [x for x in range(len(annealing_results))]
    plt.figure(figsize=(10, 6))
    plt.plot(iterations, random_results, 'r-', label='Random Search')
    plt.plot(iterations, greedy_results, 'g-', label='Greedy Search')
    plt.plot(annealing_iterations, annealing_results, 'b-', label='Simulated Annealing')
    
    plt.legend()
    plt.xlabel('Iterations')
    plt.ylabel('Cost')
    plt.title('Comparison of Local Search Methods')
    plt.grid(True)
    plt.show()

def main():
    queens = 8
    iterations = 1000
    temperature = 10
    cooling = 0.99
    random_costs = random_local_search(n=queens, iterations=iterations)
    greedy_costs = greedy_local_search(n=queens, iterations=iterations)
    annealing_costs = simulated_annealing(queens, iterations, temperature, cooling)
    plotting(random_costs, greedy_costs, annealing_costs, iterations)
    return

if __name__ == "__main__":
    main()