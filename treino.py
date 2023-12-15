# fazer print de uma frase e mais 2+3

# criar 2 variaves e fazer print destas 2 variaveis

#pedir idade, transformar em inteiro e usar IF para maior de 18 anos, dar frase se e maior ou nao de idade

# pedir notas e usar if e elif

#criar um array de frutas e fazer loop FoR, imprimir todas as frutas

# usar WHILE para fazer print de 0 a 5

# usar break dentro do FOR para fruta igual a laranja

# criar 1 FOR com enumerate das frutas e print do numero indice e da fruta
frutas = ["maca","banana","uva","melancia"]

for fruta in enumerate(frutas):
    print(fruta)

# criar FOR com range (5)

# inserir uma matriz
#criar print para cada um dos elementos da matriz, usar FOR

#criar funcao de boas vindas (frase com o nome)


# criar uma funcao quadrado de um numero e pedir para fazer print do resultado

def quadradoNumero (num, num2):
    return num**2, num2*2
   

numeroTerminal = int(input("digite um numero "))
numeroTerminal2 = int(input("digite outro numero "))

print(f"O quadrado do numero", numeroTerminal, " é: ", quadradoNumero(numeroTerminal, numeroTerminal2))


