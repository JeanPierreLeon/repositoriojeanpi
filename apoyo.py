def ingresar_texto(mensaje):
    texto=input(mensaje)
    return texto

def ingresar_entero(mensaje):
    repetir=True
    valor=None
    while repetir:
        try:
            valor=int(input(mensaje))
            repetir=False
        except:
            print("La variable a ingresar no es un numero entero")
    return valor

def mostrar_mensaje(mensaje):
	print(mensaje)
        
def ingresar_real(mensaje):
    valor=None
    repetir= True
    while repetir:
        try:
            valor=float(input(mensaje))
            repetir=False
        except:
            print("La variable a ingresar no es un numero real")
    return valor

def generar_tabla(numero_tabla,valor_minimo,valor_maximo):
    tabla=f"\n la tabla de multiplicar del {numero_tabla}\n\n"
    i=valor_minimo
    while i<=valor_maximo:
        producto = numero_tabla * i
        tabla+=f"{numero_tabla:2d} x {i:2d} = {producto:3d}\n"
        i=i+1
    return tabla

def ingresar_entero_mayor_que(mensaje,valor_minimo):
    valor=None
    repetir= True
    while repetir:
        valor=ingresar_entero(mensaje)
        if valor <= valor_minimo:
            print("El valor {valor} no es mayor que {valor_minimo}")
        else:
            repetir=False
    return valor

def ingresar_real_mayor_que(mensaje,valor_minimo):
    valor=None
    repetir=True
    while repetir:
        valor=ingresar_real(mensaje)
        if valor<=valor_minimo:
            print("El valor{valor} no es mayor que {valor_minimo}")
        else:
            repetir=False
    return valor

def generar_tablas(valor_inicial,valor_final,minimo_valor_tabla,maximo_valor_tabla):
    mensaje_tablas=f"Las tablas entre {valor_inicial} y {valor_final}\n\n"
    i=valor_inicial
    while i<=valor_final:
        mensaje_tablas+=generar_tabla(i,minimo_valor_tabla,maximo_valor_tabla)
        i=i+1
    return mensaje_tablas

def ingresar_entero_rango(mensaje,valor_minimo,valor_maximo):
    valor=None
    repetir=True
    while repetir:
        valor=ingresar_entero(mensaje)
        if valor<valor_minimo or valor>=valor_maximo:
            print(f"el valor no esta entre {valor_minimo} y {valor_maximo}")
        else:
            repetir=False
    return valor

def ingresar_real_rango(mensaje,valor_minimo,valor_maximo):
    valor=None
    repetir=True
    while repetir:

        valor=ingresar_real(mensaje)
        if valor<valor_minimo or valor >valor_maximo:
            print(f"el valor no esta entre {valor_minimo} y {valor_maximo}")
        else:
            repetir=False
    return valor

def calcular_sucesion(n):
        suma=0
        for i in range(0,n):
            if i%2==0:
                suma += -2*i
            else:
                suma += 3*(i+2)
        return suma

def ingresar_n_reales_rango(mensaje, cantidad, valor_minimo, valor_maximo):
    valores=[0.0]*cantidad
    for i in range(0,len(valores)):
        valores[i]=ingresar_real_rango(f"{mensaje} ({i+1} de {cantidad}):",valor_minimo, valor_maximo)
    return valores

def ingresar_n_enteros_rango(mensaje, cantidad, valor_minimo, valor_maximo):
    valores=[0.0]*cantidad
    for i in range(0,len(valores)):
        valores[i]=ingresar_entero_rango(f"{mensaje} ({i+1} de {cantidad}):",valor_minimo, valor_maximo)
    return valores

def ingresar_n_cadenas(mensaje,cantidad):
    textos=[""]*cantidad
    for i in range (0, len(textos)):
        textos[i] = ingresar_texto(f"{mensaje} ({i+1} de {cantidad}):")
    return textos

def ingresar_n_enteros_mayor_que(mensaje, cantidad, valor):
    valores=[]
    for i in range(0,cantidad):
        valores.append(ingresar_entero_mayor_que(mensaje, valor))
    return valores

def obtener_id_impares(lista):
    lista_impares=[]
    for i in range(0,len(lista)):
        if lista [i]%2!=0:
            lista_impares+=[i]
    return lista_impares

def obtener_indices_mayores_iguales_que(lista_valores,valor_referencia):
    lista_indices=[]
    for i in range(0, len(lista_valores)):
        if lista_valores[i]>= valor_referencia:
            lista_indices += [i]
    return lista_indices

def obtener_indices_menores_que(lista_valores,valor_referencia):
    lista_indices=[]
    for i in range(0, len(lista_valores)):
        if lista_valores[i] < valor_referencia:
            lista_indices += [i]
    return lista_indices

def obtener_mayor_elemento(lista):
    numero_mayor = 0
    for valor in lista:
        if valor > numero_mayor:
            numero_mayor = valor
    return numero_mayor 

def obtener_menor_elemento(lista):
    numero_menor = lista[0]
    for valor in lista:
        if valor < numero_menor:
            numero_menor = valor
    return numero_menor

def calcular_promedio_lista(lista, indices):
    suma=0
    for indice in indices:
        suma += lista [indice]
    promedio = suma / len(indices)
    return promedio

def generar_mensaje_pais(nombres,nombres_paises,paises,titulo):
    mensaje=f"{titulo}\n"
    cantidad_paises=0
    for i in range(0,len(nombres_paises)):
        if nombres_paises[i]==paises:
            mensaje+=f"{nombres[i]}\n"
            cantidad_paises+=1
    mensaje+=f"\n cantidad {cantidad_paises}\n"
    return mensaje

def obtener_elementos_indice(lista, indices):
    mensaje=""
    for i in indices:
        mensaje+= f"{lista[i]}\n"
    return mensaje

def obtener_indices_rango(lista, valor_minimo, valor_maximo):
    lista_indices = []
    for i in range(0, len(lista)):
        if lista[i] >= valor_minimo and lista[i] <= valor_maximo:
            lista_indices += [i]
    return lista_indices

def obtener_indices_igual_que(lista_valores,valor_referencia):
    lista_indices=[]
    for i in range(0, len(lista_valores)):
        if lista_valores[i] == valor_referencia:
            lista_indices += [i]
    return lista_indices