from collections import defaultdict

EPSILON = 'ε'

# Read grammar
def read_grammar():
    grammar = defaultdict(list)
    non_terminals = []

    n = int(input("Enter number of productions: "))

    for _ in range(n):
        line = input("Enter production (A->...): ").strip()
        lhs, rhs = line.split("->")
        lhs = lhs.strip()

        if lhs not in non_terminals:
            non_terminals.append(lhs)

        productions = rhs.split("|")
        for prod in productions:
            grammar[lhs].append(prod.strip().split())

    return grammar, non_terminals


# Take FIRST sets as input
def input_first_sets(non_terminals):
    first = {}

    print("\nEnter FIRST sets (space separated, use ε for epsilon):")
    for nt in non_terminals:
        values = input(f"FIRST({nt}): ").split()
        first[nt] = set(values)

    return first


# Compute FOLLOW
def compute_follow(grammar, non_terminals, first):
    follow = {nt: set() for nt in non_terminals}

    # Start symbol gets $
    follow[non_terminals[0]].add('$')

    changed = True
    while changed:
        changed = False

        for nt in non_terminals:
            for production in grammar[nt]:
                trailer = follow[nt].copy()

                for symbol in reversed(production):
                    if symbol in non_terminals:
                        before = len(follow[symbol])

                        follow[symbol] |= trailer

                        if EPSILON in first[symbol]:
                            trailer |= (first[symbol] - {EPSILON})
                        else:
                            trailer = first[symbol].copy()

                        if len(follow[symbol]) > before:
                            changed = True
                    else:
                        trailer = {symbol}

    return follow


# MAIN
def main():
    grammar, non_terminals = read_grammar()

    first = input_first_sets(non_terminals)

    follow = compute_follow(grammar, non_terminals, first)

    print("\nFOLLOW sets:")
    for nt in non_terminals:
        print(f"{nt}: {sorted(follow[nt])}")


if __name__ == "__main__":
    main()