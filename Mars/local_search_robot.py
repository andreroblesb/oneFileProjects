"""
We will approach the mars robot local search for the deepest point of a crater. We are provided a two-dimensional map, in wich each position has 1 channel which represents the height. Robot in position (x, y) can only move to the 8 pixels around it, and choose, for the purpose of this case scenario, the lowest point. With this we attempt to go down the crater.

The constraint to meet is:
- A movement between a pixel and another cannot have a difference of more than two meters.

The data matrix represents an image, so to locate a point is not trivial (x, y) coordinate.
The point (0, 0) in the cartesian plane would represent the first point in the matrix (0, max-y)

Therefore we apply the following transformation for a coordinate (x, y) to the matrix (r, c):
r = n_r - round(y / scale)
c = round(x / scale)

Scale is indicated to be 10.045

"""

import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gsp
import time


# Extract data

input_file = "mars_crater_map.npy"
data = np.load(input_file)

nr, nc = data.shape
print(f"nr: {nr}, nc:{nc}")

def convert_to_r_c(point, scale=10.045):
    return (round(point[1] / scale), round(point[0] / scale))

def convert_to_x_y(point, scale=10.045):
    return (round(point[1]*scale), round(point[0]*scale)) 

def euclidian_distance(point1, point2):
    return np.sqrt((point1[0]-point2[0])**2 + (point1[1] - point2[1])**2)

def plot(start, finish_greedy, finish_annealing, greedy_costs, annealing_costs):
    fig = plt.figure(figsize=(10, 6))
    gs = gsp.GridSpec(2, 2, width_ratios=[2, 1])  

    ax1 = fig.add_subplot(gs[:, 0])  
    extension = [0, data.shape[1] * 10.045, 0, data.shape[0] * 10.045] 
    im = ax1.imshow(data, cmap="magma", origin="lower", extent=extension)
    ax1.set_title("Crater map")
    
    # la hanzel y gretel
    ax1.scatter(start[0], start[1], color="red", s=4)
    ax1.scatter(finish_greedy[0], finish_greedy[1], color="blue", s=4)
    ax1.scatter(finish_annealing[0], finish_annealing[1], color="green", s=4)
    fig.colorbar(im, ax=ax1)

    ax2 = fig.add_subplot(gs[0, 1])
    x_greedy = [x for x in range(1, len(greedy_costs)+1)]
    ax2.plot(x_greedy, greedy_costs, color="blue")
    ax2.set_title("Greedy Search - Altitudes")
    ax2.set_xlabel("Iterations")
    ax2.set_ylabel("Altitude")

    ax3 = fig.add_subplot(gs[1, 1])
    x_annealing = [x for x in range(1, len(annealing_costs)+1)]
    ax3.plot(x_annealing, annealing_costs, color="green")
    ax3.set_title("Simulated Annealing - Altitudes ")
    ax3.set_xlabel("Iterations")
    ax3.set_ylabel("Altitude")

    plt.tight_layout()
    plt.show()

def get_neighbors(point : tuple):
    r = point[0]
    c = point[1]
    neighbors = []
    for j in range(-1, 2):
        for i in range(-1, 2):
            neighbor = (r+j, c+i)
            if neighbor == point or data[neighbor[0]][neighbor[1]]== -1:
                continue
            neighbors.append(neighbor)
    # primitive check
    if len(neighbors) != 8:
        return None
    return neighbors

def altitude_difference(point1, point2):
    # returns difference, and checks constraint (altitude to next point is fewer or equal to 2)
    return data[point2[0]][point2[1]] - data[point1[0]][point1[1]]

def choose_greediest(neighbors, altitudes):
    # sort neighbors in relation to altitude difference, choose iteratively until constraint met
    sorted_points = sorted(neighbors, key=lambda point: altitudes[neighbors.index(point)])
    # print(sorted_points)
    altitudes.sort()
    # print(altitudes)
    flag = False
    for i, point in enumerate(sorted_points):
        # check constraint
        if abs(altitudes[i]) <= 2:
            flag = True
            return point, flag
    return None, False

    
def greedy_search(start_point : tuple, iterations=100):
    # altitude works as the cost function
    stored_altitudes = []
    current_point = start_point
    for _ in range(iterations):
        altitudes = []
        neighbors = get_neighbors(current_point)
        # print(neighbors)
        for neighbor in neighbors:
            difference = altitude_difference(current_point, neighbor)
            altitudes.append(difference)
                
        point, flag = choose_greediest(neighbors, altitudes)
        
        # if point is the same, it did not change, therefore there is no better neighbor
        if flag is False:
            print("quitted for maximum reached")
            return stored_altitudes, convert_to_x_y(current_point)
        else:
            current_point = point
            stored_altitudes.append(data[point[0]][point[1]])
    print("quitted by iterations")  
    return stored_altitudes, convert_to_x_y(current_point)
    
def simulated_annealing(start_point : tuple, iterations=1000, temperature=10, cooling=0.95):
    best_altitude = data[start_point[0], start_point[1]]
    best_point = start_point
    
    stored_altitudes = []
    
    current_point = best_point
    current_altitude = best_altitude
    
    for _ in range(iterations):
        neighbors = get_neighbors(current_point)
        random_point = random.choice(neighbors)
        altitude = data[random_point[0]][random_point[1]]
        difference = altitude_difference(current_point, random_point)
        
        if difference >= -2 and difference < 0:
            best_altitude = altitude
            best_point = random_point
            stored_altitudes.append(altitude)
            
        else:
            acceptance = np.exp(abs(difference) / temperature)
            if random.uniform(0, 1) <= acceptance:
                current_altitude = altitude
                current_point = random_point
                stored_altitudes.append(current_altitude)
                
                if current_altitude < best_altitude:
                    best_altitude = current_altitude
                    best_point = current_point
            
        temperature *= cooling          
    return stored_altitudes, convert_to_x_y(best_point)
    
def main():
    # (x, y) to (r, c)
    iterations=200
    
    example_point1 = (3350, 5800)
    example_point2 = (6000, 6500)
    example_point3 = (2000, 2500)
    example_point4 = (6000, 2300)
    example_point5 = (6000, 9000)
    example_point6 = (1500, 1600)
    
    start_point = example_point1
    
    converted_start_point = convert_to_r_c(start_point)
    
    start_time_greedy = time.time()
    greedy_costs, minimum_point_greedy = greedy_search(converted_start_point, iterations=iterations)
    greedy_time = time.time() - start_time_greedy
    
    start_time_annealing = time.time()
    annealing_costs, minimum_point_simulated = simulated_annealing(converted_start_point, iterations=iterations)
    annealing_time = time.time() - start_time_annealing
    
    # reporte
    print(f"""\n
          final greedy coordinate: {minimum_point_greedy}\n
          greedy execution time: {greedy_time}\n
          amount of nodes explored: {len(greedy_costs)}\n
          distance from origin (m): {euclidian_distance(start_point, minimum_point_greedy)}
          """)
    
    print(f"""\n
          final annealing coordinate: {minimum_point_simulated}\n
          annealing execution time: {annealing_time}\n
          amount of nodes explored: {len(annealing_costs)}\n
          distance from origin (m): {euclidian_distance(start_point, minimum_point_simulated)}
          """)

    plot(start_point, minimum_point_greedy, minimum_point_simulated, greedy_costs, annealing_costs)
    

if __name__ == "__main__":
    main()
