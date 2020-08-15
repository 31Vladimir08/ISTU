import numpy as np
import matplotlib.pyplot as plt
import graphFunctions as graph
import searchIntersectionPoint as points
import math
import re

class Draw:
    def create_draw(self, a, b, c, d, point_start, point_finish, y):
        plt.close()
         # график.       
        x = np.linspace(point_start, point_finish, 100)
        X0 = np.linspace(point_start, point_finish, 2)
        draw = points.SearchIntersectionPoint()
        # y0...y - линии одного графика, для каждой линии свой набор точек.
        Y0 = y + X0 * 0
        Y = graph.GraphFunctions().return_fun_x(a, b, c, d, x)

        list_intersection_points = draw.return_list_intersection_points(a, b, c, d, point_start, point_finish, y)
        
        # будет 1 график, на нем 2 линии:
        fig, ax = plt.subplots()

        # функция y(x)
        ax.plot(x, Y, color = "black", label = "y=ax^3+bx^2+cx+d")

        # функция y0
        ax.plot(X0, Y0, color="red", label="Y0")

        # подпись у горизонтальной оси х
        ax.set_xlabel("x")

        # подпись у вертикальной оси y
        ax.set_ylabel("y")

        # показывать условные обозначения
        ax.legend()

        # сетка на графике
        ax.set_title("")
        ax.grid()

        # ставим точки на графике 
        ax.scatter(point_start, graph.GraphFunctions().return_fun_x(a, b, c, d, point_start), color = 'black', s = 20, marker = 'o')
        ax.scatter(point_finish, graph.GraphFunctions().return_fun_x(a, b, c, d, point_finish), color = 'black', s = 20, marker = 'o')
    
        if len(list_intersection_points) > 0:
           i = -1
           ax.scatter(list_intersection_points[i].coordinate_x, list_intersection_points[i].coordinate_y, color='red', s=20, marker='o')   
           
           # Добавление аннотации          
           xy = (list_intersection_points[i].coordinate_x, list_intersection_points[i].coordinate_y)
           ax.annotate('(%.5s, %.5s)' % xy, xy = xy, textcoords = 'data')

           # очищаем массивы
           # self._listX.clear()
           # self._listY.clear()         

        # показать рисунок
        plt.show()  
    