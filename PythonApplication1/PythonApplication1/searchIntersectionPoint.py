import graphFunctions as gfun
import intersectionPoint as point
class SearchIntersectionPoint:
    def __init__(self, a = 0.0, b = 0.0, c = 0.0, d = 0.0, is_sigma = False):
        self.__a = float(a)
        self.__b = float (b)
        self.__c = float(c)
        self.__d = float(d)
        self.__is_sigma = bool(is_sigma)
    def find_intersection_point(self, pointStart, pointFinish, y):
        n = 10      
        sigma = 0.000001
        graphFunctions = gfun.GraphFunctions(self.__a, self.__b, self.__c, self.__d)
        fa = graphFunctions.return_fun_x(pointStart)
        fb = graphFunctions.return_fun_x(pointFinish)  
        if (fa > y and fb < y) or (fa < y and fb > y):
            if (self.__is_sigma == False):
                while n > 0:            
                    n = n - 1
                    x = (pointStart + pointFinish) / 2.0          
                    fx = graphFunctions.return_fun_x(x)
                    fa = graphFunctions.return_fun_x(pointStart)
                    if (fx < y and fa < y) or (fx > y and fa > y):
                      pointStart = x
                    else:
                      pointFinish = x    
            else:
                while sigma < abs(pointStart - pointFinish):
                    x = (pointStart + pointFinish) / 2.0          
                    fx = graphFunctions.return_fun_x(x)
                    fa = graphFunctions.return_fun_x(pointStart)
                    if (fx < y and fa < y) or (fx > y and fa > y):
                        pointStart = x
                    else:
                        pointFinish = x         
            return x        
        elif (fa == y):
            return pointStart        
        elif (fb == y):   
            return pointFinish
        else:
            return None
    def return_list_intersection_points(self, point_start, point_finish, y):
        list_section = []
        list_intersection_points = []
        list_extremum_x = gfun.GraphFunctions(self.__a, self.__b, self.__c, self.__d).find_extremum_fun_x()
        count = len(list_extremum_x) if (list_extremum_x is not None) else 0
        if (count == 0):
            point_added = self.return_intersection_point(point_start, point_finish, y)
            if (point_added is not None):
                list_intersection_points.append(point_added)
        else:
            list_section.append(point_start)
            list_section.append(point_finish)
            for item in list_extremum_x:
                if (item > point_start and item < point_finish):
                    list_section.append(item)
            list_section.sort()
            for index in range (len(list_section) - 1):
                point_added = self.return_intersection_point(list_section[index], list_section[index + 1], y)
                if (point_added is not None):
                    list_intersection_points.append(point_added)
        return list_intersection_points
    def return_intersection_point(self, pointStart, pointFinish, y):
        intersection_point = point.IntersectionPoint()
        intersection_point.coordinate_x = self.find_intersection_point(pointStart, pointFinish, y)
        intersection_point.coordinate_y = gfun.GraphFunctions(self.__a, self.__b, self.__c, self.__d).return_fun_x(intersection_point.coordinate_x) if (intersection_point.coordinate_x is not None) else None
        return intersection_point if (intersection_point.coordinate_x is not None) else None
    

