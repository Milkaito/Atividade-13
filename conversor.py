
def coverpoler():
 n1=float(input('Digite um valor em centímetro: '))
 
 cont= 2.54/n1
  
 file=open('valor.txt','w+')
 file.write('o valor {} em centímetros corresponde a {} valor em polegadas.'.format(n1,cont))