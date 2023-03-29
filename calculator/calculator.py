from math import sqrt

class Calculator:
    def __init__(self):
        self.result = 0

        self._first = 0
        self._second = 0
        self._operation = ''

        self.operations = {
            '+' : self.add, 
            '-' : self.subtract, 
            '*' : self.multiply, 
            '/' : self.divide, 
            '^' : self.exponentation}

    def handle_operations(self):
        self.operations[self._operation]()

    def add(self):
        self.result = self._first + self._second

    def subtract(self):
        self.result = self._first - self._second
    
    def multiply(self):
        self.result = self._first * self._second
    
    def divide(self):
        if self._second == 0:
            raise ZeroDivisionError
        self.result  = self._first / self._second
    
    def exponentation(self):
        if self._first == self._second == float('0'):
            raise ValueError
        self.result = self._first ** self._second
    
    def sqrt(self):
        self.result = sqrt(self._first)
    
    def reset(self):
        self.result = 0
        self._first = 0
        self._second = 0

    def set_first(self, num):
        if num not in '+-/*√^=':
            self._first = float(num)

    def set_second(self, num):
        if num not in '+-/*√^=':
            self._second = float(num)

    def set_operation(self, operation):
        self._operation = operation

    def get_result(self):
        return str(self.result)