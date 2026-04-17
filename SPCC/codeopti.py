import re

def optimize_code(code_lines):
    optimized = []
    values = {}

    for line in code_lines:
        line = line.strip()

        # Remove spaces
        if not line:
            continue

        # Match assignment
        match = re.match(r"(\w+)\s*=\s*(.+)", line)

        if match:
            var = match.group(1)
            expr = match.group(2)

            # Constant folding (e.g., 2 + 3)
            try:
                value = eval(expr)
                values[var] = value
                optimized.append(f"{var} = {value}")
                continue
            except:
                pass

            # Constant propagation
            for v in values:
                expr = expr.replace(v, str(values[v]))

            # Algebraic simplification
            expr = expr.replace("*1", "")
            expr = expr.replace("1*", "")
            expr = expr.replace("+0", "")
            expr = expr.replace("0+", "")

            optimized.append(f"{var} = {expr}")

        else:
            optimized.append(line)

    return optimized


# MAIN
def main():
    print("Enter code (type END to stop):")
    code_lines = []

    while True:
        line = input()
        if line == "END":
            break
        code_lines.append(line)

    optimized = optimize_code(code_lines)

    print("\n----- Optimized Code -----")
    for line in optimized:
        print(line)


if __name__ == "__main__":
    main()