import re

class LexerError(Exception):
    pass

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]
    
    def error(self):
        raise LexerError("Invalid syntax")

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def skip_comment(self):
        while self.current_char != "\n":
            self.advance()
        self.advance()

    def integer(self):
        result = ""
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def identifier(self):
        result = ""
        while self.current_char is not None and self.current_char.isalnum():
            result += self.current_char
            self.advance()
        return result

    def string(self):
        result = ""
        self.advance()
        while self.current_char != '"':
            if self.current_char is None:
                self.error()
            result += self.current_char
            self.advance()
        self.advance()
        return result

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char == "#":
                self.skip_comment()
                continue

            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())

            if self.current_char.isalpha():
                return Token(IDENTIFIER, self.identifier())

            if self.current_char == '"':
                return Token(STRING, self.string())

            if self.current_char == ":":
                self.advance()
                return Token(COLON, ":")

            if self.current_char == "{":
                self.advance()
                return Token(LBRACE, "{")

            if self.current_char == "}":
                self.advance()
                return Token(RBRACE, "}")

            self.error()

        return Token(EOF, None)
