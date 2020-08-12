import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
import math
import re

# класс отвечает за математические расчеты
class Graph(): 

    # Переменная i отвечает за индекс массива
    _i = -1
    _listX = []
    _listY = []           
   
    def Fun0(self, Y, x):
        return Y + x * 0
    def Fun(self, x):
        return x ** 3 - 6 * (x ** 2) + 0.3 * x + 17 
    
    # по кол-ву интераций
    def MyMath(self, a, b, Y):
        n = 10      
        fa = self.Fun(a);
        fb = self.Fun(b);    
        if (fa > Y and fb < Y) or (fa < Y and fb > Y):
            while n > 0:            
                n = n - 1
                x = (a + b) / 2.0          
                fx = self.Fun(x)
                fa = self.Fun(a)
                self._listX.append(x)
                self._listY.append(fx)
                self._i = self._i + 1
            
                if (fx < Y and fa < Y) or (fx > Y and fa > Y):
                  a = x
                else:
                  b = x           
            return x        
        elif (fa == Y):
            self._listX.append(a)        
            self._listY.append(self.Fun(a))        
        elif (fb == Y):        
            self._listX.append(b)        
            self._listY.append(self.Fun(b))
        
    # функция отвечает за отображение графика
    def Draw (self, a, b, Y):   
        
        # график.       
        x = np.linspace(a, b, 100)
        X0 = np.linspace(a, b, 2)
        
        # y0...y - линии одного графика, для каждой линии свой набор точек.
        Y0 = self.Fun0(Y, X0)
        y = self.Fun(x)
        
        # будет 1 график, на нем 2 линии:
        fig, ax = plt.subplots()

        # функция y(x)
        ax.plot(x, y, color = "black", label = "y=x^3-6x^2+0.3x+17")

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
        ax.scatter(a, self.Fun(a), color = 'black', s = 20, marker = 'o')
        ax.scatter(b, self.Fun(b), color = 'black', s = 20, marker = 'o')
    
        if len(self._listX) > 0:
           ax.scatter(self._listX[self._i], self._listY[self._i], color='red', s=20, marker='o')   
           
           # Добавление аннотации          
           xy = (self._listX[self._i], self._listY[self._i])
           ax.annotate('(%.5s, %.5s)' % xy, xy = xy, textcoords = 'data')

           # очищаем массивы
           self._listX.clear()
           self._listY.clear()         

        # показать рисунок
        plt.show()  

# класс отвечающий за графический интерфейс
class Form():
    _a = 0
    _b = 0
    _y = 0
    bool = False

    # метод, отвечающий за ввод данных
    def MyInput(self):  
        patern = "^(0$|-?[1-9]\d*(\.\d*[1-9]$)?|-?0\.\d*[1-9])$"
       
        # проверка на соответствие регулярному выражению        
        str_a = self.input_a.get()
        str_b = self.input_b.get()
        str_y = self.input_y.get()
        if (re.match(patern, str_a) and re.match(patern, str_b) and re.match(patern, str_y)) is not None:
            self._a = float(str_a)
            self._b = float(str_b)
            self._y = float(str_y)
            self.bool = True
       
    # метод в котором реализуется нажатие кнопки
    def Search(self):
        try:            
            self.MyInput() 
            if self.bool == True:
                MyGraph = Graph()        
                MyGraph.MyMath(self._a, self._b, self._y)
                MyGraph.Draw(self._a, self._b, self._y)
        except:
            messagebox.showinfo("Ошибка", "Error")

    # метод, создающий графический интерфейс программы
    def CreateForm(self):
        app = tk.Tk()
        app.title("Приложение находит точку пересечения графика функции с заданной прямой")
        app.geometry("700x100")
        label_a = ttk.Label(app, text = 'Параметр а=')
        label_a.grid(row = 0, column = 0)

        self.input_a = ttk.Entry(app, width = 10)
        self.input_a.grid(row = 0, column = 1)

        label_b = ttk.Label(app, text = 'Параметр b=')
        label_b.grid(row = 0, column = 2)

        self.input_b = ttk.Entry(app, width = 10)
        self.input_b.grid(row = 0, column = 3)

        label_y = ttk.Label(app, text = 'Параметр Y0=')
        label_y.grid(row = 0, column = 4)

        self.input_y = ttk.Entry(app, width = 10)
        self.input_y.grid(row = 0, column = 5)    
    
        self.btn_search = ttk.Button(app, text = 'Найти', width = 10, command = self.Search)
        self.btn_search.grid(row = 0, column = 6)
    
        app.mainloop()

MyForm = Form()
MyForm.CreateForm()
       






