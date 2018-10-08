class memoryram:

	def __init__(self):
		self.slots = {}
		for i in range(0, 16):
			self.slots[bin(i)[2:].zfill(4)] = "00000000"

	def write(self):
	    adress = raw_input("Indique o endereco de 4 bits: ")
	    value = raw_input("Indique o valor de 8 bits : ")

	    self.slots[adress.zfill(4)] = value.zfill(8)


	def read(self):
		adress = raw_input("Indique o endereco de 4 bits: ")
		print self.slots[adress.zfill(4)]
