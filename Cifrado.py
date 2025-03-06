# Función para cifrar el texto
def Cifrar_Contraseña(clave):
    abecedario = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789"
    abecedario_lista = list(abecedario)
    texto_lista = list(clave)

    i = 0
    while i < len(texto_lista):
        if texto_lista[i] in abecedario_lista:
            indice = abecedario_lista.index(texto_lista[i])
            texto_lista[i] = abecedario_lista[(indice + 3) % len(abecedario_lista)]
        i += 1

    resultado = ""
    for caracter in texto_lista:
        resultado += caracter  # Construir manualmente la cadena cifrada
    return resultado

# Función para descifrar el texto (test)
def Descifrar_Contraseña(clave):
    abecedario = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789"
    abecedario_lista = list(abecedario)
    texto_lista = list(clave)

    i = 0
    while i < len(texto_lista):
        if texto_lista[i] in abecedario_lista:
            indice = abecedario_lista.index(texto_lista[i])
            texto_lista[i] = abecedario_lista[(indice - 3) % len(abecedario_lista)]
        i += 1

    resultado = ""
    for caracter in texto_lista:
        resultado += caracter  # Construir manualmente la cadena descifrada
    return resultado


#Esta linea tanto como la funcion "Descrifrar_Contraseña" solo sirven de test
# texto = input("Ingrese el texto a descrifrar: ")
# texto_descifrado = Descifrar_Contraseña(texto)
# print(texto_descifrado)

texto = "fdvlwdurmd"
texto_cifrafo = Cifrar_Contraseña(texto)
print(texto_cifrafo)