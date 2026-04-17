id="symtbl01"
import re

# Size mapping (can be asked in viva)
type_size = {
    "int": 4,
    "float": 4,
    "double": 8,
    "char": 1
}

symbol_table = []

def process_line(line):
    line = line.strip().replace(";", "")

    # Match declarations like: int a, b, c
    match = re.match(r"(int|float|double|char)\s+(.+)", line)
    
    if match:
        dtype = match.group(1)
        variables = match.group(2).split(",")

        for var in variables:
            var = var.strip()

            symbol_table.append({
                "Name": var,
                "Type": dtype,
                "Size": type_size[dtype]
            })

def main():
    print("Enter source code (type END to stop):")

    while True:
        line = input()
        if line == "END":
            break
        process_line(line)

    print("\n----- SYMBOL TABLE -----")
    print("Name\tType\tSize")

    for entry in symbol_table:
        print(f"{entry['Name']}\t{entry['Type']}\t{entry['Size']}")

if __name__ == "__main__":
    main()