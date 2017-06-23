
def write():
    adress = raw_input("Indique o endereco de 4 bits: ")
    value = raw_input("Indique o valor de 8 bits : ")

    slots[adress.zfill(4)] = value.zfill(8)


def read():
	adress = raw_input("Indique o endereco de 4 bits: ")
        print slots[adress.zfill(4)]

slots = {}

for i in range(0, 16):
    	slots[bin(i)[2:].zfill(4)] = "00000000"
