import numpy as np
import bz2 
from scipy.stats import norm
import matplotlib.pyplot as pl 
from momentos import momentos
n = 0
datos = []
with bz2.open( "chitaga.dat.bz2", "rt" ) as bz_file:
   for line in bz_file:
       rline = line.rstrip('\n').split(' ')
       if len(rline) == 3:
           if rline[0] != "#":
               datos.append(float(rline[2]))
        # n += 1
        # if n == 200:
        #     break
nbins = 18
xmin = min( datos )
xmax = max ( datos )
pl.figure(1)
frec1, bins , patches = pl.hist(datos,bins=nbins,range=( xmin, xmax),histtype='bar')
pl.title('HISTOGRAMA VALOR OFFSET')
pl.ylabel('FRECUENCIA')
pl.xlabel('DATA')
bins_g = bins[1:len(bins)]
N_contado = sum(frec1)
analisis = momentos()
varianza = analisis.m2(frec1, bins_g, N_contado )
mu, std = norm.fit(datos)
mu = mu
x = np.linspace(xmin, xmax, 100)
pl.figure(2)
frec2, bins2 , patches2 = pl.hist(datos,bins=nbins,range=( xmin, xmax),histtype='bar',density= True)
p = norm.pdf(x, mu, std)
pl.plot(x, p, 'k', linewidth=2)
pl.title('HISTOGRAMA  Y CURVA DE AJUSTE NORMALIZADA')
pl.ylabel('FRECUENCIA')
pl.xlabel('DATA')
pl.legend(('Curva de Ajuste','Histograma Normalizado'),
           loc='upper right')
pl.text(53, 0.6, r'$\mu$ = %0.4f'%(varianza[4]), fontsize=10)
pl.text(53, 0.55, r'$\sigma^{2}$ = %0.4f'%(varianza[0]), fontsize=10)
pl.text(53, 0.5, r'$\sigma$ = %0.4f'%(varianza[1]), fontsize=10)
pl.text(53, 0.45, r'Asimetria = %0.4f'%(varianza[2]), fontsize=10)
pl.text(53, 0.4, r'Kurt = %0.4f'%(varianza[3]), fontsize=10)
# print ("Varianza = ", varianza[0], "Sigma = ", varianza[1], "asimetria = ", varianza[2], "curtosis = ", varianza[3], "media = ", varianza[4])
pl.show()