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

class Analyzer:

    def __init__(self, rules, buffer):
        
        rules_list = [f'(?P<{typ}>{reg})' for typ, reg in rules]
        self.regex = re.compile('|'.join(rules_list))
        self.buffer = buffer
        self.token_position = 0

    def token(self):
        
        if self.token_position < len(self.buffer):
            if match := re.compile('\S').search(self.buffer, self.token_position):
                self.token_position = match.start()
            else:
                return None

            if match := self.regex.match(self.buffer, self.token_position):
                token = Token(token_type = match.lastgroup, token_value = match.group(match.lastgroup), token_position = self.token_position)
                self.token_position = match.end()
                return token
            else:
                raise UnknownToken(self.buffer, self.token_position)

    def generate_token(self):
        
        self.token_position = 0
        while token := self.token():
            yield token        