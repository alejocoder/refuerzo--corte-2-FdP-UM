
# Función para cifrar una palabra
def cifrar_palabra(palabra, letras, cifrado):
    palabra_cifrada = ""
    for letra in palabra:
        if letra in letras:
            indice = letras.index(letra)
            palabra_cifrada += cifrado[indice]
        else:
            palabra_cifrada += letra

    return palabra_cifrada

# Función para descifrar una palabra
def decifrar_palabra(palabra_cifrada, letras, cifrado):
    palabra = ""
    for caracter in palabra_cifrada:
        if caracter in cifrado:
            indice = cifrado.index(caracter)
            palabra += letras[indice]
        else:
            palabra += caracter

    return palabra

# Función principal del programa
def main():
    # Abecedario en mayúsculas y minúsculas, y espacio
    letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
    # Cifrado correspondiente
    cifrado = ["@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", "|", "1", ":", ";", "12", "<", ">", ",", ".", "/", "3", "~", "`", "!", "¡", "¿", "§", "¶", "4", "ª", "º", "°", "¤", "¢", "£", "¥", "5", "©", "®", "6", "µ", "7", "8", "9", "0"]

    while True:
        print("\nMENU:")
        print("1. Cifrar palabra")
        print("2. Descifrar palabra")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            palabra_original = input("Digite una palabra para cifrar: ")
            palabra_cifrada = cifrar_palabra(palabra_original, letras, cifrado)
            print("Palabra cifrada:", palabra_cifrada)
        elif opcion == '2':
            palabra_cifrada = input("Digite una palabra cifrada para descifrar: ")
            palabra_descifrada = decifrar_palabra(palabra_cifrada, letras, cifrado)
            print("Palabra descifrada:", palabra_descifrada)
        elif opcion == '3':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    main()