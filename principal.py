import random
import string

def generar_contrasena(longitud=12, usar_mayusculas=True, usar_minusculas=True, usar_numeros=True, usar_simbolos=True):
    # Definir los conjuntos de caracteres
    mayusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = string.punctuation

    # Crear el conjunto de caracteres basado en las opciones
    caracteres = ''
    if usar_mayusculas:
        caracteres += mayusculas
    if usar_minusculas:
        caracteres += minusculas
    if usar_numeros:
        caracteres += numeros
    if usar_simbolos:
        caracteres += simbolos

    # Verificar que al menos un conjunto de caracteres esté seleccionado
    if not caracteres:
        raise ValueError("Debe seleccionar al menos un conjunto de caracteres")

    # Generar la contraseña
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def main():
    print("Bienvenido al Generador de Contraseñas")
    
    while True:
        try:
            longitud = int(input("Ingrese la longitud deseada para la contraseña: "))
            if longitud <= 0:
                raise ValueError("La longitud debe ser un número positivo")
            break
        except ValueError as e:
            print(f"Error: {e}. Intente nuevamente.")

    usar_mayusculas = input("¿Incluir letras mayúsculas? (s/n): ").lower() == 's'
    usar_minusculas = input("¿Incluir letras minúsculas? (s/n): ").lower() == 's'
    usar_numeros = input("¿Incluir números? (s/n): ").lower() == 's'
    usar_simbolos = input("¿Incluir símbolos? (s/n): ").lower() == 's'

    try:
        contrasena = generar_contrasena(longitud, usar_mayusculas, usar_minusculas, usar_numeros, usar_simbolos)
        print(f"\nSu contraseña generada es: {contrasena}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()