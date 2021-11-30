# Miller_Rab

En el archivo "Miller_Rabin.py" se encuentra el programa de generación de primos mediante el test de Miller Rabin. Dicho programa se conforma de las siguientes funciones:
- mod: Calcula a mod b
- Mypow: Realiza lo mismo que la función pow, con la excepción de no convertir los valores a tipo float, esto permite evitar overflow
- getNros: Esta función calcula los valores de t y u para la función witness. Mediante la verificación del cumplimineto de la siguiente operación --> n-1 = 2^t * u (u % 2 = 1)
- witness: Verifica que un número sea POSIBLEMENTE primo al evaluarlo con diversas condiciones
- miller: Realiza el test de witness en un número S de bases para un número N. Y comprueba si estos resultados son primos o no
- getPrimes: Obtiene los números primos de 3 cifras mediante la función Miller. Esta función ayuda a obtener la respuesta del punto 1. de la tarea 
