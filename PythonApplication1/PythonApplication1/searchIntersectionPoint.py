import graphFunctions as gfun
import intersectionPoint as point
class SearchIntersectionPoint:
    def find_intersection_point(self, a, b, c, d, pointStart, pointFinish, y):
        n = 10      
        graphFunctions = gfun.GraphFunctions()
        fa = graphFunctions.return_fun_x(a, b, c, d, pointStart) - y
        fb = graphFunctions.return_fun_x(a, b, c, d, pointFinish) - y   
        if (fa > y and fb < y) or (fa < y and fb > y):
            while n > 0:            
                n = n - 1
                x = (pointStart + pointFinish) / 2.0          
                fx = graphFunctions.return_fun_x(a, b, c, d, x) - y
                fa = graphFunctions.return_fun_x(a, b, c, d, pointStart) - y
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
            return 0
    def return_intersection_points(self, a, b, c, d, pointStart, pointFinish, y):
        list_intersection_points = []
        list_extremum_x = gfun.GraphFunctions().find_extremum_fun_x(a, b, c)
        count = list_extremum_x.count()
        if (count == 0):
            intersection_point = point.IntersectionPoint()
            intersection_point.coordinate_x = self.find_intersection_point(a, b, c, d, pointStart, pointFinish, y)
            intersection_point.coordinate_y = gfun.GraphFunctions().return_fun_x(a, b, c, d, intersection_point.coordinate_x)
            list_intersection_points.append(intersection_point)
        return list_intersection_points
