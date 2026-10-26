
# Definitionen

b_i = [
     0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 

]

x_i = [
    -10.0, -9.0, -8.0, -7.0, -6.0, -5.0, -4.0, -3.0, -2.0, -1.0,
    0.0,  1.0,  2.0,  3.0,  4.0,  5.0,  6.0,  7.0,  8.0,  9.0, 10.0
]


# Funktionen

def f_1(x_i: float) -> float:

    y_i = []                # definition eriner Liste, leer    
    for x in  x_i:          # For schleoife über salle Objekte
        y = x               # Funktion
        y_i.append(y)       # Liste füllen, anhängen            
    print ("1. Funktion Y = x")
    print(y_i)    
    return y_i              # Liste zurück geben

def f_2(x_i: float) -> float:

    y_i = []                # definition eriner Liste, leer    
    for x in  x_i:       # For schleoife über salle Objekte
        y =  2 * x + 3      # Funktion
        y_i.append(y)   # Liste füllen, anhängen            
    print ("2. Funktion Y = 2x +3")
    print(y_i)    
    return y_i         # Liste zurück geben

def f_3(x_i: float) -> float:

    y_i = []
    for x in x_i:
        y = squared = x ** 2
        y_i.append(y)
    print ("3. Funktion Y = x^2")
    print(y_i)
    return y_i

def f_4(x_i: float) -> float:

    y_i = []
    for x in x_i:
        y = 5 * x +2 **3
        y_i.append(y)
    print ("4. Funktion Y = 5x +2^3")
    print(y_i)
    return y_i 


def f_5(b_i: float) -> float:

    y_i = []
    for b in b_i:
        y = b * 3.14
        y_i.append(round(y, 3))
    print ("5. Funktion Y = b*3.14")
    print(y_i)
    return y_i 




# Ausführung


print(x_i)

y_i = f_1(x_i)
y_i = f_2(x_i)
y_i = f_3(x_i) 
y_i = f_4(x_i) 
y_i = f_5(b_i)