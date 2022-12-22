import re

class Token:

    def __init__(self, token_type, token_value, token_position):
        self.token_type = token_type
        self.token_value = token_value
        self.token_position = token_position

    def __str__(self):
        return f'{self.token_position}\t\t{self.token_type}\t\t{self.token_value}'
    
    def __repr__(self):
        return self.__str__()