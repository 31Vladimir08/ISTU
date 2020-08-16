import tkinter as tk

import draw
import searchIntersectionPoint as points
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import math
import re

class Form:
    def __init__(self):
        self.__app = tk.Tk()
        self.is_sigma = BooleanVar()
        self.__list_intersection_points = []
    @property
    def intersection_points(self):
        return self.__list_intersection_points
    @intersection_points.setter
    def intersection_points(self, value):
        self.__list_intersection_points = value
    
     # метод в котором реализуется нажатие кнопки
    def show_draw_command(self):
        try:
            patern = "^(0$|-?[1-9]\d*(\.\d*[1-9]$)?|-?0\.\d*[1-9])$"
            str_a = self.input_a.get()
            str_b = self.input_b.get()
            str_c = self.input_c.get()
            str_d = self.input_d.get()
            str_y = self.input_y.get()
            str_start_point = self.input_start_point.get()
            str_finish_point = self.input_finish_point.get()
            float_a = float(str_a) if (re.match(patern, str_a) is not None) else 0.0
            float_b = float(str_b) if (re.match(patern, str_b) is not None) else 0.0
            float_c = float(str_c) if (re.match(patern, str_c) is not None) else 0.0
            float_d = float(str_d) if (re.match(patern, str_d) is not None) else 0.0
            float_y = float(str_y) if (re.match(patern, str_y) is not None) else 0.0
            float_start_point = float(str_start_point) if (re.match(patern, str_start_point) is not None) else 0.0
            float_finish_point = float(str_finish_point) if (re.match(patern, str_finish_point) is not None) else 0.0
            if (float_finish_point < float_start_point):
                temp = float_finish_point
                float_finish_point = float_start_point
                float_start_point = temp
            bool_is_sigma = self.is_sigma.get()
            self.intersection_points = points.SearchIntersectionPoint(float_a, float_b, float_c, float_d, bool_is_sigma).return_list_intersection_points(float_start_point, float_finish_point, float_y)
            draw.Draw(float_a, float_b, float_c, float_d).create_draw(float_start_point, float_finish_point, float_y, self.intersection_points)
        except BaseException as ex:
            messagebox.showinfo("Error", ex.args)
    def close_application_command(self):
        draw.Draw().close_draw()
        self.__app.destroy()
    def create_window(self):
        self.__app.title("Приложение находит точки пересечения графика функции типа ax^3 + bx^2 + cx + d = y")
        self.__app.geometry("700x100")
        
        label_a = ttk.Label(self.__app, text = 'Параметр а=')
        label_a.grid(row = 0, column = 0)

        self.input_a = ttk.Entry(self.__app, width = 10)
        self.input_a.grid(row = 0, column = 1)

        label_b = ttk.Label(self.__app, text = 'Параметр b=')
        label_b.grid(row = 0, column = 2)

        self.input_b = ttk.Entry(self.__app, width = 10)
        self.input_b.grid(row = 0, column = 3)

        label_c = ttk.Label(self.__app, text = 'Параметр c=')
        label_c.grid(row = 0, column = 4)

        self.input_c = ttk.Entry(self.__app, width = 10)
        self.input_c.grid(row = 0, column = 5)

        label_d = ttk.Label(self.__app, text = 'Параметр d=')
        label_d.grid(row = 0, column = 6)

        self.input_d = ttk.Entry(self.__app, width = 10)
        self.input_d.grid(row = 0, column = 7)

        label_span = ttk.Label(self.__app, text = 'Введите интервал по оси Х')
        label_span.grid(row = 1, column = 4)

        label_y = ttk.Label(self.__app, text = 'От')
        label_y.grid(row = 2, column = 0)

        self.input_start_point = ttk.Entry(self.__app, width = 10)
        self.input_start_point.grid(row = 2, column = 1)

        label_y = ttk.Label(self.__app, text = 'До')
        label_y.grid(row = 2, column = 2)

        self.input_finish_point = ttk.Entry(self.__app, width = 10)
        self.input_finish_point.grid(row = 2, column = 3)

        label_y = ttk.Label(self.__app, text = 'Параметр y=')
        label_y.grid(row = 2, column = 4)

        self.input_y = ttk.Entry(self.__app, width = 10)
        self.input_y.grid(row = 2, column = 5)
                
        radiobutton_n = ttk.Radiobutton(self.__app, text = 'n = 10', value = False, variable = self.is_sigma)
        radiobutton_n.grid(row = 2, column = 6, sticky=W)

        radiobutton_sigma = ttk.Radiobutton(self.__app, text = 'sigms = 0.000001', value = True, variable = self.is_sigma)
        radiobutton_sigma.grid(row = 2, column = 7, sticky=W)
       
        btn_search = ttk.Button(self.__app, text = 'Найти', width = 10, command = self.show_draw_command)
        btn_search.grid(row = 3, column = 6)

        btn_close = ttk.Button(self.__app, text = 'Закрыть', width = 10, command = self.close_application_command)
        btn_close.grid(row = 3, column = 7)
    
        self.__app.mainloop()