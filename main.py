import os.path
from time import sleep
import keyboard
from random import randint

def get_disks():
	disks_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	connected_disks = ['%s:' % d for d in disks_list if os.path.exists('%s:' % d)]
	return connected_disks

def detect_disk(last_disks, curr_disks):
	connected = [item for item in curr_disks if item not in last_disks]
	disconnected = [item for item in last_disks if item not in curr_disks]
	if connected:
		return True
	return False

def matrix(n):
	text = ""
	for i in range(n):
		text += chars[randint(0, len(chars)-1)]
	return text

def enter_root():
	pw = input("enter admin password : ") 
	if pw == "123456":
		return True
	print("process failed")
	return False

def styled_print(str):
	l = len(str)
	for i in range(l*3):
		print(f"\r{matrix(l)}", end="")
		sleep(0.2)

def decrypt():
	symb = ["\\", "|", "/", "-"]
	text = "Decrypting bypass key - [--------------------]"
	liste = [char for char in text]
	delay_print("".join(liste), False)
	for i in range(40):
		liste[22] = symb[int(i%4)]
		if i%2 == 0:
			liste[25+int(i/2)] = "#"
		print("".join(liste), end="\r")
		sleep(0.1)

def delay_print(strings, p):
	text = ""
	for char in strings:
		text += char
		print(text, end='\r')
		sleep(0.000001)
	if p:
		print()
	

numbers = range(48, 58)
letters = range(97, 103)
chars = [chr(n) for n in (*numbers, *letters)]

last_disks = get_disks()
curr_disks = get_disks()

path = "restricted"
usb = False

running = True
while running:
	print()
	cmd = input(f"{path}/>")
	
	if cmd == "root":
		success = enter_root()
		if success:
			path = "root"
		
	elif cmd == "open door":
		if path == "root":
			curr_disks = get_disks()
			usb = detect_disk(last_disks, curr_disks)
			last_disks = curr_disks
			if usb:
				decrypt()
				print()
				delay_print("door unlocked", True)
			else:
				delay_print("bypass key not detected, insert it", True)
		else:
			delay_print("command not available, root only", True)

	elif cmd == "quit":
		break

	elif cmd == "":
		pass

	else:
		delay_print("ERROR 481646184971786178", True)