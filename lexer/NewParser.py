class ParserError(Exception):
    pass

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise ParserError("Invalid syntax")

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def block(self):
        statements = []
        while self.current_token.type != RBRACE and self.current_token.type != EOF:
            statements.append(self.statement())
        self.eat(RBRACE)
        return Block(statements)

    def factor(self):
        token = self.current_token
        if token.type == INTEGER:
            self.eat(INTEGER)
            return IntegerLiteral(token.value)
        elif token.type == LPAREN:
            self.eat(LPAREN)
            node = self.expr()
            self.eat(RPAREN)
            return node
        else:
            self.error()

    def term(self):
        node = self.factor()

        while self.current_token.type in (MULTIPLY, DIVIDE):
            token = self.current_token
            if token.type == MULTIPLY:
                self.eat(MULTIPLY)
            elif token.type == DIVIDE:
                self.eat(DIVIDE)

            node = BinaryOperator(left=node, operator=token, right=self.factor())

        return node

    def expr(self):
        node = self.term()

        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
            elif token.type == MINUS:
                self.eat(MINUS)

            node = BinaryOperator(left=node, operator=token, right=self.term())

        return node

    def statement(self):
        if self.current_token.type == IDENTIFIER:
            identifier = self.current_token
            self.eat(IDENTIFIER)
            self.eat(ASSIGN)
            value = self.expr()
            return Assignment(identifier, value)
        elif self.current_token.type == PRINT:
            self.eat(PRINT)
            value = self.expr()
            return Print(value)
        elif self.current_token.type == LBRACE:
            return self.block()
        else:
            self.error()

    def parse(self):
        node = self.block()
        if self.current_token.type != EOF:
            self.error()

        return node
