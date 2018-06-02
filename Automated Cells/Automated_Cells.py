from sys import *
from Grid import *
from matplotlib import pyplot as plt


class A:
    def __init__(self):
        self.b = 5

        
moja = A()

print('Hello Barszczyk Opierdalaczu')
grid = Grid()
grid.perform_next_step()
print(grid.matrix[0][0].deads)

grid.perform_next_step()
print(grid.matrix[0][0].deads)

grid.perform_next_step()
print(grid.matrix[0][0].deads)


grid.perform_next_step()

print(grid.matrix[0][0].deads)

plt.hold(True)

for i in range(10):
    for j in range(10):
        plt.plot( [i], [j], marker = 's', markersize = 30, color = grid.matrix[i][j].get_plot_color(), label ='point')
           
plt.grid()
plt.show()
            