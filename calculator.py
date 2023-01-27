class Calculator:
    def __init__(self):
        self.result = 0
        self.temporary = 0
        

    def add(self, x):
        self.result = self.temporary + x

    def subtract(self, x):
        self.result = self.temporary - x
    
    def multiply(self, x):
        self.result = self.temporary * x
    
    def divide(self, x):
        if x != 0:
            self.result  = self.temporary / x
        else:
            print("Cant divide by 0!")
    
    def change_sign(self):
        self.temporary *= -1
    
    def reset(self):
        self.result = 0
        self.temporary = 0

    def set_temporary(self, num):
        if num not in '+-/*':
            self.temporary = float(num)

    def __str__(self):
        return str(self.result)