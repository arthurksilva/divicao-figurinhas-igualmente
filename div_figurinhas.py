# -*- coding: utf-8 -*-

N = 0
F1 = int(input("Qtd de Figurinhas? "))
F2 = int(input("Qtd de Figurinhas? "))
cont = 0
qtd = 0
Result_F1 = 0
Result_F2 = 0

if F1 > F2:
    while(cont == 0):    
        F1 = F1 - 1
        if F1 == F2:
            Result_F1 = F1
            cont = 1
            F1 = F1 + qtd
        qtd = 1 + qtd
           

cont = 0

if F1 < F2:
    while(cont == 0):    
        F2 = F2 - 1
        if F2 == F1:
            Result_F2 = F2
            cont = 1
            F2 = F2 + qtd
        qtd = 1 + qtd
  
print(Result_F1)
print(Result_F2)

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''