nome = input()
salariofixo = float(input())
totalvendas = float(input())

totalvendas = totalvendas*0.15
salariofixo = salariofixo+totalvendas

print(f'TOTAL = R$ {salariofixo:.2f}')