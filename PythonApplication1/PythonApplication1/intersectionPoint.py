class IntersectionPoint:
    def __init__(self):
        self.__coordinate_x = 0.0
        self.__coordinate_y = 0.0
    @property
    def coordinate_x(self):
        return self.__coordinate_x
    @coordinate_x.setter
    def coordinate_x(self, value):
        if (value is not None):
            self.__coordinate_x = float(value)
        else: 
            self.__coordinate_x = None
    @property
    def coordinate_y(self):
        return self.__coordinate_y
    @coordinate_y.setter
    def coordinate_y(self, value):
        if (value is not None):
            self.__coordinate_y = float(value)
        else: 
            self.__coordinate_y = None