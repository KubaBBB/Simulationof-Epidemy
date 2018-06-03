from sys import *
from Grid import *
from matplotlib import pyplot as plt
import numpy as np

def main(size):
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
        
    colours = ['white','green','yellow','orange','black']

    X = []
    Y = []
    #print (grid.get_states_colors())
    
    #for index, row in enumerate( grid.get_states_colors() ):
    #    #print (row)
    #    npArr = np.array(row)
    #    for i in range(grid.get_grid_size()):
    #        x_ins = np.where(npArr[i] == 'yellow')[0]
    #        y_ins = np.array([index for _ in range( np.count_nonzero (x_ins) ) ] )

    #    X = np.insert(X, len(X), x_ins )
    #    Y = np.insert(Y, len(Y), y_ins )
    #    print (np.count_nonzero(x_ins))
    #    print (np.count_nonzero(y_ins))
    #print (X)
    ##print (np.count_nonzero(X))
    #print (Y)
    states_matrix = np.array(grid.get_states_colors())
    for item in colours:
        for i in range(grid.get_grid_size()):
            for j in range(grid.get_grid_size()):
                if states_matrix[i][j] == item:
                    X = np.insert(X, len(X),i)
                    Y = np.insert(Y, len(Y),j)
        plt.scatter( X, Y, marker = 's', c = item)
        print(len(X))
    
        print(len(Y))
        
        X=[]
        Y=[]


    ##print (X)
    
    #print (np.count_nonzero(Y))
    #for colour in colours:
    #    for i in range(size):
    #        coordinates = [coordinates, ( np.where( colour ==
    #        grid.get_states_colors()[i])[0] )]
    #    #print (np.where( colour == grid.get_states_colors())[0])
    #    print (coordinates)

    #values = np.array(['s','a','s','f','s','f','s','s','f','s'])
    #searchval = 3
    #ii = np.where(values == 'f')[0]
    #print (ii)

    #plt.plot( coordinates(:,1), coordinates(:,2), marker = 's', markersize =
    #5, color = colour, label ='point')
    
    #plt.grid()
    plt.show()
    



if __name__ == "__main__":
    size = 30
    main(size)
                    