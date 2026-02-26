#Tarifa del taxi
def calcular_viaje():
    distancia_recorrida = float(input('¿Cuántos km viajaste en el taxi?: '))
    tarifa_base = 1
    if distancia_recorrida >= 10:
        print("La tarifa base es de $2")
        tarifa_base = 2

    hora_viaje = int(input('Ingrese la hora de viaje (SOLO HORAS NO MINUTOS: '))
    while hora_viaje not in range (0, 23+1):
        print("ERROR!: Es una hora inválida, intenta otra vez")
        hora_viaje = int(input('Ingrese la hora de viaje (SOLO HORAS NO MINUTOS: )'))
    if hora_viaje in range(9, 19+1):
        horario = 'Diurno'
        costo_viaje = 0.50 
        costo_total = tarifa_base + distancia_recorrida*costo_viaje
    elif hora_viaje in range(20, 23+1) or hora_viaje in range(0, 5+1):
        costo_viaje = 0.65
        costo_total = tarifa_base + distancia_recorrida*costo_viaje
        horario = 'Nocturno'
    else: 
        print("???")
    
    print(f'- Horario: {horario} \n- Distancia: {distancia_recorrida} \n- Costo a pagar: {costo_total}')
    
calcular_viaje()
