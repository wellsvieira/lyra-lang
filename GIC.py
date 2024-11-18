'''
Program   : Body
          | Declares Body
          | Declares

Declares  : Declare
          | Declares Declare

Declare   : INT NAME
          | INT NAME ATR NUM
          | ARRAY NAME LSBRACKET NUM RSBRACKET
          | ARRAY NAME LSBRACKET NUM RSBRACKET ATR LPAREM List RPAREM 
          | MATRIX NAME LSBRACKET NUM RSBRACKET LSBRACKET NUM RSBRACKET
          | MATRIX NAME LSBRACKET NUM RSBRACKET LSBRACKET NUM RSBRACKET ATR LPAREM ListOfLists RPAREM

List      : NUM COMMA List
          | NUM

ListOfLists : List 
            | ListOfLists COMMA List

Body      : Statement
          | Body Statement

Statement : Attribution
          | If
          | While
          | Write


Attribution : NAME ATR Expression
            | NAME LSBRACKET Expression RSBRACKET ATR Expression
            | NAME LSBRACKET Expression LSBRACKET Expression RSBRACKET ATR Expression
            | NAME ATR READ
            | NAME LSBRACKET Expression RSBRACKET ATR READ
            | NAME LSBRACKET Expression LSBRACKET Expression RSBRACKET ATR READ

If        : IF LPAREN Condition RPAREN THEN Body END
          | IF LPAREN Condition RPAREN THEN Body ELSE Body END

While     : WHILE LPAREN Condition RPAREN DO Body END

Write     : WRITES LPAREN STRING RPAREN
          | WRITEI LPAREN Expression RPAREN


Expression: Term
          | Expression ADD Term
          | Expression SUB Term
          | Expression OR Term

Term      : Factor
          | Term MULT Factor
          | Term DIV Factor
          | Term MOD Factor
          | Term AND Factor

Factor    : NUM
          | Variable
          | LPAREN Expression RPAREN
          | NOT LPAREN Condition RPAREN

Condition : Expression GREATER Expression
          | Expression LESS Expression
          | Expression GREATERE Expression
          | Expression LESSE Expression
          | Expression EQUAL Expression
          | Expression NEQUAL Expression

Variable  : NAME LSBRACKET Expression RSBRACKET
          | NAME LSBRACKET Expression RSBRACKET LSBRACKET Expression RSBRACKET
          | NAME


Variable  : NAME LSBRACKET Expression RSBRACKET
          | NAME LSBRACKET Expression RSBRACKET LSBRACKET Expression RSBRACKET
          | NAME
          '''
