import re

# Token types
KEYWORDS = {"if", "else", "while", "for", "float", "int"}
OPERATORS = r"[+\-*/=<>!]"
PUNCTUATION = r"[.,;(){}]"

def tokenize(code):
    tokens = []
    i = 0

    while i < len(code):
        char = code[i]

        # Skip whitespace
        if char.isspace():
            i += 1
            continue

        # Keywords / Identifiers
        if char.isalpha() or char == "_":
            match = re.match(r"[a-zA-Z_][a-zA-Z0-9_]*", code[i:])
            value = match.group()

            if value in KEYWORDS:
                tokens.append(("KEYWORD", value))
            else:
                tokens.append(("IDENTIFIER", value))

            i += len(value)

        # Numbers (Literals)
        elif char.isdigit():
            match = re.match(r"\d+", code[i:])
            value = match.group()
            tokens.append(("LITERAL", value))
            i += len(value)

        # Operators
        elif re.match(OPERATORS, char):
            tokens.append(("OPERATOR", char))
            i += 1

        # Punctuation
        elif re.match(PUNCTUATION, char):
            tokens.append(("PUNCTUATION", char))
            i += 1

        else:
            tokens.append(("UNKNOWN", char))
            i += 1

    return tokens


# Main
code = "float interest = p*n*r;"
tokens = tokenize(code)

for token in tokens:
    print(token)