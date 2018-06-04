from Grid import *
from matplotlib import pyplot as plt
import numpy as np
import time


def main(size, colors, max_iteration):
    print('Hello Barszczyk Opierdalaczu')
    grid = Grid(size)

    X = []
    Y = []
    iteration = 0
    while iteration < max_iteration :
        start = time.time()

        grid.perform_next_step(colors)
        mapped_states = np.array(grid.get_states_colors())
        plt.figure(figsize=(10, 10))
        for color in colors:
            if iteration is not 0:
                grid.reload_grid()
            for i in range(grid.get_grid_size()):
                for j in range(grid.get_grid_size()):
                    if mapped_states[i][j] == color:
                        X = np.insert(X, len(X),i)
                        Y = np.insert(Y, len(Y),j)
            plt.scatter(X, Y, s=100, marker = 's', c = color)
            X = []
            Y = []

        end = time.time()
        print('Time of performing next iteration: ' + str(end - start))
        plt.axis([-1, size, -1, size])
        plt.title('Iteration: ' + str(iteration))
        plt.xlabel('X') 
        plt.ylabel('Y')
        plt.show()
        iteration += 1
        
if __name__ == "__main__": 
    size = 4
    colors = ['white','green','yellow','orange','grey','black', 'blue']
    max_iteration = 20
    main(size, colors, max_iteration)