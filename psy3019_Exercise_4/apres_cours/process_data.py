import numpy as np

matrice = np.array([
"###################################################",
"#  _     _                    _                   #",
"# | |   (_)                  | |              /   #",
"# | |__  _  ___ _ __         | | ___  _   _  __   #",
"# | '_ \\| |/ _ \\ '_ \\    _   | |/ _ \\| | | |/ _ \\ #",
"# | |_) | |  __/ | | |  | |__| | (_) | |_| |  __/ #",
"# |_.__/|_|\\___|_| |_|   \\____/ \\___/ \\__,_|\\___| #",
"#                                                 #",
"###################################################"
], dtype=str)

for i, line in enumerate(matrice):
    random_line = '1234r2345234r234f23rfnewinrfc²ienr²jrf'
    f = open(f"resultat{i+1}.txt", "x")
    f.write(line)
    f.write("\n")
    f.write(random_line)
    f.close()

    