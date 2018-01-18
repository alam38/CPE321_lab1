# Name: Andrew Lam
# Course: CPE-321
# Instructor: Zachary Peterson
# Assignment: Lab 1
# Term: Winter 2018

def Xor(string1, string2):
	if len(string1) != len(string2):
		print("The length of the two strings are not equal")
		return
	else:
		return ''.join('{:02x}'.format(ord(a)^ord(b), 'x') for a,b in zip(string1, string2))
		

def main():
	print(Xor('Darlin dont you go', 'and cut your hair!'))

if __name__ == "__main__":
	main()
