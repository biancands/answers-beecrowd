import math as m

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

def distancia(x1,y1,x2,y2):
    calculo = m.sqrt(((x2-x1)**2)+((y2-y1)**2))
    print(f'{calculo:.4f}')
    
distancia(x1,y1,x2,y2)
