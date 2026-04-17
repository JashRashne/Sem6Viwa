import pandas as pd

def first_pass(filename):
    mnt = []   # Macro Name Table
    mdt = []   # Macro Definition Table
    ala = []   # Argument List Array

    mdt_index = 0
    in_macro = False
    ala_map = {}

    with open(filename, "r") as f, open("output1.txt", "w") as out:
        for line in f:
            line = line.strip()

            # Start of macro
            if line == "MACRO":
                in_macro = True
                ala_map = {}
                continue

            if in_macro:

                # Macro Header
                if not ala_map:
                    parts = line.split()
                    name = parts[0]
                    params = parts[1].split(",") if len(parts) > 1 else []

                    # Add to MNT
                    mnt.append((name, mdt_index))

                    # Build ALA (Pass 1)
                    ala = []
                    for i, p in enumerate(params, 1):
                        ala_map[p] = f"#{i}"
                        ala.append((i, ""))   # blank arguments

                    continue

                # End of macro
                if line == "MEND":
                    mdt.append((mdt_index, "MEND"))
                    mdt_index += 1
                    in_macro = False
                    ala_map = {}
                    continue

                # Replace parameters with positional notation
                for p in ala_map:
                    line = line.replace(p, ala_map[p])

                # Add to MDT
                mdt.append((mdt_index, line))
                mdt_index += 1

            else:
                # Write non-macro lines to output1.txt
                out.write(line + "\n")

    return (pd.DataFrame(mnt, columns=["Macro", "MDT_Index"]),
            pd.DataFrame(mdt, columns=["Index", "Definition"]),
            pd.DataFrame(ala, columns=["Index", "Argument"]))


# ---------------- MAIN ----------------
def main():
    filename = "input.txt"

    mnt, mdt, ala = first_pass(filename)

    print("\n----- MNT (Macro Name Table) -----")
    print(mnt)

    print("\n----- MDT (Macro Definition Table) -----")
    print(mdt)

    print("\n----- ALA (Pass 1) -----")
    print(ala)

    print("\n----- Output File (output1.txt) -----")
    with open("output1.txt", "r") as f:
        print(f.read())


if __name__ == "__main__":
    main()