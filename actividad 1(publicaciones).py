#Autor: Anthony Emiliano Terán Arellano
#Version: 1.0.0

import json

archivo = open("publicacion.json")
contenido = json.load(archivo)

def filtrar():
    profesores = []
    for profesor in contenido:
        cedula = profesor['cedula']
        apellidos = profesor['apellidos']
        if cedula is not profesores:
            profesores.append({
                'cedula': cedula,
                'apellidos': apellidos,
                'articulos': 0
            })
    for docentes in profesores:
        cedula = docentes['cedula']
        for profesor in contenido:
            if profesor['cedula'] == cedula:
                docentes['articulos'] += 1
    print(profesores[0])


if __name__ == "__main__":
    filtrar();