'''	1 o calculamos s = 3 ∗ 10 + 4 ∗ 9 + 5 ∗ 8 + 7 ∗ 7 + 0 ∗ 6 + 2 ∗ 5 + 1 ∗ 4 + 5 ∗ 3 + 9 ∗ 2 = 202 .
	2 o calculamos x = 11 − s% 11 = 11 − 202 % 11 = 11 − 4 = 7 .
	3 o o dígito verificador é 0 se x> 9 e é o próprio x, caso contrário. Então, d= 7 .
	Exercício 4.14. Codifique a função cpf(n,d) que devolve verdade só se o CPF
	n tem dígito verificador d. Use o método descrito no exercício anterior para
	calcular o dígito verificador do CPF do seguinte modo:
	Suponha CPF = 345702159 .
	1 o calculamos o primeiro dígito a = dv( 345702159 ) = 7 .
	2 o calculamos o segundo dígito b = dv( 3457021597 ) = 1 .
	Então, número completo do CPF é 345702159 − 71 .

	Ainda não identifiquei a lógica para descobrir dígitos verificadores com letras :/
	
	Estados emissores
	
	http://www.acetbs.net.br/samba/noticias/7-artigos/177-como-conferir-um-cpf

'''

def valida_cpf(cpf, multiplo):
	i=0
	s=0
	global separa_dígito 
	separa_dígito = list(cpf)

	while (i < len(separa_dígito)):
		a = int(separa_dígito[i])*multiplo
		s+=a
		multiplo -=1
		i+=1

	x=str(11-int(s%11))
	if (int(x)>9):
		x=str(0)
	separa_dígito.append(x)
	separa_dígito = "".join(separa_dígito[:])

def main(cpf):

	valida_cpf(cpf, 10)
	valida_cpf(separa_dígito, 11)
	estado = separa_dígito[8]
	print("\nSeu cpf é",separa_dígito,"\n")
	if (estado == '1'):
		print("Estado emissor - Distrito Federal, Goiás, Mato Grosso do Sul e Tocantins\n")
	elif (estado == '2'):
		print("Estado emissor - Pará, Amazonas, Acre, Amapá, Rondônia e Roraima\n")
	elif (estado == '3'):
		print("Estado emissor - Ceará, Maranhão e Piauí\n")
	elif (estado == '4'):
		print("Estado emissor - Pernambuco, Rio Grande do Norte, Paraíba e Alagoas\n")
	elif (estado == '5'):
		print("Estado emissor - Bahia e Sergipe\n")
	elif (estado == '6'):
		print("Estado emissor - Minas Gerais\n")
	elif (estado == '7'):
		print("Estado emissor - Rio de Janeiro e Espírito Santo\n")
	elif (estado == '8'):
		print("Estado emissor - São Paulo\n")
	
	elif (estado == '9'):
		print("Estado emissor - Paraná e Santa Catarina\n")
	else:
		print("Estado emissor - Rio Grande do Sul\n")

cpf = input("Digite os 9 primeiros números de seu CPF: ")

if (len(cpf) == 9 and cpf.isdigit()) == True:
	main(cpf)
else:
	while (True):
		if (len(cpf) <=8 or len(cpf) >= 10 or cpf.isdigit() == False):
			cpf = (input("\nNão podem estar entre os dígitos base:\n\n	-Letras;\n	-Caracteres especiais;\n	-Mais de 10 dígitos.\n\nDigite os 9 primeiros dígitos de seu CPF: "))
			if (len(cpf) == 9 and cpf.isdigit()):
				main (cpf)
				break
