RESPUESTA UNO
Vector pmf de y
[0.03698 0.03364 0.03105 0.03481 0.03546 0.0395  0.04947 0.04839 0.06363 0.08419 0.07856 0.08193 0.06626 0.05344 0.0444  0.03981 0.03691 0.0343 0.04137 0.02939 0.03657]
De este primer vector observando la imagen adjunta curvay.png podemos determinar que la gráfica es similar a una distribución guassiana o normal.

Vector pmf de x
[0.06448 0.06785 0.07734 0.09035 0.11988 0.13828 0.11806 0.09494 0.07289 0.05709 0.06233]
De este primer vector observando la imagen adjunta curvax.png podemos determinar que la gráfica es similar a una distribución guassiana o normal.

Para ambos casos se hizo la comparación con las distribuciones en la siguiente página web.
https://relopezbriega.github.io/blog/2016/06/29/distribuciones-de-probabilidad-con-python/

Y de esa manera se obtuvo cual era la mejor curva de ajuste para ambas pmf.

RESPUESTA DOS
Asumir independencia de X y Y. Analíticamente, ¿cuál es entonces la expresión de la función de densidad conjunta que modela los datos?
<img src="https://render.githubusercontent.com/render/math?math=G(K) = (\frac{1}{\sqrt{2\pi\mu^2}})\exp{\frac{-(k-u)^2}{2\mu^2}}">
Entonces tenemos para x
<img src="https://render.githubusercontent.com/render/math?math=Gx(x) = (\frac{1}{\sqrt{2\pi\mu x^2}})\exp{\frac{-(x-ux)^2}{2\mu x^2}}">
y para y
<img src="https://render.githubusercontent.com/render/math?math=Gy(y) = (\frac{1}{\sqrt{2\pi\mu y^2}})\exp{\frac{-(y-uy)^2}{2\mu y^2}}">
Por lo tanto
<img src="https://render.githubusercontent.com/render/math?math=Gx,y(K) = Gx(x)Gy(y)">
Donde <img src="https://render.githubusercontent.com/render/math?math=\mu x = 3.299 , \mu y = 6.026 ,ux = 9.904, uy = 15.079.">

En caso de no poder ver la respuesta bien ver pdf adjunto
RESPUESTA TRES
Para obtener los resultados del punto 3 es necesario tener claro esto primero:
Vector de y
ys=[5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
Vector de x
xs = [5,6,8,9,10,11,12,13,14,15]
Entonces:
-La suma del vector de ys 290
-La suma del vector de xs 103
-X media es  9.363636363636363
-Y media es 13.80952380952381
Por lo tanto:
-La correlacion es 142.0366
-La covarianza es -17.352364675324676
Note que la covarianza es negativa esto implica que cuando una variable crece la otra variable decrece. Tienen una relación Inversa.
-La correlacion de pearson es: -0.7392980823207718
La correlación de pearson debe ser -1 < p < 1, como nuestra correlación de pearson es -0.7 aprox se determina que existe correlación negativa

RESPUESTA CUATRO
Las gráficas en 2D son del modelo y su respectiva pmf (note que la pmf no empieza en 0 por lo tanto se encuentra desfasada de manera vertical en la gráfica).
La gráfica en 3D se encuentra adjunta.
