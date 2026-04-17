from collections import OrderedDict

def left_factoring(grammar):
    while True:
        changed = False
        new_grammar = OrderedDict()

        for non_terminal in grammar:
            productions = grammar[non_terminal]
            grouped = {}

            # Group by first symbol
            for prod in productions:
                key = prod[0] if prod != 'ε' else 'ε'
                grouped.setdefault(key, []).append(prod)

            temp_productions = []

            for key in grouped:
                group = grouped[key]

                # If common prefix exists
                if len(group) > 1 and key != 'ε':
                    changed = True
                    new_nt = non_terminal + "'"

                    # Find longest common prefix
                    prefix = group[0]
                    for prod in group[1:]:
                        i = 0
                        while i < len(prefix) and i < len(prod) and prefix[i] == prod[i]:
                            i += 1
                        prefix = prefix[:i]

                    temp_productions.append(prefix + new_nt)

                    # Create new productions
                    new_prods = []
                    for prod in group:
                        remainder = prod[len(prefix):]
                        if remainder == "":
                            remainder = 'ε'
                        new_prods.append(remainder)

                    new_grammar[new_nt] = new_prods
                else:
                    temp_productions.extend(group)

            new_grammar[non_terminal] = temp_productions

        grammar = new_grammar
        if not changed:
            break

    return grammar


# Driver code
grammar = OrderedDict()
n = int(input("Enter number of productions: "))

for _ in range(n):
    rule = input("Enter production (A->...): ").replace(" ", "")
    lhs, rhs = rule.split("->")
    grammar[lhs] = rhs.split("|")

result = left_factoring(grammar)

print("\nGrammar after left factoring:")
for nt, prod in result.items():
    print(f"{nt} -> {' | '.join(prod)}")