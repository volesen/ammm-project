import re
from typing import TextIO

scanner = re.Scanner(
    [
        # Whitespace
        (r"\s+", None),
        # Line comments
        (r"//.*", None),
        # Numbers (integers for now)
        (r"\d+", lambda scanner, token: ("INTEGER", int(token))),
        # Operators
        (r"=", lambda scanner, token: ("ASSIGN", token)),
        # Delimiters
        (r"\[", lambda scanner, token: ("LBRACKET", token)),
        (r"\]", lambda scanner, token: ("RBRACKET", token)),
        # Semicolon
        (r";", lambda scanner, token: ("SEMICOLON", token)),
        # Identifiers
        (r"[a-zA-Z_][a-zA-Z0-9_]*", lambda scanner, token: ("IDENTIFIER", token)),
    ]
)


class Parser:
    tokens: list
    current: int

    def __init__(self, tokens: list):
        self.tokens = tokens
        self.current = 0

    def parse(self):
        return self.parse_assignments()

    def parse_assignments(self):
        assignments = {}

        while not self.is_at_end():
            assignments.update(self.parse_assignment())

        return assignments

    def parse_assignment(self):
        identifier = self.parse_identifier()
        self.consume("ASSIGN")
        value = self.parse_value()
        self.consume("SEMICOLON")

        return {identifier: value}

    def parse_identifier(self):
        return self.consume("IDENTIFIER")[1]

    def parse_value(self):
        if self.match("LBRACKET"):
            return self.parse_list()
        else:
            return self.parse_number()

    def parse_number(self):
        return self.consume("INTEGER")[1]

    def parse_list(self):
        values = []

        while not self.match("RBRACKET"):
            values.append(self.parse_value())

        return values

    def is_at_end(self):
        return self.current >= len(self.tokens)

    def match(self, token_type):
        if self.is_at_end():
            return False

        if self.tokens[self.current][0] != token_type:
            return False

        self.current += 1

        return True

    def consume(self, token_type):
        if self.is_at_end():
            raise SyntaxError(f"Expected {token_type}, found EOF")

        token = self.tokens[self.current]

        if token[0] != token_type:
            raise SyntaxError(f"Expected {token_type}, found {token[0]}")

        self.current += 1

        return token


def parse(dat_file: TextIO):
    tokens, _ = scanner.scan(dat_file.read())
    parser = Parser(tokens)

    return parser.parse()
