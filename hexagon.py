import math
from calculator import Shape


class Hexagon(Shape):
    def __init__(self,side):
        is_error_value = Hexagon.is_error_value(side)
        if is_error_value:
                raise ValueError
        
        self.side = side

    def get_area(self):
         return (3 * math.sqrt(3) * math.pow(self.side,2)) /2 

    def get_perimeter(self):
        return 6 * self.side    

    def get_repr(self):
         return f"side :{self.side}"