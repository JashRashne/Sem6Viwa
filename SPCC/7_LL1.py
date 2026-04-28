from collections import defaultdict

EPSILON = 'ε'

# Input Grammar
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

        for prod in rhs.split("|"):
            grammar[lhs].append(prod.strip().split())

    return grammar, non_terminals


# Input FIRST sets
def input_first(non_terminals):
    first = {}
    print("\nEnter FIRST sets:")
    for nt in non_terminals:
        first[nt] = set(input(f"FIRST({nt}): ").split())
    return first


# Input FOLLOW sets
def input_follow(non_terminals):
    follow = {}
    print("\nEnter FOLLOW sets:")
    for nt in non_terminals:
        follow[nt] = set(input(f"FOLLOW({nt}): ").split())
    return follow


# Compute FIRST of a production
def first_of_string(prod, first):
    result = set()

    for symbol in prod:
        if symbol not in first:  # terminal
            result.add(symbol)
            return result
        result |= (first[symbol] - {EPSILON})
        if EPSILON not in first[symbol]:
            return result

    result.add(EPSILON)
    return result


# Construct LL(1) table
def construct_table(grammar, non_terminals, first, follow):
    table = defaultdict(dict)

    for nt in non_terminals:
        for prod in grammar[nt]:

            first_set = first_of_string(prod, first)

            for terminal in (first_set - {EPSILON}):
                table[nt][terminal] = " ".join(prod)

            if EPSILON in first_set:
                for terminal in follow[nt]:
                    table[nt][terminal] = "ε"

    return table


# MAIN
def main():
    grammar, non_terminals = read_grammar()
    first = input_first(non_terminals)
    follow = input_follow(non_terminals)

    table = construct_table(grammar, non_terminals, first, follow)

    print("\n----- LL(1) Parsing Table -----")
    for nt in table:
        for t in table[nt]:
            print(f"M[{nt}, {t}] = {nt} -> {table[nt][t]}")


if __name__ == "__main__":
    main()