import graphFunctions as gfun
import intersectionPoint as point
class SearchIntersectionPoint:
    def __init__(self, a, b, c, d):
        self.__a = float(a)
        self.__b = float (b)
        self.__c = float(c)
        self.__d = float(d)
    def find_intersection_point(self, pointStart, pointFinish, y):
        n = 10      
        graphFunctions = gfun.GraphFunctions(self.__a, self.__b, self.__c, self.__d)
        fa = graphFunctions.return_fun_x(pointStart)
        fb = graphFunctions.return_fun_x(pointFinish)  
        if (fa > y and fb < y) or (fa < y and fb > y):
            while n > 0:            
                n = n - 1
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
        
    def return_list_intersection_points(self, point_start, point_finish, y):
        list_intersection_points = []
        list_extremum_x = gfun.GraphFunctions(self.__a, self.__b, self.__c, self.__d).find_extremum_fun_x()
        count = len(list_extremum_x) if (list_extremum_x is not None) else 0
        if (count == 0):
            point_added = self.return_intersection_point(point_start, point_finish, y)
            if (point_added is not None):
                list_intersection_points.append(point_added)
        elif (count == 1):
            if ((point_start < list_extremum_x[0] and point_finish < list_extremum_x[0]) or (point_start >= list_extremum_x[0] and point_finish > list_extremum_x[0])):
                point_added = self.return_intersection_point(point_start, point_finish, y)
                if (point_added is not None):
                    list_intersection_points.append(point_added)
            else:
                point_added = self.return_intersection_point(point_start, list_extremum_x[0], y)
                if (point_added is not None):
                    list_intersection_points.append(point_added)
                point_added = self.return_intersection_point(list_extremum_x[0], point_finish, y)
                if (point_added is not None):
                    list_intersection_points.append(point_added)
        else:
            if ((point_start < list_extremum_x[0] and point_finish < list_extremum_x[0]) or (point_start >= list_extremum_x[len(list_extremum_x) - 1] and point_finish > list_extremum_x[len(list_extremum_x) - 1])):
                point_added = self.return_intersection_point(point_start, point_finish, y)
                if (point_added is not None):
                    list_intersection_points.append(point_added)
            else:
                for item in list_extremum_x:
                    pass
        return list_intersection_points
    def return_intersection_point(self, pointStart, pointFinish, y):
        intersection_point = point.IntersectionPoint()
        intersection_point.coordinate_x = self.find_intersection_point(pointStart, pointFinish, y)
        intersection_point.coordinate_y = gfun.GraphFunctions(self.__a, self.__b, self.__c, self.__d).return_fun_x(intersection_point.coordinate_x) if (intersection_point.coordinate_x is not None) else None
        return intersection_point if (intersection_point.coordinate_y is not None) else None
    

