from ram import memoryram

ram = memoryram()

op = "R"

while op in ("RWLrwl"):

    op = raw_input ("Digite W para escrever, R para ler, L para listar toda a memoria  e qualquer tecla para parar. \n")

    if op == "R" or op == "r":
        ram.read()
    if op == "W" or op == "w":
        ram.write()
    if op == "L" or op == "l":
        for i in sorted(ram.slots):
            print i, ram.slots[i]
