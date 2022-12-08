#Autor: Anthony Emiliano Terán Arellano
#Version: 1.0.0

import json

archivo = open("publicacion.json")
contenido = json.load(archivo)
profesores = []

def construir():
    for docente in contenido:
        cedula = docente['cedula']
        apellidos = docente['apellidos']
        datos = {
            'cedula': cedula,
            'apellidos': apellidos,
            'publicaciones': 0,
            'tipos': [],
            'areas': []
        }
        if datos not in profesores:
            profesores.append(datos)
    publicaciones()
    areas()
    imprimir()


def publicaciones():
    for docente in profesores:
        cedula = docente['cedula']
        for profesor in contenido:
            if profesor['cedula'] == cedula:
                docente['publicaciones'] += 1


def areas():
    for docentes in profesores:
          cedula = docentes['cedula']
          areas_trabajadas = docentes['areas']
          for profesor in contenido:
            if profesor['cedula'] == cedula:
                area = profesor['area']
                if not area in areas_trabajadas:
                   areas_trabajadas.append(area);


def imprimir():
    for docente in profesores:
        print(" ")
        print("==========================")
        print(f"Nombre: {docente['apellidos']}")
        print(f"Cedula: {docente['cedula']}")
        print(f"Publicaciones: {docente['publicaciones']}")
        areas = docente['areas'];
        print('Areas trabajadas:')
        for key in areas:
            print(key)
        print("==========================")
        print(" ")


if __name__ == "__main__":
    construir();
