# Escribe una funcion llamada 'OrdenarLista()' que recibe una lista de numeros enteros y los escribe 
# en un fichero llamado 'ListaOrdenada.txt'. Lafuncion debe de escribir la lista de numeros que recibe 
# ordenada de mayor a menor en el archivo.
# La funcion no devuelve nada. 

# Escrie otra funcion (NumeroPar()) que abra un fichero que contiene una lista ordenada de numeros, 
# lo lea y escriba en otro fichero ,llamado 'ListaDePares.txt', solo los numeros pares del fichero de entrada.
# Esta funcion no devuelve ningun valor.

# Ademas de las dos funciones teneis que hacer un codigo de ejemplo de ejecucion de las mismas.

file = open('ListaOrdenada.txt')
def OrdenarLista():
    file = open ('ListaOrdenada','w')

