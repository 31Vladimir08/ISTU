import matplotlib.pyplot as plt
import numpy as np
import math

a=float(input("Введите числовое значение параметра а= "))
b=float(input("Введите числовое значение параметра b= "))
n=5
listX=[]
listY=[]
  
def f(x):
    return x**3 - 6*(x**2) + 0.3*x+17  
# по кол-ву интераций
def MyMethod(f, a, b, n):
    fa=f(a);
    fb=f(b);    
    if(fa>0 and fb<0) or (fa<0 and fb>0):
        while n>0:            
            n=n-1
            x = (a + b) / 2.0          
            fx = f(x)
            fa = f(a)
            listX.append(x)
            listY.append(fx)
            
            if (fx < 0 and fa < 0) or (fx > 0 and fa > 0):
              a = x
            else:
              b = x           
        return x        
    elif(fa==0):
        listX.append(a)        
        listY.append(f(a))        
    elif(fb==0):        
        listX.append(b)        
        listY.append(f(b))
    else:        
        print("Корней нет")
def MyPrint():
    i=0
    while i<len(listX):
        print(i+1,') x= ', listX[i], ' y= ', listY[i])
        i=i+1
def Draw():
    # график.
    x = np.linspace(a, b, 100)
    # y1...y4 - линии одного графика, для каждой линии свой набор точек.
    y=x**3 - 6*(x**2) + 0.3*x+17;
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
    ax.scatter(a, f(a), color='black', s=70, marker='o')
    ax.scatter(b, f(b), color='black', s=70, marker='o')
    
    if len(listX)>0:
      num=0
      while num<n:   
        ax.scatter(listX[num], listY[num], color='red', s=70, marker='o')         
        #Добавление аннотации
        ax.annotate (num+1, xy=(listX[num], listY[num]+3))
        num=num+1    
    #показать рисунок
    plt.show()  

x = MyMethod(f, a, b, n)
MyPrint();
Draw();


