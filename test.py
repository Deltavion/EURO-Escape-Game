from random import randint
from time import sleep

numbers = range(48, 58)
letters = range(97, 103)
chars = [chr(n) for n in (*numbers, *letters)]

symb = ["\\", "|", "/", "-"]

def delay_print(strings):
	text = ""
	for char in strings:
		text += char
		print(text, end='\r')
		sleep(0.000001)

text = "Decrypting bypass key - [--------------------]"
liste = [char for char in text]
print("".join(liste), end="\r")
for i in range(40):
	liste[22] = symb[int(i%4)]
	if i%2 == 0:
		liste[25+int(i/2)] = "#"
	print("".join(liste), end="\r")
	sleep(0.1)


	
	