import graphFunctions as gfun
import intersectionPoint as point
class SearchIntersectionPoint:
    def find_intersection_point(self, a, b, c, d, pointStart, pointFinish, y):
        n = 10      
        graphFunctions = gfun.GraphFunctions()
        fa = graphFunctions.return_fun_x(a, b, c, d, pointStart)
        fb = graphFunctions.return_fun_x(a, b, c, d, pointFinish)    
        if (fa > y and fb < y) or (fa < y and fb > y):
            while n > 0:            
                n = n - 1
                x = (pointStart + pointFinish) / 2.0          
                fx = graphFunctions.return_fun_x(a, b, c, d, x)
                fa = graphFunctions.return_fun_x(a, b, c, d, pointStart)
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
        graphFunctions = gfun.GraphFunctions()
        list_extremum_x = graphFunctions.find_extremum_fun_x(a, b, c)
        list_intersection_points = []
        point_x = self.find_intersection_point(a, b, c, d, pointStart, pointFinish, y)
        point_y = gfun.GraphFunctions().return_fun_x(a, b, c, d, point_x)
        list_intersection_points.append(point.IntersectionPoint(point_x, point_y))
        return list_intersection_points
