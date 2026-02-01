from enum import Enum,auto

class TokenType(Enum):
    IDENT=auto()
    NUMBER=auto()
    PLUS=auto()
    LPAREN=auto()
    RPAREN=auto()
    KEYWORD=auto()
    SEMICOLON=auto()  
    ASSIGN = auto()

class Token: 
    def __init__(self,_type,value=None):
        self.type=_type
        self.value=value

    def __repr__(self):   #replicate object and debug object
        return f"{self.type.name}:{self.value}"
    
class Lexer: 
    def __init__(self,text):
        self.text=text
        self.pos=0
        self.current_char=self.text[self.pos] if text else None

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char=self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char in " \t\n":
            self.advance()

    def read_identifier(self):
        result=""
        while self.current_char is not None and self.current_char.isalnum():
            result+=self.current_char
            self.advance()
        if result == "hydro":
            return Token(TokenType.KEYWORD, result)
        else:
            return Token(TokenType.IDENT, result)
        
    def read_number(self):
        result=""
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return Token(TokenType.NUMBER, int(result))

    def get_next_token(self):
        while self.current_char is not None:

            if self.current_char in " \t\n":
                self.skip_whitespace()
                continue

            if self.current_char.isalpha():
                return self.read_identifier()
            
            if self.current_char.isdigit():
                return self.read_number()
            
            if self.current_char == "=":
                self.advance()
                return  Token(TokenType.ASSIGN,'=')
            
            if self.current_char == '+':
                self.advance()
                return Token(TokenType.PLUS, '+')

            if self.current_char == '(':
                self.advance()
                return Token(TokenType.LPAREN, '(')

            if self.current_char == ')':
                self.advance()
                return Token(TokenType.RPAREN, ')')

            if self.current_char == ';':
                self.advance()
                return Token(TokenType.SEMICOLON, ';')
            
            raise Exception(f"Illegal character: {self.current_char}")
        
        return None
    
    def tokenize(self):
        tokens=[]

        while True:
            token=self.get_next_token()
            if token is None:
                break
            tokens.append(token)

        return tokens
            
with open(r"furina.txt", "r") as f:
    source_code = f.read()

print("RAW CHAR CODES (before):")
print([ord(c) for c in source_code])

source_code = source_code.replace('\r', '')
print("SOURCE CODE READ:")
print(repr(source_code))

lexer = Lexer(source_code)
tokens = lexer.tokenize()

print("\nTOKENS:")
for token in tokens:
    print(token)
