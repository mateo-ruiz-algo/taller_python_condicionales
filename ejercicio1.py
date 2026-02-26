#Pedir datos al usuario
def identificar_usuario():
    nombre = input('Ingrese su nombre: ')
    edad = int(input("¿Cuál es su edad?: "))
    ciudad = input("¿En cuál ciudad vive?: ")

    print(f"Hola {nombre}, tienes {edad} años, y vives en {ciudad}")

identificar_usuario()
