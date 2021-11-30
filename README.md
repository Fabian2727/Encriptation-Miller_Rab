# Miller_Rab

En el archivo "Miller_Rabin.py" se encuentra el programa de generación de primos mediante el test de Miller Rabin. Dicho programa se conforma de las siguientes funciones:
- mod: Calcula a mod b
- Mypow: Realiza lo mismo que la función pow, con la excepción de no convertir los valores a tipo float, esto permite evitar overflow
- getNros: Esta función calcula los valores de t y u para la función witness. Mediante la verificación del cumplimineto de la siguiente operación --> n-1 = 2^t * u (u % 2 = 1)
- witness: Verifica que un número sea POSIBLEMENTE primo al evaluarlo con diversas condiciones
- miller: Realiza el test de witness en un número S de bases para un número N. Y comprueba si estos resultados son primos o no
- getPrimes: Obtiene los números primos de 3 cifras mediante la función Miller. Esta función ayuda a obtener la respuesta del punto 1. de la tarea 

====================================================================================
En el archivo "RandPrimeGen.py" se encuentra el generador de números primos. Conformado por las siguientes funciones:
- mod: Calcula a mod b
- Mypow: Realiza lo mismo que la función pow, con la excepción de no convertir los valores a tipo float, esto permite evitar overflow
- getNros: Esta función calcula los valores de t y u para la función witness. Mediante la verificación del cumplimineto de la siguiente operación --> n-1 = 2^t * u (u % 2 = 1)
- witness: Verifica que un número sea POSIBLEMENTE primo al evaluarlo con diversas condiciones
- miller: Realiza el test de witness en un número S de bases para un número N. Y comprueba si estos resultados son primos o no
- prime_candidate: Crea una lista en la que aleatoriamente agrega 1 y 0 hasta tener una longitus b, de modo que sea un número binario de b bits y posteriormente se convierte dicho binario a int, a dicho int lo llamamos n y se produce la operación m = 2^b -1 y finalmente se retorna n = n | m
- generate_prime: Elegimos como valor S = 15 y se obtiene el candidato a primo n. Posteriormente, minetras la funcion Miller nos devuelva True, iremos aumentano n de dos en dos hasta romper con el bucle y obtener el valor final  de n.
