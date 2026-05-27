class Shape:

    def get_area(self):
        pass

    def get_perimeter(self):
        pass
    
    @staticmethod
    def is_error_value(*args):
        for num in args:
            if not isinstance(num, (int,float)) or num <=0:
                return True
        return False

    def __str__(self):
        return f"Shape : {self.__class__.__name__} \n Area : {self.get_area()} \n perimter : {self.get_perimeter()}"