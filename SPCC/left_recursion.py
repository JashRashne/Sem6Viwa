from collections import OrderedDict

def remove_left_recursion(grammar):
    new_grammar = OrderedDict()

    for non_terminal, productions in grammar.items():
        alpha = []   # left-recursive parts
        beta = []    # non-left-recursive parts

        for prod in productions:
            if prod.startswith(non_terminal):
                alpha.append(prod[len(non_terminal):])
            else:
                beta.append(prod)

        # If no left recursion
        if not alpha:
            new_grammar[non_terminal] = productions
            continue

        # Create new non-terminal
        new_nt = non_terminal + "'"

        # A → βA'
        new_grammar[non_terminal] = [b + new_nt for b in beta]

        # A' → αA' | ε
        new_grammar[new_nt] = [a + new_nt for a in alpha] + ['ε']

    return new_grammar


# Driver code
grammar = OrderedDict()
n = int(input("Enter number of productions: "))

for _ in range(n):
    rule = input("Enter production (A->...): ").replace(" ", "")
    lhs, rhs = rule.split("->")
    grammar[lhs] = rhs.split("|")

result = remove_left_recursion(grammar)

print("\nGrammar after removing left recursion:")
for nt, prod in result.items():
    print(f"{nt} -> {' | '.join(prod)}")