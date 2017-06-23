def write():
    adress = input("Indique um endereço de 4 bits: ")
    value = input("Indique o valor de 8 bits: ")

    slots[adress.zfill(4)] = value.zfill(8)


def read():
    adress = input("Indique um endereco de 4 bits: ")
    print(slots[adress.zfill(4)])


slots = {}

for i in range(0, 15):
    slots[bin(i)[2:].zfill(4)] = "00000000"