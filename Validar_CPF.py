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
	print("Seu cpf é ",separa_dígito)
	

cpf = input("Digite os 9 primeiros números de seu CPF: ")

if (len(cpf) == 9 and str(cpf) in '0123456789'):
	main(cpf)	
else:
	while (True):
		if (len(cpf) <=8 or len(cpf) >= 10 or str(cpf) not in '0123456789'):
			cpf = (input("\nNão podem estar entre os dígitos base:\n\n	-Letras;\n	-Caracteres especiais;\n	-Mais de 10 dígitos.\n\nDigite os 9 primeiros dígitos de seu CPF: "))
			if (len(cpf) == 9 and str(cpf) in '0123456789'):
				main (cpf)
				break
