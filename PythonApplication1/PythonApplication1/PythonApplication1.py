import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import matplotlib.pyplot as plt
import numpy as np
import math

class Graph():
    
    _a=0
    _b=0
    _n=5
    _Y=0
    listX=[]
    listY=[]

    def MyInput(self, a, b, Y):
        self._a=a
        self._b=b
        self._Y=Y             
   
    def Fun0(self, x):
        return self._Y+x*0
    def Fun(self, x):
        return x**3 - 6*(x**2) + 0.3*x+17  
    # по кол-ву интераций
    def MyMath(self):
        a=self._a
        b=self._b
        n=self._n
        fa=self.Fun(a);
        fb=self.Fun(b);    
        if(fa>self._Y and fb<self._Y) or (fa<self._Y and fb>self._Y):
            while n>0:            
                n=n-1
                x = (a + b) / 2.0          
                fx = self.Fun(x)
                fa = self.Fun(a)
                self.listX.append(x)
                self.listY.append(fx)
            
                if (fx < self._Y and fa < self._Y) or (fx > self._Y and fa > self._Y):
                  a = x
                else:
                  b = x           
            return x        
        elif(fa==self._Y):
            self.listX.append(a)        
            self.listY.append(self.Fun(a))        
        elif(fb==self._Y):        
            self.listX.append(b)        
            self.listY.append(self.Fun(b))
        else:        
            messagebox.showinfo("GUI Python", "Корней нет")
    
    def Draw(self):
       
        # график.
        a=self._a
        b=self._b
        
        x = np.linspace(a, b, 100)
        X0 = np.linspace(a, b, 2)
        
        # y1...y4 - линии одного графика, для каждой линии свой набор точек.
        Y0=self.Fun0(X0)
        y=self.Fun(x)      
        # будет 1 график, на нем 1 линия:
        fig, ax = plt.subplots()
        # функция y(x)
        ax.plot(x, y, color="black", label="y=x^3-6x^2+0.3x+17")
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
        ax.scatter(a, self.Fun(a), color='black', s=70, marker='o')
        ax.scatter(b, self.Fun(b), color='black', s=70, marker='o')
    
        if len(self.listX)>0:
          num=0          
          while num<self._n:   
            ax.scatter(self.listX[num], self.listY[num], color='red', s=70, marker='o')         
            #Добавление аннотации
            ax.annotate (num+1, xy=(self.listX[num], self.listY[num]))           
            num=num+1    
        #показать рисунок
        plt.show()  

app=tk.Tk()
app.title("Приложение находит точку пересечения графика функции с заданной прямой")
app.geometry("700x100")
label_a=ttk.Label(app, text='Параметр а=')
label_a.grid(row=0, column=0)

input_a=ttk.Entry(app, width=10)
input_a.grid(row=0, column=1)

label_b=ttk.Label(app, text='Параметр b=')
label_b.grid(row=0, column=2)

input_b=ttk.Entry(app, width=10)
input_b.grid(row=0, column=3)

label_y=ttk.Label(app, text='Параметр Y0=')
label_y.grid(row=0, column=4)

input_y=ttk.Entry(app, width=10)
input_y.grid(row=0, column=5)
    
def Search():
    MyGraph=Graph()
    MyGraph.MyInput(float(input_a.get()), float(input_b.get()), float(input_y.get()))
    MyGraph.MyMath()
    MyGraph.Draw()
    
btn_search=ttk.Button(app, text='Найти', width=10, command=Search)
btn_search.grid(row=0, column=6)
    
app.mainloop()
       






