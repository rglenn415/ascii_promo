from time import sleep


def main():
	while True:
		with open('rush.txt','r') as file:
			for line in file:
				# Removes the newline at end of each print statement
				print(line, end='')
				sleep(.06)


if __name__ == '__main__':
	main()