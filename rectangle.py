from calculator import Shape

class Rectangle(Shape):

    def __init__(self,width,height):
        is_error_value = Rectangle.is_error_value(width,height)
        if is_error_value:
            raise ValueError ("Side must be greater than 0")

        self.width = width
        self.height = height 


    def get_area(self):
       return  self.width * self.height 

    def get_perimeter(self):
        return  2 * (self.width + self.height)

