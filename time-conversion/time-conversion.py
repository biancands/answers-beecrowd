def horas(y):
  x = y//3600
  resto = y%3600
  return x, resto 

def minutos(y):
  z = y//60
  ss = y%60
  return z,ss

segundos = int(input())

h,r = horas(segundos)
m,s = minutos(r)

print(f'{h}:{m}:{s}')