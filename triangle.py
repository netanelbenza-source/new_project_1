from rectangle import Rectangle
 

class Tringle(Rectangle):
    
    def __init__(self, height , base ,side_a,side_b,side_c):
        self.base   = base
        self.height = height
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c 
        # is_error_value = Tringle.is_error_value(self.base,self.height,self.side_a,self.side_b,self.side_c)
        # if not is_error_value:
        #     raise ValueError("Side must be greater than 0")

    def get_area(self):
        return (self.base * self.height) / 2   
   
    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c