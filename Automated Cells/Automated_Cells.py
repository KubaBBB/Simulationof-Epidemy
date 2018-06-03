from sys import *
from Grid import *
from matplotlib import pyplot as plt
import numpy as np

def main(size, colors):
    print('Hello Barszczyk Opierdalaczu')
    
    grid = Grid(size)
    grid.perform_next_step()
    print(grid.cells[0][0].get_deads())

    grid.perform_next_step()
    print(grid.cells[0][0].get_deads())

    grid.perform_next_step()
    print(grid.cells[0][0].get_deads())
    
    grid.perform_next_step()

    print(grid.cells[0][0].get_deads())

    plt.hold(True)
        
    X = []
    Y = []
    states_matrix = np.array(grid.get_states_colors())

    for color in colors:
        for i in range(grid.get_grid_size()):
            for j in range(grid.get_grid_size()):
                if states_matrix[i][j] == color:
                    X = np.insert(X, len(X),i)
                    Y = np.insert(Y, len(Y),j)

        plt.scatter( X, Y, marker = 's', c = color)

        X=[]
        Y=[]
   
    #plt.grid()
    plt.show()
    

if __name__ == "__main__":
    size = 30
    colors = ['white','green','yellow','orange','black']
    main(size, colors)
                    