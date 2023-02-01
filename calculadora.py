#Primeiro Programa Criado em Python 01/02/2023
#Desenvolvedor Gabriel Odorcik
print('Calculadora')
print('Adição = a / Subtração = s / Multiplicação = m / Divisão = d')

n_1 = int(input('Digite o primeiro valor: '))

n_2 = int(input('Digite o segundo valor: '))
#Entrada dos Valores da calculadora

adicao = n_1 + n_2

sub = n_1 - n_2

multi = n_1 * n_2

divis = n_1 / n_2
#declaração das funções dos calculos

bot = str(input('Digite a letra correspondente ao calculo: '))
#declaração da entrada da função escolhida

if bot == 'a':
    print(adicao)

elif bot == 's':
    print(sub)

elif bot == 'm':
    print(multi)

elif bot == 'd':
    print(divis)

else:
    print('Impossivel')

#Definindo as condições


   

