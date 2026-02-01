from dataclasses import dataclass
from typing import List


class AST:
    pass


class Statement(AST):
    pass


class Expression(AST):
    pass


@dataclass
class Program(AST):
    statements: List[Statement]


@dataclass
class Assign(Statement):
    name: str
    value: Expression


@dataclass
class Print(Statement):
    value: Expression


@dataclass
class BinaryOp(Expression):
    left: Expression
    op: str
    right: Expression


@dataclass
class Number(Expression):
    value: int


@dataclass
class Variable(Expression):
    name: str
