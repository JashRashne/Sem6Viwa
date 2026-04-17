import pandas as pd

# ---------------- PASS 1 ----------------
def first_pass(filename):
    mnt, mdt, ala = [], [], []
    mdt_index = 0
    in_macro = False
    ala_map = {}

    with open(filename, "r") as f, open("output1.txt", "w") as out:
        for line in f:
            line = line.strip()

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

                    mnt.append((name, mdt_index))

                    ala_pass1 = []
                    for i, p in enumerate(params, 1):
                        ala_map[p] = f"#{i}"
                        ala_pass1.append((i, ""))

                    continue

                # End of Macro
                if line == "MEND":
                    mdt.append((mdt_index, "MEND"))
                    mdt_index += 1
                    in_macro = False
                    ala_map = {}
                    continue

                # Replace parameters with index
                for p in ala_map:
                    line = line.replace(p, ala_map[p])

                mdt.append((mdt_index, line))
                mdt_index += 1

            else:
                out.write(line + "\n")

    return (pd.DataFrame(mnt, columns=["Macro", "MDT_Index"]),
            pd.DataFrame(mdt, columns=["Index", "Definition"]),
            pd.DataFrame(ala_pass1, columns=["Index", "Argument"]))


# ---------------- PASS 2 ----------------
def second_pass(filename, mnt, mdt):
    ala_pass2 = []

    with open(filename, "r") as f, open("output2.txt", "w") as out:
        for line in f:
            line = line.strip()
            if not line:
                continue

            parts = line.split()
            macro_call = parts[0]

            # If macro call
            if macro_call in mnt["Macro"].values:
                args = parts[1].split(",") if len(parts) > 1 else []
                ala_map = {f"#{i+1}": arg for i, arg in enumerate(args)}

                for i, arg in enumerate(args, 1):
                    ala_pass2.append((i, arg))

                start = int(mnt[mnt["Macro"] == macro_call]["MDT_Index"].values[0])
                i = start

                while mdt.iloc[i]["Definition"] != "MEND":
                    inst = mdt.iloc[i]["Definition"]

                    for key in ala_map:
                        inst = inst.replace(key, ala_map[key])

                    out.write(inst + "\n")
                    i += 1

            else:
                out.write(line + "\n")

    return pd.DataFrame(ala_pass2, columns=["Index", "Argument"])


# ---------------- MAIN ----------------
def main():
    filename = "input.txt"

    mnt, mdt, ala1 = first_pass(filename)

    print("\n----- MNT (Macro Name Table) -----")
    print(mnt)

    print("\n----- MDT (Macro Definition Table) -----")
    print(mdt)

    print("\n----- ALA (Pass 1) -----")
    print(ala1)

    print("\n----- Output File (output1.txt) -----")
    print(open("output1.txt").read())

    ala2 = second_pass("output1.txt", mnt, mdt)

    print("\n----- ALA (Pass 2) -----")
    print(ala2)

    print("\n----- Output File (output2.txt) -----")
    print(open("output2.txt").read())


if __name__ == "__main__":
    main()