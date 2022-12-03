from sly import Lexer

import re

def group(*choices): return '(' + '|'.join(choices) + ')'
def any(*choices): return group(*choices) + '*'
def maybe(*choices): return group(*choices) + '?'

# Numbers
Hexnumber = r'0[xX](?:_?[0-9a-fA-F])+'
Binnumber = r'0[bB](?:_?[01])+'
Octnumber = r'0[oO](?:_?[0-7])+'
Decnumber = r'(?:0(?:_?0)*|[1-9](?:_?[0-9])*)'
Exponent = r'[eE][-+]?[0-9](?:_?[0-9])*'
Pointfloat = group(r'[0-9](?:_?[0-9])*\.(?:[0-9](?:_?[0-9])*)?',
                   r'\.[0-9](?:_?[0-9])*') + maybe(Exponent)
Expfloat = r'[0-9](?:_?[0-9])*' + Exponent

# Hashes
#MD5Hash = r'(?i)(?<![a-z0-9])[a-f0-9]{32}(?![a-z0-9])'
# ...

class PLexer(Lexer):
    tokens = {
        NAME, 
        NUMBER,
        #HASH, 
        STRING, 
        FLOAT, 
        PLUS, 
        MINUS,
        DIVIDE,
        LPAREN, 
        RPAREN, 
        LBRACE, 
        RBRACE, 
        LT, 
        LE, 
        GT, 
        GE,
        EQ, 
        EQEQ, 
        NE, 
        IF, 
        ELSE, 
        DEF,
        STRUCT,
        RETURN,
        TIMES,
        COLON,
        MOD,
        WHILE, 
        UNTIL, 
        BREAK, 
        CONTINUE,
        AND, 
        OR, 
        COMMA,
        LSHIFT,
        RSHIFT,
        OR,
        AND,
        XOR
    }

    
    ###########################################################################
    #   Match Multiple Flavours of Comments, Multi-Line too                   #
    ###########################################################################

    # Python Style Comments
    @_(r'#.*')
    def HASH_SINGLE_COMMENT(self, t):
        pass
   
    # C Style Comments
    @_(r'//.*')
    def SLASH_SINGLE_COMMENT(self, t):
        pass

    # C Style Comments *
    @_(r'/\*.*?\*/')
    def SLASHSTAR_SINGLE_COMMENT(self, t):
        pass

    # C++ Style Comments
    @_(r'\/\*+((([^\*])+)|([\*]+(?!\/)))[*]+\/')
    def SLASHSTAR_MULTI_COMMENT(self, t):
        pass

    literals = {',',';'}

    FLOAT = group(Pointfloat, Expfloat)
    
    NUMBER = group(
                Hexnumber, 
                Binnumber, 
                Octnumber, 
                Decnumber
            )

    #HASH = group(
    #            MD5Hash
    #        )

    ignore = ' \t\r'
    @_(r'\n')
    def newline(self,t ):
        self.lineno += 1

    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NAME['if'] = IF
    NAME['else'] = ELSE
    
    # Def Synonyms
    NAME['def'] = DEF
    NAME['function'] = DEF
    NAME['sub'] = DEF
    NAME['func'] = DEF
    NAME['subroutine'] = DEF

    NAME['struct'] = STRUCT
    NAME['return'] = RETURN
    NAME['while'] = WHILE
    NAME['until'] = UNTIL
    NAME['break'] = BREAK
    NAME['continue'] = CONTINUE
    NAME['and'] = AND
    NAME['or'] = OR
    STRING = r'(\".*?\")|(\'.*?\')'
    LSHIFT = r'<<'
    RSHIFT = r'>>'
    OR = r'\|'
    AND = r'\&'
    XOR = r'\^'
    GE = r'>='
    GT = r'>'
    LE = r'<='
    LT = r'<'
    NE = r'!='
    EQEQ = r'=='
    EQ = r'='
    LBRACE = r'\{'
    RBRACE = r'\}'
    LPAREN = r'\('
    RPAREN = r'\)'
    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    MOD = r'%'
    COLON = r':'


    def error(self, t):
        print(f'Illegal character {t.value[0]}, in line {self.lineno}, index {self.index}')
        exit()
