from ast_nodes import Assign,Print,Variable
from lexer import TokenType
from ast_nodes import BinaryOp,Number

class Parser:
    def __init__(self,tokens):
        self.tokens=tokens
        self.pos=0
        self.current_token=self.token[self.pos] if tokens else None


    def advance(self):
        self.pos+=1
        if self.pos<len(self.tokens):
            self.current_token=self.tokens[self.pos]
        else:
            self.current_token=None

    def eat(self,token_type):
        if self.current_token and self.current_token.type==token_type:
            self.advance()
        else:
            raise Exception(f"Expected {token_type}, got {self.current_token}")

    def statement(self):
        if self.current_token.type == TokenType.IDENT:
            stmt=self.assignment()
            self.eat(TokenType.SEMICOLON)
            return stmt  
        
        elif self.current_token.type == TokenType.KEYWORD:
            stmt = self.print_stmt()
            self.eat(TokenType.SEMICOLON)
            return stmt
        
        else:
            raise Exception(f"Invalid statement starting with {self.current_token}")
        
    def assignment(self):
        name = self.current_token.value
        self.eat(TokenType.IDENT)
        self.eat(TokenType.ASSIGN)
        value = self.expression()
        return Assign(name, value)

    def print_stmt(self):
        self.eat(TokenType.KEYWORD)
        self.eat(TokenType.LPAREN)
        value = self.expression()
        self.eat(TokenType.RPAREN)
        return Print(value)
    
    def expression(self):
        left=self.term()
        while self.current_token and self.current_token.type == TokenType.PLUS:
            self.eat(TokenType.PLUS)
            right=self.term
            left=BinaryOp(left,"+",right)
            return left
        
    def term(self):
        token=self.current_token
        if token.type == TokenType.NUMBER:
            self.eat(TokenType.NUMBER)
            return Number(token.value)
        
        elif token.type == TokenType.IDENT:
                self.eat(TokenType.IDENT)
                return Variable(token.value)

        else:
            raise Exception(
            f"Unexpected token in expression: {token}"
            )       