import ram3

op = "R"

while op in ("RWLrwl"):

    op = upper(input("Digite W para escrever, R para ler, L para listar toda a memoria e qualquer tecla para parar. \n"))

    if op == "R":
        ram3.read()
    if op == "W":
        ram3.write()
    if op == "L:
        for i in sorted(ram3.slots):
            print(i, ram3.slots[i])

