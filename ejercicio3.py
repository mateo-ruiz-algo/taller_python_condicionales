#Posee descuento o no
def descuento_en_cliente():
    subtotal = float(input("Ingrese el subtotal: "))
    descuento = 0
    tipo_cliente = input("Usted es cliente vip o regular: ").lower()
    if tipo_cliente == 'vip':
        print("Usted posee un 15%")
        
        descuento = subtotal*0.15

    elif tipo_cliente == 'regular':
        print("Si su compra fue igual o mayor a $100 posee un 5% de descuento ")
        if subtotal >= 100:
            descuento = subtotal*0.05
        else:
            print('Cliente no válido')

    promo = round(descuento, 2)

    total = round(subtotal-promo, 2)
    print(f"- Subotal: {subtotal} \n- Descuento aplicado: {promo} \n- Total final: {total}")

descuento_en_cliente()
