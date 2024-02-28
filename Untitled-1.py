numero1 = int(input("digite um numero "))
numero2 = int(input("digite o segundo numero"))

print("Escolha uma das opções abaixo")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - divisão")
operador = int(input("Digite o numero correspondente:"))

if operador == 1:
    print ("A soma é:" + str(numero1 + numero2))
elif operador == 2:    
    print("A Subtração é:" + str(numero1 - numero2))
elif operador == 3:  
   print("A Multiplicação é:" + str(numero1 * numero2))
elif operador == 4:  
    print("A divisão é:" + str(numero1 / numero2))
else:
    print("Numero incorreto")
    