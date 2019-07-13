import sys

def somar(n1, n2):
	return n1 + n2

def main():
	
	arg1  = int(sys.argv[1])
	arg2 = int(sys.argv[2])
	result = int(sys.argv[3])
	operation = somar(arg1, arg2)
	
	if(operation == result):
		output = True
	else:
		output = False

	print(output)

if __name__ == "__main__":
	main()