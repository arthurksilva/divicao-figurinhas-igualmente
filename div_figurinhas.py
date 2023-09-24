# -*- coding: utf-8 -*-

N = 0
F1 = int(input("Qtd de Figurinhas? "))
F2 = int(input("Qtd de Figurinhas? "))
cont = 0

while(cont == 0):
    N = N + 1    
    if F1 % N == 0:
        Result_F1 = F1 / 2
        cont  = 1

cont = 0

while(cont == 0):
    if F2 % N == 0:
        Result_F2 = F1 / 2
        cont  = 1  
  
print(Result_F1)
print(Result_F2)

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''