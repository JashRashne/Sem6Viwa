grammar = {}
first = {}
follow = {}
table = {}

# -------- INPUT --------
n = int(input("Enter number of productions: "))
print("Enter productions:")

for _ in range(n):
    line = input()
    left, right = line.split("->")
    grammar[left] = right.split("|")

for nt in grammar:
    first[nt] = set()
    follow[nt] = set()

start = list(grammar.keys())[0]
follow[start].add("$")


# -------- FIRST --------
def find_first(symbol):

    if symbol not in grammar:
        return {symbol}

    if len(first[symbol]) != 0:
        return first[symbol]

    for prod in grammar[symbol]:

        if prod == "ε":
            first[symbol].add("ε")

        else:
            for ch in prod:
                temp = find_first(ch)

                first[symbol] |= (temp - {"ε"})

                if "ε" not in temp:
                    break
            else:
                first[symbol].add("ε")

    return first[symbol]


for nt in grammar:
    find_first(nt)


# -------- FOLLOW --------
changed = True

while changed:
    changed = False

    for head in grammar:
        for prod in grammar[head]:

            for i in range(len(prod)):

                if prod[i] in grammar:

                    before = len(follow[prod[i]])

                    if i + 1 < len(prod):
                        next_symbol = prod[i + 1]

                        temp = find_first(next_symbol)

                        follow[prod[i]] |= (temp - {"ε"})

                        if "ε" in temp:
                            follow[prod[i]] |= follow[head]

                    else:
                        if prod[i] != head:
                            follow[prod[i]] |= follow[head]

                    if len(follow[prod[i]]) > before:
                        changed = True


# -------- PRINT FIRST --------
print("\nFIRST Sets:")
for nt in first:
    print("FIRST({}) = {}".format(nt, first[nt]))


# -------- PRINT FOLLOW --------
print("\nFOLLOW Sets:")
for nt in follow:
    print("FOLLOW({}) = {}".format(nt, follow[nt]))


# -------- BUILD TABLE --------
terminals = set()

for head in grammar:
    for prod in grammar[head]:
        for ch in prod:
            if ch not in grammar and ch != "ε":
                terminals.add(ch)

terminals.add("$")
terminals = sorted(terminals)

for nt in grammar:
    table[nt] = {}
    for t in terminals:
        table[nt][t] = ""


for head in grammar:

    for prod in grammar[head]:

        first_prod = set()

        if prod == "ε":
            first_prod.add("ε")

        else:
            for ch in prod:

                temp = find_first(ch)

                first_prod |= (temp - {"ε"})

                if "ε" not in temp:
                    break
            else:
                first_prod.add("ε")

        for t in first_prod:
            if t != "ε":
                table[head][t] = prod

        if "ε" in first_prod:
            for f in follow[head]:
                table[head][f] = "ε"


# -------- PRINT TABLE --------
print("\nLL(1) Parsing Table:\n")

print("{:10}".format(""), end="")
for t in terminals:
    print("{:10}".format(t), end="")
print()

for nt in grammar:
    print("{:10}".format(nt), end="")

    for t in terminals:
        entry = table[nt][t]
        print("{:10}".format(entry), end="")

    print()


# -------- STACK PARSER --------
string = input("\nEnter input string: ") + "$"

stack = ["$", start]
pointer = 0

print("\nStack\t\tInput\t\tAction")

while stack:

    top = stack[-1]
    current = string[pointer]

    print("{:15}{:15}".format("".join(stack), string[pointer:]), end="")

    if top == current:
        stack.pop()
        pointer += 1
        print("Match")

    elif top in grammar:

        entry = table[top][current]

        if entry == "":
            print("Error")
            print("\nString Rejected")
            break

        stack.pop()

        if entry != "ε":
            for ch in reversed(entry):
                stack.append(ch)

        print("{}->{}".format(top, entry))

    else:
        print("Error")
        print("\nString Rejected")
        break

    if stack == ["$"] and string[pointer] == "$":
        print("\nString Accepted")
        break

