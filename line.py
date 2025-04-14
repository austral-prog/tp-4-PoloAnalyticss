import math
def line():
    A = float(input("Ingrese el coeficiente A: "))
    B = float(input("Ingrese el coeficiente B: "))
    X1 = float(input("Ingrese el coeficiente X1: "))
    X2 = float(input("Ingrese el coeficiente X2: "))
    print(f"El coeficiente A de su ecuación de la recta es: {A} ")
    print(f"El coeficiente B de su ecuación de la recta es: {B}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {X1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {X2}")
    print("Para la siguiente ecuación:")
    print(f"\t Y = {A}X + {B}")
    print("Dados los siguientes puntos:")
    Y1 = A * X1 + B
    Y2 = A * X2 + B
    print(f"\t P1 ({X1}, {Y1})")
    print(f"\t P2 ({X2}, {Y2})")
    P1 = (X1, A*X1 + B)
    P2 = (X2, A*X2 + B)   
    print(f"La distancia entre ellos es: {math.dist(P1, P2)}")
