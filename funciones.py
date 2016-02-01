# len (<blabla>)
#Funcion que nos indica la longitud de lo que le pasemos
print len("Hola Mundo")
print len("Hola Planeta Tierra")
print len([5,6,7,8,9,0,1])
print len([5,6,7,8,9,0,1,2,3,4,5])
print len(("sfa", "laf"))
print len(range(10))
print len(range(100))

#type(<XD>) Funcion que nos indica el tipo de dato algun objeto
print type("sdfer")
print type('sdfer')
print type(len)
import datetime
print type(datetime)
print type(30000000000000000000000000000000000000000000)
print type(30000000000000000000000000000000000000000000.00000001)

#sum(<XD>)
#Funcion que obtiene la sumatoria de una listo o ...
print sum([3,4,5,6,7])
print sum([3,4,5,6,7,8,9,10])

arr= [3,3,5,8,9,10] + range(1000)

print len(arr)
print sum(arr)

#Duck Typing
print "H" * 5
print "Hola" * 5

#Redoondea a tantos decimales
print round(3.14159,4)

import math
#Redondea al numero superior
print math.ceil(3.14159)

#Redondea al numero inferior
print math.floor(3.14159)

#Funcion de math
print math.factorial(5)

#Funcion map, sobrecargar funciones?
print map(str, [5,3,7])
print map(math.ceil, [5.4, 3.3, 7.8])
print map(math.factorial,range(10))

#Funcion de ordenamiento
print sorted([5,6,3,7,1,8,9])
print sorted(["B", "A", "D" ])
