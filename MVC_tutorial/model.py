"""
Model module
"""

class Model:
    """
    Model class
    """

    def __init__(self):
        """
        Constructor
        """
        self.previous_value = ''
        self.value =''
        self.operator = ''

    def calculate(self, caption):
        if caption == 'C':
            self.previous_value = ''
            self.value = ''

        elif isinstance(caption, int):
            self.value += str(caption)   

        elif caption == '+/-':
            self.value = self.value[1:] if self.value[0] == '-' else '-' + self.value

        elif caption == '%':
            pass 

        elif caption == '.':
            if not caption in self.value:
                self.value += caption

        elif caption == '=':
            self.value = str(self._evaluate())
            pass
        else:
            if self.value:
                if caption == '/' and isinstance(self.previous_value, int) and isinstance(self.value, int):
                    self.operator = '//' 
                else:
                    self.operator = caption
                
                self.previous_value = self.value
                self.value = ''
            pass
        return self.value

    def _evaluate(self):
        return eval(self.previous_value+self.operator+self.value)
