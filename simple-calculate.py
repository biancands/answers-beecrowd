codigo1, num1, valor1 = input().split()
codigo2, num2, valor2 = input().split()

codigo1 = int(codigo1)
codigo2 = int(codigo2)

num1 = int(num1)
num2 = int(num2)

valor1 = float(valor1)
valor2 = float(valor2)

valortotal = (num1*valor1)+(num2*valor2)

print(f'VALOR A PAGAR: R$ {valortotal:.2f}')