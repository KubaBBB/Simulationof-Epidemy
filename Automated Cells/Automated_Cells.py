from sys import *
from Grid import *
from matplotlib import pyplot as plt

def main(size):
    print('Hello Barszczyk Opierdalaczu')
    

    grid = Grid(size)
    grid.perform_next_step()
    print(grid.matrix[0][0].get_deads())

    grid.perform_next_step()
    print(grid.matrix[0][0].get_deads())

    grid.perform_next_step()
    print(grid.matrix[0][0].get_deads())


    grid.perform_next_step()

    print(grid.matrix[0][0].get_deads())

    plt.hold(True)

    for i in range(grid.get_grid_size()):
        for j in range(grid.get_grid_size()):
            plt.plot( [i], [j], marker = 's', markersize = 5, color = grid.matrix[i][j].get_plot_color(), label ='point')
           
    plt.grid()
    plt.show()


if __name__ == "__main__":
    size = 30
    main(size)



            