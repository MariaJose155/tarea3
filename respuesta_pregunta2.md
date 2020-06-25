Respuesta pregunta 2
Asumir independencia de X y Y. Analíticamente, ¿cuál es entonces la expresión de la función de densidad conjunta que modela los datos?
sabemos que 2 variables son estadisticamente independientes si y solo si:
P{X ≤ x, Y ≤ y} = P{X ≤ x}P{Y ≤ y}
de lo anterior sabemos que la función acumulativa es la siguiente:
FX,Y (x, y) = FX (x)FY (y) 
y la función de densidad es:
fX,Y (x, y) = fX (x)fY (y)
tambien sabemos que la función de densidad conjunta bivarida discreta esta dada por:
fX,Y (x, y) = sumatoria de n=1 hasta N sumatoria de n=1 hasta M de P(xn, ym)δ(x − xn)δ(y − ym) 
entonces la expresión que modela los datos es la siguiente:
fX (x|Y ≤ y) = fX (x)
fY (y|X ≤ x) = fY (y)
