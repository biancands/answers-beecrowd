a,b,c = map(int, input().split())

def calculaMaior(x,y):
    maior = (x+y+abs(x-y))/2
    return maior
    
def calcula(a,b,c):
    valor1 = calculaMaior(a,b)
    valor2 = calculaMaior(b,c)
    
    if valor1 > valor2:
        print(f'{valor1:.0f} eh o maior')
    else:
        print(f'{valor2:.0f} eh o maior')
        
calcula(a,b,c)
