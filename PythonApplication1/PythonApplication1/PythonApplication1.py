import matplotlib.pyplot as plt
import numpy as np
import math

class Graph:
    _a=0
    _b=0
    _n=5
    listX=[]
    listY=[]

    def MyInput(self):
        self._a=float(input("Введите числовое значение параметра а= "))
        self._b=float(input("Введите числовое значение параметра b= "))       
 
    def Fun(self, x):
        return x**3 - 6*(x**2) + 0.3*x+17  
    # по кол-ву интераций
    def MyMethod(self):
        a=self._a
        b=self._b
        n=self._n
        fa=self.Fun(a);
        fb=self.Fun(b);    
        if(fa>0 and fb<0) or (fa<0 and fb>0):
            while n>0:            
                n=n-1
                x = (a + b) / 2.0          
                fx = self.Fun(x)
                fa = self.Fun(a)
                self.listX.append(x)
                self.listY.append(fx)
            
                if (fx < 0 and fa < 0) or (fx > 0 and fa > 0):
                  a = x
                else:
                  b = x           
            return x        
        elif(fa==0):
            self.listX.append(a)        
            self.listY.append(self.Fun(a))        
        elif(fb==0):        
            self.listX.append(b)        
            self.listY.append(self.Fun(b))
        else:        
            print("Корней нет")
    def MyPrint(self):
        i=0
        while i<len(self.listX):
            print(i+1,') x= ', self.listX[i], ' y= ', self.listY[i])
            i=i+1
    def Draw(self):
        # график.
        a=self._a
        b=self._b
        x = np.linspace(a, b, 100)
        # y1...y4 - линии одного графика, для каждой линии свой набор точек.
        y=self.Fun(x);
        # будет 1 график, на нем 1 линия:
        fig, ax = plt.subplots()
        # функция y(x)
        ax.plot(x, y, color="black", label="y=x^3-6x^2+0.3x+17")

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
            ax.annotate (num+1, xy=(self.listX[num], self.listY[num]+3))
            num=num+1    
        #показать рисунок
        plt.show()  

MyGraph=Graph()
MyGraph.MyInput()
MyGraph.MyMethod()
MyGraph.MyPrint()
MyGraph.Draw()


