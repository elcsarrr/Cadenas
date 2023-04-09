texto = "Hola Que Tal"
texto2 = "hoLa quE tAL"
print (texto)
print (texto.lower())# pone en minuscula todo el texto
print(texto.upper())# pone en mayuscula todo el texto
print (texto2.title())#pone el texto en formato de titulo
print (texto.find("Que")) # encuentra la posicion en el que esta la letra contando desde 0
print(texto.count("a")) # cuenta las veces existe en el texto lo que se ponga en ""

textoFinal = texto.replace("o", "0")# remplaza las cosas del texto
print(textoFinal)
valor = texto.isnumeric() #arroja un true o flase si es numero
print(valor)
cadenaSeparada = texto.split(" ") # crea una especie de arreglo con el texto 
print(cadenaSeparada)