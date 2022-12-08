#Autor: Anthony Emiliano Terán Arellano
#Version: 1.0.0

import json

archivo = open("publicacion.json")
contenido = json.load(archivo)


def filtrar():
    profesores = []
    for personal in contenido:
        cedula = personal['cedula']
        apellidos = personal['apellidos']
        datos = {'cedula': cedula,
                 'apellidos': apellidos,
                 'articulos': 0
                 }
        if datos not in profesores:
             profesores.append(datos)
    for docentes in profesores:
        cedula = docentes['cedula']
        for profesor in contenido:
            if profesor['cedula'] == cedula:
                docentes['articulos'] += 1
    print(profesores)


if __name__ == "__main__":
    filtrar();
