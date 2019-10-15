import sys

def somar(args):
	soma = 0
	for arg in args:
		soma += int(arg)
	return soma

def main():

	arquivo_entrada = open("entrada.txt","r")
	arquivo_saida = open("saida.txt","r")

	with arquivo_saida as saida:
		listSaida = saida.read().splitlines()

	i = 0
	with arquivo_entrada as entrada:
		listEntrada = entrada.read().splitlines() 
		for l in listEntrada:
			i += 1
			imput = l.split()
			soma = somar(imput)
			s = int(listSaida[i-1])
			
			if soma == s:
				print(True)
			else:
				print(False)

	arquivo_entrada.close()
	arquivo_saida.close()

if __name__ == "__main__":
	main()
