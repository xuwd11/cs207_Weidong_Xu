import numpy as np

class Circle:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def cal_radius(self):
        self.r = np.sqrt(self.x*self.x + self.y*self.y)
        return self.r
    
    def cal_area(self):
        if 'r' in vars(self):
            self.area = np.pi * self.r*self.r
        else:
            self.area = np.pi * (self.x*self.x + self.y*self.y)
        return self.area
    
    def cal_circumference(self):
        if 'r' in vars(self):
            self.cir = 2 * np.pi * np.sqrt(self.r*self.r)
        else:
            self.cir = 2 * np.pi * np.sqrt(self.x*self.x + self.y*self.y)
        return self.cir
    
    def print_circle(self):
        print('x = ', self.x)
        print('y = ', self.y)
        print('radius = ', self.r)
        print('area = ', self.area)
        print('circumference = ', self.cir)