from collections import defaultdict

EPSILON = 'ε'

def read_grammar(filename):
    grammar = defaultdict(list)
    non_terminals = []

    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            lhs, rhs = line.split("->")
            lhs = lhs.strip()
            if lhs not in non_terminals:
                non_terminals.append(lhs)
            productions = rhs.split("|")
            for prod in productions:
                grammar[lhs].append(prod.strip().split())

    return grammar, non_terminals


def compute_first(grammar, non_terminals):
    first = {nt: set() for nt in non_terminals}

    changed = True
    while changed:
        changed = False
        for nt in non_terminals:
            for production in grammar[nt]:
                i = 0
                add_epsilon = True

                while i < len(production):
                    symbol = production[i]

                    if symbol not in grammar:  # terminal
                        if symbol not in first[nt]:
                            first[nt].add(symbol)
                            changed = True
                        add_epsilon = False
                        break

                    else:
                        before = len(first[nt])
                        first[nt] |= (first[symbol] - {EPSILON})
                        if EPSILON not in first[symbol]:
                            add_epsilon = False
                            break
                        if len(first[nt]) > before:
                            changed = True

                    i += 1

                if add_epsilon:
                    if EPSILON not in first[nt]:
                        first[nt].add(EPSILON)
                        changed = True

    return first


def main():
    grammar, non_terminals = read_grammar("grammar.txt")
    first = compute_first(grammar, non_terminals)

    print("\nFIRST sets:")
    for nt in non_terminals:
        print(f"{nt}: {sorted(first[nt])}")



if __name__ == "__main__":
    main()
