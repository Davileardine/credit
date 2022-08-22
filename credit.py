#Algoritmo de Luhn

cartao = input('Insira um número de cartão: ')

#splitando o número em uma array para tratamento individual
lista = [int(x) for x in cartao]
verificador = lista.pop()

soma = 0

for i in range(len(lista)):

   if i % 2 == 0:
      valorTemp = lista[i] * 2
      if valorTemp > 9:
         valorTemp = valorTemp - 9  # para transformar 15 em 1+5=6, por exemplo -> 15-9 = 6
      soma += valorTemp
   else:
      soma += lista[i]

if soma % 10 + verificador == 10:
   
   if lista[0] == 3 and lista[1] == 7 or lista[1] == 4:
      print('Amex')
   
   if lista[0] == 5 or lista[0] == 3:
      print('Mastercard')
   if lista[0] == 4:
      print('Visa')
else:
   print('Inválido!')
