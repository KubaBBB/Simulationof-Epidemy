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

plt.scatter([1,2,3], [2, 2, 2])

plt.hold(True)
plt.scatter([1,2,3], [3, 3, 3])
plt.hold(True)

plt.scatter([1,2,3], [1, 1, 1])

plt.plot( [5], [7], marker = 's', markersize = 50, color = grid.matrix[0][0].get_plot_color(), label ='point')

plt.grid()
plt.show()
            