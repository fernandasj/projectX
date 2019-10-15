import sys

def somar(n1, n2):
	return n1 + n2

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
			soma = somar(int(imput[0]), int(imput[1]))
			s = int(listSaida[i-1])
			
			if soma == s:
				print(True)
			else:
				print(False)

	arquivo_entrada.close()
	arquivo_saida.close()

if __name__ == "__main__":
	main()