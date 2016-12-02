
# coding: utf-8

# # Un mundo de código 4

# 1.- Escribir una función que reciba una tupla de elementos e indique si se encuentran ordenados de menor a mayor o no.

# In[17]:

#pylint: disable = I0011, c0103
""" DocString
"""

def test_sorted(tupla):
    """
1.- Escribir una función que reciba una tupla de elementos e indique si se
encuentran ordenados de menor a mayor o no.
    """
    if tupla == ():
        return -1
    previous = tupla[0]
    for item in tupla:
        if previous <= item:
            previous = item
        else:
            return False
    return True


# In[18]:

tupla1 = (1,2,3,4,5,6,6,7,8,9,10)
tupla2 = (1,2,3,5,4,6,7,8,9,10)
tupla3 = ()
tupla4 = (5,)
print(test_sorted(tupla1))
print(test_sorted(tupla2))
print(test_sorted(tupla3))
print(test_sorted(tupla4))


# 2.- Dominó.

# a) Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son recibidas en dos tuplas, por ejemplo: (3,4) y (5,4).

# In[7]:

#pylint: disable = I0011, c0103
""" DocString
"""

def domino_1(token_1, token_2):
    """
a) Escribir una función que indique si dos fichas de dominó encajan o no.
Las fichas son recibidas en dos tuplas, por ejemplo: (3,4) y (5,4).
    """
    return (token_1[0] == token_2[0] or token_1[0] == token_2[1]
        or token_1[1] == token_2[0] or token_1[1] == token_2[1])


# In[8]:

print(domino_1((1, 2), (3, 2)))
print(domino_1((1, 2), (3, 5)))
print(domino_1((1, 2), (3, 1)))


# b) Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son recibidas en una cadena, por ejemplo: 3-4 2-5. Nota: utilizar la función split de las cadenas.
# 

# In[22]:

#pylint: disable = I0011, c0103
""" DocString
"""

def domino_2(token):
    """
b) Escribir una función que indique si dos fichas de dominó encajan o no.
Las fichas son recibidas en una cadena, por ejemplo: 3-4 2-5.
Nota: utilizar la función split de las cadenas.
    """
    token = token.split()
    token_1 = token[0].split("-")
    token_2 = token[1].split("-")
    return (token_1[0] == token_2[0] or token_1[0] == token_2[1]
        or token_1[1] == token_2[0] or token_1[1] == token_2[1]) 


# In[23]:

print(domino_2("1-2 3-2"))
print(domino_2("1-2 3-5"))
print(domino_2("1-2 3-1"))


# 3.- Campaña electoral

# a) Escribir una función que reciba una tupla con nombres, y para cada nombre imprima el mensaje "Estimado [nombre], vote por mí".

# In[24]:

#pylint: disable = I0011, c0103
""" DocString
"""

def campana_1(names):
    """
a) Escribir una función que reciba una tupla con nombres, y para cada 
nombre imprima el mensaje "Estimado [nombre], vote por mí".
    """
    for i in names:
        print("Estimado %s, vote por mí" % i)


# In[26]:

campana_1(("José", "Ango", "Juana", "Luis", "Paco"))


# b) Escribir una función que reciba una tupla con nombres, una posición de origen p y una cantidad n, e imprima el mensaje anterior para los n nombres que se encuentran a partir de la posición p.

# In[35]:

#pylint: disable = I0011, c0103
""" DocString
"""

def campana_2(names, pos):
    """
b) Escribir una función que reciba una tupla con nombres, una posición
de origen p y una cantidad n, e imprima el mensaje anterior para los n
nombres que se encuentran a partir de la posición p.
    """
    for i in range(pos, len(names)):
        print("Estimado %s, vote por mí" % names[i])


# In[36]:

campana_2(("José", "Ango", "Juana", "Luis", "Paco"), 2)


# c) Modificar las funciones anteriores para que tengan en cuenta el género del destinatario, para ello, deberán recibir una tupla de tuplas, conteniendo el nombre y el género.

# In[43]:

#pylint: disable = I0011, c0103
""" DocString
"""

def campana_3(names):
    """
c) Modificar las funciones anteriores para que tengan en cuenta el
género del destinatario, para ello, deberán recibir una tupla de
tuplas, conteniendo el nombre y el género.
    """
    for i in names:
        if i[0]=="H":
            print("Estimado %s, vote por mí" % i[1])
        else:
            print("Estimada %s, vote por mí" % i[1])

def campana_4(names, pos):
    """
c) Modificar las funciones anteriores para que tengan en cuenta el
género del destinatario, para ello, deberán recibir una tupla de
tuplas, conteniendo el nombre y el género.
    """
    for i in range(pos, len(names)):
        if names[i][0]=="H":
            print("Estimado %s, vote por mí" % names[i][1])
        else:
            print("Estimada %s, vote por mí" % names[i][1])


# In[45]:

campana_3((("H", "José"), ("H", "Ango"), ("M", "Juana"), ("H", "Luis"), ("H", "Paco")))
print()
campana_4((("H", "José"), ("H", "Ango"), ("M", "Juana"), ("H", "Luis"), ("H", "Paco")),2)


# 4.- Vectores

# a) Escribir una función que reciba dos vectores y devuelva su producto escalar.

# In[49]:

#pylint: disable = I0011, c0103
""" DocString
"""

def scalar(x, y):
    """
    a) Escribir una función que reciba dos vectores y devuelva su producto escalar.
    """
    return (x[0]*y[0]+x[1]*y[1])


# In[50]:

print(scalar((1,4), (6,2)))


# b) Escribir una función que reciba dos vectores y devuelva si son o no ortogonales.

# In[ ]:

#pylint: disable = I0011, c0103
""" DocString
"""

def ortogonal(x,y):
    """
    b) Escribir una función que reciba dos vectores y devuelva si son o no ortogonales.    
    """
    if scalar(x,y) == 0:
        return True
    else:
        return False


# c) Escribir una función que reciba dos vectores y devuelva si son paralelos o no.

# In[68]:

#pylint: disable = I0011, c0103
""" DocString
"""

def parallel(x,y):
    """
    c) Escribir una función que reciba dos vectores y devuelva si son paralelos o no.
    """
    return (x[0]/y[0]) == (x[1]/y[1])


# In[73]:

print(parallel((4,4), (9,9)))
print(parallel((4,4), (9,7)))


# d) Escribir una función que reciba un vector y devuelva su norma.

# In[76]:

#pylint: disable = I0011, c0103
""" DocString
"""

def magnitude(x):
    """
    d) Escribir una función que reciba un vector y devuelva su norma.
    """
    return(x[0]*x[0] + x[1]*x[1]) ** (1/2)


# In[77]:

print(magnitude((2,2)))


# 5.- Dada una lista de números enteros, escribir una función que:

# a) Devuelva una lista con todos los que sean primos.

# In[ ]:




# b) Devuelva la sumatoria y el promedio de los valores.

# In[ ]:




# c) Devuelva una lista con el factorial de cada uno de esos números.

# In[ ]:




# 6.- Dada una lista de números enteros y un entero k, escribir una función que:
# 
# 

# a) Devuelva tres listas, una con los menores, otra con los mayores y otra con los iguales a k.
# 
# 

# In[ ]:




# b) Devuelva una lista con aquellos que son múltiplos de k.

# In[ ]:




# 7.- Escribir una función que reciba una lista de tuplas (Apellido, Nombre, Inicial_segundo_nombre) y devuelva una lista de cadenas donde cada una contenga primero el nombre, luego la inicial con un punto, y luego el apellido.
# 
# 

# In[ ]:




# 8.- Inversión de listas
# 
# 

# a) Realizar una función que, dada una lista, devuelva una nueva lista cuyo contenido sea igual a la original pero invertida. Así, dada la lista ['Di', 'buen', 'día', 'a', 'papa'], deberá devolver ['papa', 'a', 'día', 'buen', 'Di'].
# 

# In[ ]:




# b) Realizar otra función que invierta la lista, pero en lugar de devolver una nueva, modifique la lista dada para invertirla, sin usar listas auxiliares.
# 

# In[ ]:




# 9.- Escribir una función empaquetar para una lista, donde empaquetar significa indicar la repetición de valores consecutivos mediante una tupla (valor, cantidad de repeticiones). Por ejemplo, empaquetar ([1, 1, 1, 3, 5, 1, 1, 3, 3]) debe devolver [(1, 3) , (3, 1) , (5, 1), (1, 2), (3, 2)].
# 
# 

# In[ ]:




# 10.- Matrices.

# a) Escribir una función que reciba dos matrices y devuelva la suma.
# 

# In[ ]:




# b) Escribir una función que reciba dos matrices y devuelva el producto.
# 

# In[ ]:




# c) Escribir una función que opere sobre una matriz y mediante eliminación gaussiana devuelva una matriz triangular superior.
# 

# In[ ]:




# d) Escribir una función que indique si un grupo de vectores, recibidos mediante una lista, son linealmente independientes o no.
# 

# In[ ]:




# 11.- Plegado de un texto. Escribir una función que reciba un texto y una longitud y devuelva una lista de cadenas de como máximo esa longitud. Las líneas deben ser cortadas correctamente en los espacios (sin cortar las palabras).
# 
# 

# In[ ]:




# 12.- Funciones que reciben funciones.
# 
# 

# a) Escribir una funcion llamada map, que reciba una función y una lista y devuelva la lista que resulta de aplicar la función recibida a cada uno de los elementos de la lista recibida.
# 

# In[ ]:




# b) Escribir una función llamada filter, que reciba una función y una lista y devuelva una lista con los elementos de la lista recibida para los cuales la función recibida devuelve un valor verdadero.
# ¿En qué ejercicios de nuestro mundo de código podría haberse utilizado estas funciones?

# In[ ]:




# 13.- Escribir una función que reciba una lista desordenada y un elemento, que:
# 

# a) Busque todos los elementos coincidan con el pasado por parámetro y devuelva la cantidad de coincidencias encontradas.
# 

# In[ ]:




# b) Busque la primera coincidencia del elemento en la lista y devuelva su posición.
# 

# In[ ]:




# c) Utilizando la función anterior, busque todos los elementos coincidan con el pasado por parámetro y devuelva una lista con las posiciones.
# 

# In[ ]:




# 14.- Escribir una función que reciba una lista de números no ordenada, que:

# a) Devuelva el valor máximo.

# In[ ]:




# b) Devuelva una tupla que incluya el valor máximo y su posición.
# ¿Qué sucede si los elementos son cadenas de caracteres? Nota: no utilizar lista.sort()

# In[ ]:




# 15.- Agenda simplificada. Escribir una función que reciba una cadena a buscar y una lista de tuplas (nombre_completo, telefono), y busque dentro de la lista, todas las entradas que contengan en el nombre completo la cadena recibida (puede ser el nombre, el apellido o sólo una parte de cualquiera de ellos). Debe devolver una lista con todas las tuplas encontradas.

# In[ ]:




# 16.- Sistema de facturación simplificado
# 
# Se cuenta con una lista ordenada de productos, en la que uno consiste en una tupla de (identificador, descripción, precio), y una lista de los productos a facturar, en la que cada uno consiste en una tupla de (identificador, cantidad).
# 
# Se desea generar una factura que incluya la cantidad, la descripción, el precio unitario y el precio total de cada producto comprado, y al final imprima el total general.
# 
# Escribir una función que reciba ambas listas e imprima por pantalla la factura solicitada.

# In[ ]:




# 17.- Escribir una función que reciba una lista ordenada y un elemento, si el elemento se encuentra en la lista, debe encontrar su posición, mediante búsqueda binaria y devolverlo. Si no se encuentra, debe agregarlo a la lista en la posición correcta y devolver esa nueva posición. (No utilizar lista.sort())

# 18.- Escribir una función que reciba una lista de tuplas, y que devuelva un diccionario en donde las claves sean los primeros elementos de las tuplas, y los valores una lista con los segundos.
# 
# Por ejemplo:
# 
# l = [ ('Nola', 'don Pepito'), ('Nola', 'don Jose'), ('Buenos', 'días') ]
# print tuplas_a_diccionario(l)
# Deberá mostrar: { 'Nola': ['don Pepito', 'don Jose'], 'Buenos': ['días'] }

# In[ ]:




# 19.- Diccionarios usados para contar.

# a) Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad de apariciones de cada palabra en la cadena. Por ejemplo, si recibe "Qué lindo día que hace hoy" debe devolver: 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1
# 

# In[ ]:




# b) Escribir una función que cuente la cantidad de apariciones de cada carácter en una cadena de texto, y los devuelva en un diccionario.
# 

# In[ ]:




# c) Escribir una función que reciba una cantidad de iteraciones de una tirada de 2 dados a realizar y devuelva la cantidad de veces que se observa cada valor de la suma de los dos dados. Nota: utilizar el módulo random para obtener tiradas aleatorias.
# 

# In[ ]:




# 20.- Continuación de la agenda.
# 
# Escribir un programa que vaya solicitando al usuario que ingrese nombres.
# 
# Si el nombre se encuentra en la agenda (implementada con un diccionario), debe mostrar el teléfono y, opcionalmente, permitir modificarlo si no es correcto.
# Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente. El usuario puede utilizar la cadena "*", para salir del programa.
# 

# In[ ]:




# 21.- Escribir una función que reciba un texto y para cada caracter presente en el texto devuelva la cadena más larga en la que se encuentra ese caracter.

# In[ ]:



