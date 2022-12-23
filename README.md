# The Lexical Analyzer
This Analyzer gets Input.txt input file of source code and generates tokens in Output.xlsx Excel file. (Each token in one cell and its corresponding token type in other cell)


* ### How to run "The Lexical Analyzer"?
  Open a new terminal and type command below
  
  ``` 
  $ python3 LexicalAnalyzer.py input.txt
  ```

* ### In what way The Output is structured?
  Token positions are placed in the first column. In the second column, you will find the type of token. The third column shows the value of that             token.
  
  | Position      | Type          | Value                              |
  | ------------- |:-------------:| ---------------------------------- |
  | 0             | COMMENT       | # Program make a simple calculator |
  | 36            | COMMENT       | # This function adds two numbers   |
  | 69            | IDENTIFIER    | def                                |


* ### What if "The Lexical Analyzer" doesn't recognize a token?
  The Lexical Analyzer displays the structure above when recognizing a token. Lexical Analyzer, however, displays the message "Lexical Analyzer Error:       Unknown Token" whenever it cannot recognize a token.
