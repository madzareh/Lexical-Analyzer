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

class UnknownToken(Exception):
    
    def __init__(self, buffer, token_position):

        super().__init__()
        self.buffer = buffer
        self.token_position = token_position

    def __str__(self):
        return f'\nLexical Analyzer Error: Unknown Token\n\n{self.buffer[self.token_position:self.token_position + 30]}'        