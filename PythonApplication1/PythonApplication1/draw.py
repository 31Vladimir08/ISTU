import numpy as np
import matplotlib.pyplot as plt
import graphFunctions as graph
import searchIntersectionPoint as points
import math
import re

class Draw:
    def __init__(self, a = 0.0, b = 0.0, c = 0.0, d = 0.0):
        self.__a = float(a)
        self.__b = float (b)
        self.__c = float(c)
        self.__d = float(d)

    def create_draw(self, point_start, point_finish, y, list_intersection_points):
        plt.close()
        draw_fun = graph.GraphFunctions(self.__a, self.__b, self.__c, self.__d)
         # график.       
        x = np.linspace(point_start, point_finish, 100)
        X0 = np.linspace(point_start, point_finish, 2)
        # y0...y - линии одного графика, для каждой линии свой набор точек.
        Y0 = y + X0 * 0
        Y = draw_fun.return_fun_x(x)

        # list_intersection_points = points.SearchIntersectionPoint(self.__a, self.__b, self.__c, self.__d).return_list_intersection_points(point_start, point_finish, y)
        
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
        ax.scatter(point_start, draw_fun.return_fun_x(point_start), color = 'black', s = 20, marker = 'o')
        ax.scatter(point_finish, draw_fun.return_fun_x(point_finish), color = 'black', s = 20, marker = 'o')
        count = len(list_intersection_points)
        if count > 0:
           for i in range(count):
               ax.scatter(list_intersection_points[i].coordinate_x, list_intersection_points[i].coordinate_y, color='red', s=20, marker='o')   
               # Добавление аннотации          
               xy = (list_intersection_points[i].coordinate_x, list_intersection_points[i].coordinate_y)
               ax.annotate('(%.5s, %.5s)' % xy, xy = xy, textcoords = 'data')

        # показать рисунок
        plt.show()
        return True
    def close_draw(self):
        plt.close()