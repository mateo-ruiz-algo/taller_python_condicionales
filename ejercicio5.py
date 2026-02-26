#calificar notas de estudiantes
def calificaciones():
    n1 = int(input('Ingresar la primera nota: '))
    if n1 not in range(0, 100+1):
        print("ERROR!: La nota no está en el rango de 0-100 la nota")
        exit()
    
    n2 = int(input('Ingresar la segunda nota: '))
    if n2 not in range(0, 100+1):
        print("ERROR!: La nota no está en el rango de 0-100 la nota")
        exit()
    
    n3 = int(input('Ingresar la tercera nota: '))
    if n3 not in range(0, 100+1): 
        print("ERROR!: La nota no está en el rango de 0-100 la nota")
        exit()

    lista = []
    lista.append(n1)
    lista.append(n2)
    lista.append(n3)
    for nota in lista:
        if nota in range(90, 100+1):
            Estado =  'Excelente'
        elif nota in range(80, 89+1):
            Estado =  'Muy Bueno'
        elif nota in range(70, 79+1):
            Estado =  'Bueno'
        elif nota in range(60, 69+1):
            Estado =  'Supletorio'
        else:
            Estado = 'Reprobado'

    promedio = sum(lista)/len(lista)
    print(f"Las notas ingresadas fueron: \n- Primera nota {n1} \n- Segunda nota {n2} \n- Tercera nota {n3}")
    print(f"El promedio de las calificaciones es: {promedio}")
    print(f'En resumen: \n- {n1} es {Estado} \n- {n2} es {Estado} \n- {n3} es {Estado} ')

calificaciones()