class GraphFunctions:
    def return_fun_x(self, a, b, c, d, x):
        return a * (x ** 3) + b * (x ** 2) + c * x + d 
    def return_discriminant(self, a, b, c):
        return (2 * b) ** 2 - (4 * 3 * a * c)
    def find_extremum_fun_x(self, a, b, c):
        list_x = []
        if (a != 0 and b != 0 and c != 0):
            discriminant = self.return_discriminant(a, b, c)
            if (discriminant > 0):
                list_x.append((-(b * 2) - (discriminant ** 0.5)) / (2 * 3 * a))
                list_x.append((-(b * 2) + (discriminant ** 0.5)) / (2 * 3 * a))
                list_x.sort()
            elif (discriminant == 0):
                list_x.append((-(b * 2)) / (2 * 3 * a))
            else:
                list_x.clear()
        elif (a == 0 and b != 0):
            list_x.append((-c) / (2 * b))
        elif (b == 0 and a != 0):
            square_x = (-c) / (3 * a)
            if (square_x >= 0):
                list_x.append(square_x ** 0.5)
            else:
                list_x.clear()
        else:
            list_x.clear()
        return list_x