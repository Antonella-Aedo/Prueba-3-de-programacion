from utilidades import menu, registrar, buscar_alumno, listar_alumnos
listas_alumnos=[]
while True:
    try:
        menu()
        op= int(input("ingrese opcion: "))
        if op == 1:
            listas_alumnos.append(registrar())
        elif op==2:
            listar_alumnos(listas_alumnos)
        elif op==3:
            buscar_alumno(listas_alumnos)


        elif op== 5:
            print("saliste del rpograma")
            break
        else:
            print("opcion invalida, opciones desde el 1 hasta 5. ")
    except ValueError:
        print("solo numeros")