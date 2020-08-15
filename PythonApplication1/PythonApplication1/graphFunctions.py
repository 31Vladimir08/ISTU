class GraphFunctions:
    def __init__(self, a, b, c, d):
        self.__a = float(a)
        self.__b = float (b)
        self.__c = float(c)
        self.__d = float(d)

    def return_fun_x(self, x):
        return self.__a * (x ** 3) + self.__b * (x ** 2) + self.__c * x + self.__d 
    def return_discriminant(self):
        return (2 * self.__b) ** 2 - (4 * 3 * self.__a * self.__c)
    def find_extremum_fun_x(self):
        list_x = []
        if (self.__a != 0 and self.__b != 0 and self.__c != 0):
            discriminant = self.return_discriminant()
            if (discriminant > 0):
                list_x.append((-(self.__b * 2) - (discriminant ** 0.5)) / (2 * 3 * self.__a))
                list_x.append((-(self.__b * 2) + (discriminant ** 0.5)) / (2 * 3 * self.__a))
                list_x.sort()
            elif (discriminant == 0):
                list_x.append((-(self.__b * 2)) / (2 * 3 * self.__a))
            else:
                list_x.clear()
        elif (self.__a == 0 and self.__b != 0):
            list_x.append((-self.__c) / (2 * self.__b))
        elif (self.__b == 0 and self.__a != 0):
            square_x = (-self.__c) / (3 * self.__a)
            if (square_x >= 0):
                list_x.append(square_x ** 0.5)
            else:
                list_x.clear()
        else:
            list_x.clear()
        return list_x