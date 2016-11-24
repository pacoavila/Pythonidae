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


