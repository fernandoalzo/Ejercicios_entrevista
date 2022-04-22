import sympy
class funciones():
    
    def max_num(list_values):
        """
        El parametro debe ser una lista
        >>> funciones.max_num([1, 2, 4, 5, 6, 7])
        7

        la lista solo debe conrener numeros enteros 
        >>> funciones.max_num([1, 2, 4, 5, 6, "7"])
        Traceback (most recent call last):
        ...
        TypeError: '>' not supported between instances of 'str' and 'int'
        """ 
        return max(list_values)

    def min_num(list_values):
        """
        El parametro debe ser una lista
        >>> funciones.min_num([1, 2, 4, 5, 6, 7])
        1

        la lista solo debe conrener numeros enteros 
        >>> funciones.min_num([1, 2, 4, 5, 6, "7"])
        Traceback (most recent call last):
        ...
        TypeError: '<' not supported between instances of 'str' and 'int'
        """
        return min(list_values)

    def first_number(list_values):
        return list_values[0]

    def last_number(list_values):
        return list_values[-1]

    def number_of_prime_numbers(list_values):
        """
        El parametro debe ser una lista
        >>> funciones.number_of_prime_numbers([1, 2, 4, 5, 6, 7])
        3
        """
        numeros_primos = [x for x in list_values if sympy.isprime(x)]
        return len(numeros_primos)
    
    def number_of_even_numbers(list_values):
        numeros_pares = [x for x in list_values if x % 2 == 0]
        return len(numeros_pares)
    
    def number_of_odd_numbers(list_values):
        numeros_impares = [x for x in list_values if x % 2 != 0 ]
        return len(numeros_impares)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)