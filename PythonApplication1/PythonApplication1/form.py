import tkinter as tk
import draw
import searchIntersectionPoint as points
from tkinter import ttk
from tkinter import messagebox

class Form:
    def __init__(self):
        self.__list_intersection_points = []
    @property
    def intersection_points(self):
        return self.__list_intersection_points
    @intersection_points.setter
    def intersection_points(self, value):
        self.__list_intersection_points = value
     # метод в котором реализуется нажатие кнопки
    def execute(self):
        try:
            float_a = float(self.input_a.get())
            float_b = float(self.input_b.get())
            float_c = float(self.input_c.get())
            float_d = float(self.input_d.get())
            float_y = float(self.input_y.get())
            float_start_point = float(self.input_start_point.get())
            float_finish_point = float(self.input_finish_point.get())
            self.intersection_points = points.SearchIntersectionPoint(float_a, float_b, float_c, float_d).return_list_intersection_points(float_start_point, float_finish_point, float_y)
            draw.Draw(float_a, float_b, float_c, float_d).create_draw(float_start_point, float_finish_point, float_y, self.intersection_points)
        except BaseException as ex:
            messagebox.showinfo("Error", ex.args)
    def create_window(self):
        app = tk.Tk()
        app.title("Приложение находит точку пересечения графика функции типа ax^3 + bx^2 + cx + d = 0 с заданной прямой на участке с заданным интерваллом")
        app.geometry("700x100")
        label_a = ttk.Label(app, text = 'Параметр а=')
        label_a.grid(row = 0, column = 0)

        self.input_a = ttk.Entry(app, width = 10)
        self.input_a.grid(row = 0, column = 1)

        self.label_b = ttk.Label(app, text = 'Параметр b=')
        self.label_b.grid(row = 0, column = 2)

        self.input_b = ttk.Entry(app, width = 10)
        self.input_b.grid(row = 0, column = 3)

        self.label_c = ttk.Label(app, text = 'Параметр c=')
        self.label_c.grid(row = 0, column = 4)

        self.input_c = ttk.Entry(app, width = 10)
        self.input_c.grid(row = 0, column = 5)

        self.label_d = ttk.Label(app, text = 'Параметр d=')
        self.label_d.grid(row = 0, column = 6)

        self.input_d = ttk.Entry(app, width = 10)
        self.input_d.grid(row = 0, column = 7)

        self.label_span = ttk.Label(app, text = 'Введите интервал по оси Х')
        self.label_span.grid(row = 1, column = 4)

        self.label_y = ttk.Label(app, text = 'От')
        self.label_y.grid(row = 2, column = 0)

        self.input_start_point = ttk.Entry(app, width = 10)
        self.input_start_point.grid(row = 2, column = 1)

        self.label_y = ttk.Label(app, text = 'До')
        self.label_y.grid(row = 2, column = 2)

        self.input_finish_point = ttk.Entry(app, width = 10)
        self.input_finish_point.grid(row = 2, column = 3)

        label_y = ttk.Label(app, text = 'Параметр Y0=')
        label_y.grid(row = 2, column = 4)

        self.input_y = ttk.Entry(app, width = 10)
        self.input_y.grid(row = 2, column = 5)    
    
        self.btn_search = ttk.Button(app, text = 'Найти', width = 10, command = self.execute)
        self.btn_search.grid(row = 2, column = 7)
    
        app.mainloop()