class GraphFunctions:
    def return_fun_x(self, a, b, c, d, x):
        return a * (x ** 3) + b * (x ** 2) + c * x + d 
    def return_discriminant(self, a, b, c):
        return (2 * b) ** 2 - (4 * 3 * a * c)
    def find_extremum_fun_x(self, a, b, c):
        list_x = []
        discriminant = self.return_discriminant(a, b, c)
        if (discriminant > 0):
            list_x.append((-(b * 2) - (discriminant ** 0.5)) / (2 * 3 * a))
            list_x.append((-(b * 2) + (discriminant ** 0.5)) / (2 * 3 * a))
            list_x.sort()
        elif (discriminant == 0):
            list_x.append((-(b * 2)) / (2 * 3 * a))
        else:
            list_x.clear()
        return list_x