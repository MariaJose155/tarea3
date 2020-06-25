"""
Created on Tue Jun 25 19:27:34 2020

@author: María José Arce M / B60561
"""
# PAQUETES
import numpy as np
from scipy import stats
import matplotlib.pyplot  as plt
from mpl_toolkits import mplot3d
import pandas as pd
import csv
from numpy import exp
from numpy import linspace
from numpy import random
import scipy.optimize as optimize
from scipy.optimize import curve_fit
# lista donde se almacenan datos
lote = []

# Cargar en la lista 'xy'
with open('xy.csv', newline='') as archivo:
	lectura = csv.reader(archivo)
	next(lectura, None) 	# no guardar el encabezado
	for fila in lectura:
		lote.append(fila)	# adjuntar cada fila a lote

# Número de filas de lote
N = len(lote)
#inicializamos ys
y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19,y20,y21,y22,y23,y24,y25 = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0;
#inicializamos xs
x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15 = 0,0,0,0,0,0,0,0,0,0,0;
#encontramos la pmf de y para esto recorremos individualmente las 21 columnas
#empezamos en la columna 1 porque la 0 es un "encabezado"
for i in range(N):
	pos1 = float(lote[i][1]);
	y5 += pos1;
#print ("el valor de y5",y5)
for i in range(N):
	pos2 = float(lote[i][2]);
	y6 += pos2;
#print ("el valor de y6",y6)
for i in range(N):
	pos3 = float(lote[i][3]);
	y7 += pos3;
#print ("el valor de y7",y7)
for i in range(N):
	pos4 = float(lote[i][4]);
	y8 += pos4;
#print ("el valor de y8",y8)
for i in range(N):
	pos5 = float(lote[i][5]);
	y9 += pos5;
#print ("el valor de y9",y9)
for i in range(N):
	pos6 = float(lote[i][6]);
	y10 += pos6;
#print ("el valor de y10",y10)
for i in range(N):
	pos7 = float(lote[i][7]);
	y11 += pos7;
#print ("el valor de y11",y11)
for i in range(N):
	pos8 = float(lote[i][8]);
	y12 += pos8;
#print ("el valor de y12",y12)
for i in range(N):
	pos9 = float(lote[i][9]);
	y13 += pos9;
#print ("el valor de y13",y13)
for i in range(N):
	pos10 = float(lote[i][10]);
	y14 += pos10;
#print ("el valor de y14",y14)
for i in range(N):
	pos11 = float(lote[i][11]);
	y15 += pos11;
#print ("el valor de y15",y15)
for i in range(N):
	pos12 = float(lote[i][12]);
	y16 += pos12;
#print ("el valor de y16",y16)
for i in range(N):
	pos13 = float(lote[i][13]);
	y17 += pos13;
#print ("el valor de y17",y17)
for i in range(N):
	pos14 = float(lote[i][14]);
	y18 += pos14;
#print ("el valor de y18",y18)
for i in range(N):
    pos15 = float(lote[i][15]);
    y19 += pos15;
#print ("el valor de y19",y19)
for i in range(N):
    pos16 = float(lote[i][16]);
    y20 += pos16;
#print ("el valor de y20",y20)
for i in range(N):
    pos17 = float(lote[i][17]);
    y21 += pos17;
#print ("el valor de y21",y21)
for i in range(N):
    pos18 = float(lote[i][18]);
    y22 += pos18;
#print ("el valor de y22",y22)
for i in range(N):
    pos19 = float(lote[i][19]);
    y23 += pos19;
#print ("el valor de y23",y19)
for i in range(N):
    pos20 = float(lote[i][20]);
    y24 += pos20;
#print ("el valor de y24",y24)
for i in range(N):
    pos21 = float(lote[i][21]);
    y25 += pos21;
#print ("el valor de y25",y25)

M = 21; #numero de columnas
#encontramos la pmf de x, recorremos individualmente las filas, en este caso evaluamos para cada fila recorrida si se encuentra en la columna 0 cuando esto sucede se debe suma 1 para que no lo tome en cuenta

for j in range(M):
  if j == 0:
    j = j + 1;
  else:
    pos11 = float(lote[0][j]);
    x5 += pos11;
#print ("el valor de x5",x5)
for j in range(M):
  if j == 0:
    j = j + 1;
  else:
    pos22 = float(lote[1][j]);
    x6 += pos22;
#print ("el valor de x6",x6)
for j in range(M):
  if j == 0:
    j = j + 1;
  else:
    pos33 = float(lote[2][j]);
    x7 += pos33;
#print ("el valor de x7",x7)
for j in range(M):
  if j == 0:
    j = j + 1;
  else:
    pos44 = float(lote[3][j]);
    x8 += pos44;
#print ("el valor de x8",x8)
for j in range(M):
  if j == 0:
    j = j + 1;
  else:
    pos55 = float(lote[4][j]);
    x9 += pos55;
#print ("el valor de x9",x9)
for j in range(M):
  if j == 0:
    j = j + 1;
  else:
    pos66 = float(lote[5][j]);
    x10 += pos66;
#print ("el valor de x10",x10)
for j in range(M):
  if j == 0:
    j = j + 1;
  else:
    pos77 = float(lote[6][j]);
    x11 += pos22;
#print ("el valor de x11",x11)
for j in range(M):
  if j == 0:
    j = j + 1;
  else:
    pos88 = float(lote[7][j]);
    x12 += pos88;
#print ("el valor de x12",x12)
for j in range(M):
  if j == 0:
    j = j + 1;
  else:
    pos99 = float(lote[8][j]);
    x13 += pos99;
#print ("el valor de x13",x13)
for j in range(M):
  if j == 0:
    j = j + 1;
  else:
    pos100 = float(lote[9][j]);
    x14 += pos100;
#print ("el valor de x14",x14)
for j in range(M):
  if j == 0:
    j = j + 1;
  else:
    pos110 = float(lote[10][j]);
    x15 += pos110;
#print ("el valor de x15",x15)
#ploteamos las curvas de ambas pmf
curvax = plt.plot([x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15])
plt.title ( 'curva x' )
plt.savefig('curva x')
plt.cla()

curvay = plt.plot([y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19,y20,y21,y22,y23,y24,y25])
plt.title ( 'curva y' )
plt.savefig('curva y')
plt.cla()
#observamos las gráficas

#vectores resultantes de la pmf de x y de y
yy=np.array([y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19,y20,y21,y22,y23,y24,y25])
xx = np.array([x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15])
print("----------------------")
print("valores de la pmf de y")
print(yy)
print("con estos valores obtenemos una gráfica con una forma similar a la de una distribución gaussina o normal" )
print("----------------------")
print("valores de la pmf de x")
print(xx)
print("con estos valores obtenemos una gráfica con una forma similar a la de una distribución gaussina o normal" )
print("----------------------")
#vector de y
ys=[5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
#vector de x
xs = [5,6,8,9,10,11,12,13,14,15]
#graficar en 2d

#use el siguiente link para saber a que se aproxima
#https://relopezbriega.github.io/blog/2016/06/29/distribuciones-de-probabilidad-con-python/

#modelo para pmf de X
#MODELO DISTRIBUCIÓN NORMAL
mu, sigma = 3, 10 # media y desvio estandar
normal = stats.norm(mu, sigma)
x = np.linspace(normal.ppf(0.01),
                normal.ppf(0.99), 100)
fp = normal.pdf(x) # Función de Probabilidad
plt.plot(x, fp)
plt.plot([x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15])
plt.title('Distribución Normal')
plt.ylabel('probabilidad')
plt.xlabel('valores')
plt.savefig('Distribución Normal vs funcion de densidad marginal X')
plt.cla()
#modelo para pmf de Y
#MODELO DISTRIBUCIÓN NORMAL
m, s = 10, 8.5 # media y desvio estandar
normal = stats.norm(m, s)
x = np.linspace(normal.ppf(0.01),
                normal.ppf(0.99), 100)
fp = normal.pdf(x) # Función de Probabilidad
plt.plot(x, fp)
plt.plot([y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19,y20,y21,y22,y23,y24,y25])
plt.title('Distribución Normal')
plt.ylabel('probabilidad')
plt.xlabel('valores')
plt.savefig('Distribución Normal vs funcion de densidad marginal Y')
plt.cla()
#correlacion
#recorro martriz
correlacion = 0;
for j in range(20):
      for i in range(10):
            if j == 0:
                  j = j + 1;
            else:
                  promedio = float(lote[i][j]);
                  vectorys = ys[j];
                  vectorxs = xs[i];
                  correlacion += promedio*vectorxs*vectorys;
                  


print ("la correlacion es",correlacion)
print("----------------------")


#covarianza
sumavectorx = 0;
sumavectory = 0;
for j in range(20):
  sumavectory += ys[j];

for i in range(10):
  sumavectorx +=xs[i];
print("la suma del vector de ys",sumavectory)
print("----------------------")
print("la suma del vector de xs",sumavectorx)
print("----------------------")
#entonces 
xmedia = sumavectorx/11;
ymedia = sumavectory/21;

print("x media es ",xmedia)
print("----------------------")
print("y media es",ymedia)
print("----------------------")
covarianza = 0;
promedio = 0;
for j in range(20):
      for i in range(10):
            if j == 0:
                  j = j + 1;
            else:
                  promedio = float(lote[i][j]);
                  vectorysmedia = ys[j] - xmedia;
                  vectorxsmedia = xs[i] - ymedia;
                  covarianza += promedio*vectorxsmedia*vectorysmedia;
                  
print("la covarianza es", covarianza)
print("Note que la covarianza es negativa esto implica que cuando una variable crece la otra variable decrece. Tienen una relación Inversa.")
print("----------------------")
#coeficiente de correlación
#encontramos varianza
varianzax=vectorysmedia/11;
varianzay=vectorxsmedia/21;
#entonces el coeficiente de correlacion es

pearson = covarianza/varianzax*varianzay
print("la correlacion de pearson es:",pearson)

print("la correlación de pearson debe ser -1 < p < 1, como nuestra correlación de pearson es -0.7 aprox se determina que existe correlación negativa")
print("----------------------")

print("Asumir independencia de X y Y. Analíticamente, ¿cuál es entonces la expresión de la función de densidad conjunta que modela los datos?")
print("sabemos que 2 variables son estadisticamente independientes si y solo si:")
print("P{X ≤ x, Y ≤ y} = P{X ≤ x}P{Y ≤ y} ")
print("de lo anterior sabemos que la función acumulativa es la siguiente:")
print("FX,Y (x, y) = FX (x)FY (y) ")
print("y la función de densidad es:")
print("fX,Y (x, y) = fX (x)fY (y)")
print("tambien sabemos que la función de densidad conjunta bivarida discreta esta dada por:")
print("fX,Y (x, y) = sumatoria de n=1 hasta N sumatoria de n=1 hasta M de P(xn, ym)δ(x − xn)δ(y − ym) ")
print("entonces la expresión que modela los datos es la siguiente:")
print("fX (x|Y ≤ y) = fX (x)")
print("fY (y|X ≤ x) = fY (y)")



#graficar en 3d
#Observo que en el archivo xyp es más sencillo obtener los vectores y,x y z por separado, entonces:
# lista donde se almacenan datos
lote2 = []

# Cargar en la lista 'xyp'
with open('xyp.csv', newline='') as archivo:
	lectura2 = csv.reader(archivo)
	next(lectura2, None) 	# no guardar el encabezado
	for fila2 in lectura2:
		lote2.append(fila2)	# adjuntar cada fila a lote

vecX = [];
vecY = [];
vecZ = [];

for h in range(230):
  vx = lote2[h][0]
  vecX.append(vx)
  vy = lote2[h][1]
  vecY.append(vy)
  vz = lote2[h][2]
  vecZ.append(vz)
#para este punto en vecX,vecY,vecZ tenemos una lista con los valores de x, y y z
#como no supe como modificar cada elemento de la lista y pasarlo a enteros o flotantes segun el caso, decidí hacerlo manual y obtener de esta manera la gráfica en 3D.
vvx=np.array([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9,9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12,12, 12, 12, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 14, 14,14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15])
vvy=np.array([5, 6, 7,8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 5, 6, 7, 8,9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,21, 22, 23, 24, 25, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 5,6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,17,18, 19, 20, 21, 22, 23, 24, 25, 5,6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 5,6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 5, 6, 7,8,9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 5, 6,7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])
vvz=np.array([0.00262, 0.00177, 0.00325, 0.00353, 0.003, 0.00365, 0.00544, 0.00466, 0.00381,0.00445, 0.00122, 0.0049, 0.0022, 0.00359, 0.00304, 0.00212, 0.00355, 0.00247,0.00337, 0.00184, 0.00266, 0.00493, 0.00307, 0.00216, 0.00186, 0.00448, 0.00356, 0.0037, 0.00376,0.00381, 0.00318, 0.00201,0.00337, 0.00301, 0.00435, 0.00369, 0.00266, 0.00396, 0.00394, 0.00495, 0.0014, 0.00387, 0.00283,0.00333, 0.00369, 0.00387, 0.00396, 0.00275, 0.00569, 0.00223, 0.00364, 0.00362, 0.0041, 0.00441, 0.00644, 0.00316, 0.00389, 0.00328, 0.00244,0.00526, 0.00488, 0.00387, 0.00593, 0.00288, 0.00143, 0.00456, 0.00205, 0.00273, 0.00357,0.00175, 0.00551, 0.00627, 0.01, 0.00796, 0.00881, 0.0065, 0.00431, 0.00486, 0.00457,0.00339, 0.00276, 0.00339, 0.00305, 0.00195, 0.00466, 0.00404, 0.00313, 0.00318, 0.00195, 0.0043, 0.00437, 0.00666, 0.0103, 0.01257, 0.01372, 0.01399, 0.00934, 0.00784, 0.00416, 0.00298, 0.00292, 0.00323, 0.0032, 0.00334,0.00238, 0.00277, 0.00293, 0.00373, 0.00315, 0.00509, 0.00259, 0.00512, 0.00727, 0.01273, 0.01635, 0.0176, 0.015, 0.01172, 0.00766, 0.00644, 0.00498, 0.00359, 0.00396, 0.00411,0.00149,0.00321, 0.00425, 0.00405, 0.00389, 0.00315, 0.00198, 0.00418, 0.00526, 0.00645, 0.00944, 0.0125, 0.01554, 0.01179, 0.00905, 0.00792, 0.00482, 0.00462, 0.00296, 0.00112, 0.00238, 0.00271, 0.00366, 0.0023, 0.00294, 0.00217, 0.00533, 0.00328, 0.00532, 0.00596, 0.00453, 0.00395, 0.00736, 0.00752, 0.00873, 0.00635, 0.00634, 0.00205, 0.00363, 0.00528, 0.00367, 0.00467, 0.00356, 0.0034, 0.00361, 0.00461, 0.0, 0.00333, 0.00158, 0.00517, 0.00364, 0.00267, 0.00303, 0.00543, 0.00341, 0.00585, 0.0043, 0.00318, 0.00488, 0.00426, 0.00255, 0.004, 0.00351, 0.00388, 0.00397, 0.00277, 0.00257, 0.00327, 0.00428, 0.00498, 0.00214, 0.00292, 0.00218, 0.00302, 0.00436, 0.00276, 0.00121, 0.0035, 0.00121, 0.004, 0.00265, 0.00234, 0.00145, 0.00358, 0.0019, 0.00268, 0.00336, 0.0029, 0.0012, 0.00108, 0.00243, 0.00227, 0.00562, 0.00247, 0.00363, 0.00437, 0.00272, 0.00387, 0.00385, 0.00388, 0.00257, 0.00406, 0.00393, 0.00244, 0.00333, 0.00235])

fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot3D(vvx,vvy,vvz,'red')
plt.show()
plt.savefig('3d')
