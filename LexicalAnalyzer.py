import numpy as np
import pandas as pd
from typer import Typer
from Token import Analyzer, UnknownToken

app = Typer()
@app.command()

def lexanalyzer(inputfile):
    rules = [
        ('COMMENT',             r'\#' + r'.*'),
        ('IF_KEYWORD',          r'if'),
        ('ELSE_KEYWORD',        r'else'),
        ('FOR_KEYWORD',         r'for'),
        ('WHILE_KEYWORD',       r'while'),
        ('CONSTANT_STRING',     r'".*?"|\'.*?\''),
        ('CONSTANT_NUMBER',     r'\d+'),
        ('PLUS',                r'\+'),
        ('MINUS',               r'\-'),
        ('MULTIPLY',            r'\*'),
        ('DIVIDE',              r'\/'),
        ('L_PARENTHESES',       r'\('),
        ('L_BRACE',             r'\{'),
        ('R_PARENTHESES',       r'\)'),
        ('R_BRACE',             r'\}'),
        ('COMMA',               r'\,'),
        ('SINGLE_QUOTATION',    r'\''),
        ('DOUBLE_QUOTATION',    r'\"'),
        ('EQUAL',               r'=='),
        ('ASSIGNMENT',          r'='),
        ('COLON',               r':'),
        ('SEMICOLON',           r';'),
        ('IDENTIFIER',          r'[a-zA-Z_]\w*'),
    ]

    LexicalAnalyzer = Analyzer(rules, open(inputfile, 'r').read())
    try:
        arr = []

        for token in LexicalAnalyzer.generate_token():
            arr.append([token.token_position, token.token_type, token.token_value])
            
        arr = np.array(arr)
        
        df = pd.DataFrame(arr, columns=['Position', 'Type', 'Value'])
        df.to_excel('output.xlsx', index = None, header = True)

    except UnknownToken as Error:
        print(Error)
        
if __name__ == '__main__':
    app()