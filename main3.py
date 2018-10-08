from ram3 import memoryram

ram3 = memoryram()
op = "R"

while op in ("RWLrwl"):

    op = input("Digite W para escrever, R para ler, L para listar toda a memoria  e qualquer tecla para parar. \n")

    if op == "R" or op == "r":
        ram3.read()
    if op == "W" or op =="w":
        ram3.write()
    if op == "L" or op == "l":
        for i in sorted(ram3.slots):
            print(i, ram3.slots[i])

