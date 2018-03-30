# -*-coding:UTF-8-*-
import random, string


class GenRcode():
	
	def genrcode():
		chars = string.letters + string.digits
		s = "".join(random.choice(chars) for i in range(10))
		t = "".join(random.sample(chars, 10))
		rcode = s + " ******** " + t
		return rcode
	genrcode = staticmethod(genrcode)

if __name__ == "__main__":
	rcode = []
	for i in range(200):
		rcode.append(GenRcode.genrcode())
	for l in rcode:
		print l + "\n"

