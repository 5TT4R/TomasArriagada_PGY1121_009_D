import numpy,os,time,funciones
lista_ruts = []
while True:
    lista_ruts.sort()
    funciones.menu()
    opc = funciones.validar_opcion()
    if opc == 1:
        l_total_p = funciones.comprar_entrada()
        lista_ruts.append(l_total_p[-1])
        l_total_p.pop()
    elif opc == 2:
        funciones.m_ubicaciones()
    elif opc == 3:
        print(lista_ruts)
        time.sleep(3)
        os.system("cls")
    elif opc == 4:
        funciones.g_totales()
    else:
        f = input("Desea Salir? (S/N)")
        if f.upper() == "S":
            os.system("cls")
            print("Cerrando")
            time.sleep(2)
            os.system("cls")
            print("Cerrando.")
            time.sleep(2)
            os.system("cls")
            print("Cerrando..")
            time.sleep(2)
            os.system("cls")
            print("Tomás Arriagada     06-07-2023")
            break
        elif f.upper() == "N":
            pass
