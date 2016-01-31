"""#Factorial calculado de dos formas
factorial = 10
acum = 1
while factorial >= 1:
    acum = acum * factorial
    factorial = factorial - 1
    print "El valor del factorial temporal es %i" % acum
print "El valor del factorial es %i" % acum
"""
#Factorial recursivo
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)

print "Resultado: %i" % factorial(5)
