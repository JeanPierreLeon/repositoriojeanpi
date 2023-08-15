from apoyo import ingresar_entero_mayor_que, mostrar_mensaje

VALOR_MINIMO=0

def main():
    dias=ingresar_entero_mayor_que("Ingrese los dias que se va a hospedar: ", VALOR_MINIMO)
    mensaje=generar_mensaje_pagar(dias)
    mostrar_mensaje(mensaje)
    
def generar_mensaje_pagar(dias):
    if dias >= 0 and dias <= 4:
        mensaje=f"Su descuento es del 8% y el valor a pagar por noche es de 80.000"
        
    elif dias >= 5 and dias <= 8:
        mensaje=f"Su descuento es del 15% y el valor a pagar por noche es de 75.000"
    
    elif dias >= 8 and dias <= 10:
        mensaje=f"Su descuento es del 20% y el valor a pagar por noche es de 35.000"  
        
    else:
        mensaje=f"No tenemos ningun descuento para los dias que se va a quedar"
    return mensaje


main()

    