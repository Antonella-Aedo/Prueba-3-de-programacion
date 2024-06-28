import math
def registrar():
    listas_notas= []
    nombre=input("ingrese su nombre: ")
    apellido=input("ingrese su apellido: ")
    edad=int(input("ingrese su edad: "))
    nivel=int(input("ingresa el nivel: "))
    while True:
        notas=int(input("ingrese todas sus notas, cuando acabe ingrese 0: "))
        if notas == 0:
           break
        else:
            listas_notas.append(notas)
            print(f"notas:{listas_notas}")
            print(sum(listas_notas))
    alumnos= {
        "nombre": nombre,
        "apellido": apellido ,
        "edad": edad,
        "nivel": nivel,
        "notas": listas_notas
    }
    return alumnos
def menu():
    print("menu")
    print("1) Registro de alumno")
    print("2) listar todos los alumnos")
    print("3) Buscar alumnos por nivel")
    print("4) Calcular la nota promedio por alumno")
    print("5) Salir del programa")

def buscar_alumno(lista):
    Nivel=int(input("ingrese el nivel que quiere buscar: "))
    for i in range(len(lista)):
        if Nivel ==lista[i]['nivel']:
            print(f"Nivel: {lista[i]['nivel']}")
            print(f"Nombre: {lista[i]['nombre']}")
            print(f"Apellido{lista[i]['apellido']}")
            print(f"Edad{lista[i]['edad']}")
            print(f"notas: {lista[i]['notas']}")
            print()
    else:
        print("no se encuentra el nivel que busca")

def listar_alumnos(lista):
    for i in range(len(lista)):
        print(f"alumno {i+1}")
        print(f"Nivel: {lista[i]['nivel']}")
        print(f"Nombre: {lista[i]['nombre']}")
        print(f"Apellido: {lista[i]['apellido']}")
        print(f"Edad: {lista[i]['edad']}")
        print(f"notas: {lista[i]['notas']}")
        print()


def agregar_documento(lista):
    with open("documento.txt", "w") as archivo:
        for i in lista:
            x= f"{i['nombre']},{i['apellido']}, {i['edad']}, {i['nivel']}, {i['notas']}"
            archivo.write(x)