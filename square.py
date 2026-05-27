from rectangle import Rectangle 


class Squre(Rectangle):

    def __init__(self, side):
        super().__init__(width = side, height = side)

        def get_area(self):
           return self.side * self.side
        
        def get_perimeter(self):
            return self.height * 4
        
        def get_repr(self):
         return f":width{self.width},height:{self.height}"


a = Squre(5)
print(a.get_area())