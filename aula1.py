# para marcar comentario: selecionar as linhas e Ctrl ;

# print("ola mundo!")

# soma = 2 + 3

# print(soma)

# subtracao = 5 - 2 

# print (subtracao)

# print ("O resultado é:",5-2)

# multiplicacao = 9 * 9
# divisao = 8 / 2

# print (multiplicacao, divisao)

# divisao1 = 0

# Estrutura de controle - condicionais 
# Default do Python é guardar qualquer input como String

# idade = int(input("digite sua idade:"))

# if idade >= 18:
#     print("no brasil vc é maior de idade")
# else:
#     print("nao é maior de idade")

# nota = 50

# if nota >= 90:
#     print("A")
# elif nota >= 80:
#     print("B")
# elif nota >=70:
#     print("C")
# elif nota <= 20:
#     print("reprovado")
# else:
#     print("nota abaixo C")


# Loop

# frutas = ["uva","banana","laranja"]

# for fruta in frutas:
#     print(fruta)

# for i in frutas:
#     print(i)

# for i in range(5):
#     print(i)

# while

# contador = 0

# while contador < 5:
#     print (contador)
#     contador += 1
#     # contador = contador + 1
    
# frutas = ["uva","banana","laranja","pera"]

# for fruta in frutas:
#     if  fruta == "laranja":
#         break
#     print(fruta)

# for indice, fruta in enumerate(frutas):
#     print(f"O Indice:{indice} é Fruta:{fruta}")

#     print(indice, fruta)

# altura = 1.78

# FOR aninhado - ou de 2 dimensoes - arrays bidimensionais

# for i in range(5):
#     for j in range(3):
#         print(f"i: {i} e j: {j}")

# matriz = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# for linha in matriz:
#     for elemento in linha:
#         print(elemento)

# Funcoes

# def boasVindas(nome):
#     return "Seja bem vinda " + nome + "!"

# aluna = input("Digite o nome: ")

# mensagem = boasVindas(aluna)

# print(mensagem)

#Alternativa para imprimir
#print(boasVindas(aluna))

# #Funcao vazia, so imprimir

# # def boasVindas ():
# #     print("seja bem vinda")

# # boasVindas()

# def quadradoDeUmNumero(numero):
#     return numero ** 2

# numeroTerminal = int(input("digite um numero: "))
                     
# resultado = quadradoDeUmNumero(numeroTerminal)

# print("resultado é", resultado)

#Estrutura Chave-VaLOR

# pessoa = {'nome':'Joao','idade':'25','cidade':'Sao Paulo'}

# pessoa = {
#     'nome':'Joao',
#     'idade':'25',
#     'cidade':'Sao Paulo'
#     }

# print(pessoa['nome'])

#Objeto - sempre que criar uma classe, colocar a 1a letra maiuscula

# class Pessoa:
#     def __init__(self, nome, idade, cidade):
#         self.nome = nome
#         self.idade = idade
#         self.cidade = cidade

# pessoa = Pessoa(nome='Joao', idade='25', cidade='SP')
# print(pessoa.nome)

#mais de 1 compnente na funcao

# def soma(a, b):
#     return a+b
# resultadoSoma = soma(4, 6)

# print('A soma é: ', resultadoSoma)

# Exercicio

# kilometros = int(input("Quantos kms vc percorreu com o carro alugado?"))

# dias = int(input("Qtos dias vc alugou o carro?"))

# precoFinal = (kilometros*0.15)+(dias*60)

# print(f'O valor final a ser pago será: R$',precoFinal)

# # Tabuada (1 a 10)

# for i in range(1,11):
#     for j in range (1,11):
#        print(f'{i} X {j} =', i * j)


# Pedir 10 numeros impares

# lista = []
# contador = 0
# while contador <10:
#     numero = int(input("Digite um numero impar: "))
#     if numero%2 != 0:
#         lista.append(numero)
#         contador = contador+1
#     else:
#         numero = int(input("Digite um numero impar: "))
#         contador = contador

# site para treinar: CODEWARS

# # resolucao da profa
# numeros = []
# numero = 0
# quantidadeSobrando = 10

# while quantidadeSobrando > 0:
#     numero = 0
#     while numero % 2 == 0:
#         numero = int(input("Digite um número ímpar, não pode ser um número par: "))
    
#     numeros.append(numero)
#     quantidadeSobrando -= 1
    
# posicao = 0

# while posicao < len(numeros):
#     print(numeros[posicao])
#     posicao += 1

# print(numeros)


import pandas as pd

