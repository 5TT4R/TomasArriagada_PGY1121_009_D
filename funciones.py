import os,time,numpy

def menu():
    os.system("cls")
    print("""
    1. Comprar Entradas
    2. Mostrar Ubicaciónes disponibles
    3. Ver listado de asistentes
    4. Mostrar ganancias totales
    5. Salir""")

def validar_opcion():
    while True:
        try:
            opc = int(input("Ingrese opción: "))
            if opc in (1,2,3,4,5):
                break
            else:
                print("ERROR DEBE INGRESAR UNA OPCIÓN VALIDA")
        except:
            print("ERROR DEBE INGRESAR UN NÚMERO ENTERO")
    return opc
ubicaciones = numpy.zeros([10,10],int,)
lista_ruts = []
platinum = 120000
gold = 80000
silver = 50000


l_total_p = [0,0,0,[0,0],[0,0]]


def m_ubicaciones():
    print("ESCENARIO")
    for x in range(len(ubicaciones)):
        print(f"Fila {x+1}    ",end="")
        for y in range(len(ubicaciones[x])):
            print(ubicaciones[x][y],end="")
        print("")
    time.sleep(4)
    os.system("cls")

def g_totales():
    print(f"""
    Tipo de entrada          cantidad                total
    platinum ${platinum}              {l_total_p[0]}                   ${l_total_p[1]}
    
    gold ${gold}                   {l_total_p[3][0]}                   ${l_total_p[3][1]}
    
    silver ${silver}                 {l_total_p[4][0]}                   ${l_total_p[4][1]}
    --------------------------------------------------------------------------------------------------------------------------
    
    TOTAL                         {l_total_p[4][0]+l_total_p[3][0]+l_total_p[0]}                  ${l_total_p[4][1]+l_total_p[3][1]+l_total_p[1]}   """)  
    time.sleep(4)
    os.system("cls")


def comprar_entrada():
    platinum = 120000
    gold = 80000
    silver = 50000

    if 0 not in ubicaciones:
        print("SALA LLENA VUELVA MÁS TARDE")
    else:
        cantidad = validar_cantidad()
        m_ubicaciones()
        for x in range(cantidad):
            while True:
                fila = validar_fila()
                columna = validar_columna()
                if ubicaciones[fila-1][columna-1] == 1:
                    print("ASIENTO OCUPADO ELIGA OTRO")
                else:
                    if fila == 1 or fila == 2:
                        l_total_p[2] = l_total_p[2] + platinum
                        l_total_p[0] += 1
                        l_total_p[1]+=platinum
                    elif fila == 3 or fila == 4 or fila == 5:
                        l_total_p[2] += gold
                        l_total_p[3][0] +=1
                        l_total_p[3][1]+=gold
                    elif fila == 6 or fila == 7 or fila == 8 or fila == 9 or fila == 10:
                        l_total_p[2] +=silver
                        l_total_p[4][0]+=1
                        l_total_p[4][1]+=gold
                    ubicaciones[fila-1][columna-1] = 1
                    break
        run = validar_run()
        l_total_p.append(run)        
        print("COMPRA REALIZADA CON ÉXITO")
        time.sleep(4)
        os.system("cls")
        return l_total_p
            

def validar_fila():
    while True:
        try:
            fila = int(input("Ingrese fila: "))
            if fila in (1,2,3,4,5,6,7,8,9,10):
                break
            else:
                print("ERROR FILA NO EXISTE")
        except:           
            print("ERROR DEBE INGRESAR UN NÚMERO ENTERO")
    return fila

def validar_columna():
    while True:
        try:
            columna = int(input("Ingrese columna: "))
            if columna in (1,2,3,4,5,6,7,8,9,10):
                break
            else:
                print("ERROR columna NO EXISTE")
        except:           
            print("ERROR DEBE INGRESAR UN NÚMERO ENTERO")
    return columna



def validar_cantidad():
    while True:
        try:
            cantidad = int(input("Ingrese cantidad de entradas(de 1 a 3):"))
            if cantidad in (1,2,3):
                break
            else:
                print("ERROR DEBE INGRESAR UNA CANTIDAD DE 1 A 3")
        except:
            print("ERROR DEBE INGRESAR UN NUMERO ENTERO")
    return cantidad

def validar_run():
    while True:
        try:
            run = int(input("Ingrese run(sin guion, puntos ni dígito verificador): "))
            if len(str(run)) >= 7 and len(str(run)) <=9:
                break
            else:
                print("ERROR RUN NO VALIDO")
        except:
            print("ERROR DEBE INGRESAR UN NUMERO ENTERO")
    return run

