
def normal(i):
    return i

# si la funcion NO va a ser reutilizable:
#       normal = lambda x: x

def cuadrado(x):
    return x * x

def cubo(x):
    return x**3

def sumaTodos(limitTo, f):
    resultado = 0
    for i in range(limitTo+1):
        resultado += f(i)
        
    return resultado

if __name__ == '__main__':
    
    print(sumaTodos(100, normal))
    print(sumaTodos(3, cuadrado))
