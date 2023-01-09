#Autor: Anthony Terán Arellano
#Version 1.0

# Hacer un diccionario de sistema becario

#Academicas: Promedio de 95 - 100 y Asistencia de asignaturas >= 90% y deudas de 0.

#Situacion vulnerable: Estado socio economico bajo o medio bajo y Asistencia de asignaturas >= 90%, Promedio de 80 - 100
# y deudas de 0

estudiantes = [{'nombre': 'Anthony', 'carrera': 'Software', 'sexo': 'H', 'estado': 'Medio', 'deuda': 0, 'promedio': 80,
                'asistencia': 92, 'beca': False, 'tipo': ''},
               {'nombre': 'Kendryd', 'carrera': 'Software', 'sexo': 'H', 'estado': 'Medio', 'deuda': 25.50,
                'promedio': 90, 'asistencia': 100, 'beca': False, 'tipo': ''},
               {'nombre': 'Elkin', 'carrera': 'Software', 'sexo': 'H', 'estado': 'Medio bajo', 'deuda': 15.50,
                'promedio': 79, 'asistencia': 85, 'beca': False, 'tipo': ''},
               {'nombre': 'Mikel', 'carrera': 'Software', 'sexo': 'H', 'estado': 'Medio bajo', 'deuda': 0,
                'promedio': 77, 'asistencia': 95, 'beca': False, 'tipo': ''},
               {'nombre': 'Josue', 'carrera': 'Derecho', 'sexo': 'H', 'estado': 'Medio alto', 'deuda': 0,
                'promedio': 95, 'asistencia': 90, 'beca': False, 'tipo': ''},
               {'nombre': 'Emerson', 'carrera': 'Software', 'sexo': 'H', 'estado': 'Medio alto', 'deuda': 50.25,
                'promedio': 72, 'asistencia': 70, 'beca': False, 'tipo': ''},
               {'nombre': 'Maria', 'carrera': 'Contabilidad', 'sexo': 'M', 'estado': 'Medio bajo', 'deuda': 0,
                'promedio': 75, 'asistencia': 79, 'beca': False, 'tipo': ''},
               {'nombre': 'Ivan', 'carrera': 'Industrial', 'sexo': 'H', 'estado': 'Medio alto', 'deuda': 50.25,
                'promedio': 82, 'asistencia': 85, 'beca': False, 'tipo': ''},
               {'nombre': 'Daniela', 'carrera': 'Derecho', 'sexo': 'M', 'estado': 'Medio bajo', 'deuda': 0,
                'promedio': 90, 'asistencia': 100, 'beca': False, 'tipo': ''},
               {'nombre': 'Freddy', 'carrera': 'Derecho', 'sexo': 'M', 'estado': 'Medio bajo', 'deuda': 0,
                'promedio': 90, 'asistencia': 100, 'beca': False, 'tipo': ''}
               ]


def beca_academica():
    for i in estudiantes:
        nombre = i['nombre']
        carrera = i['carrera']
        promedio = i['promedio']
        asistencia = i['asistencia']
        deuda = i['deuda']

        cumple_prom = (95 <= promedio <= 100)
        cumple_asis = (90 <= asistencia <= 100)
        cumple_deud = (deuda == 0)
        if cumple_prom and cumple_asis and cumple_deud:
            i['beca'] = True
            i['tipo'] = 'Academica'
            print(f"{nombre} estudiante de {carrera} ha obtenido la beca tipo {i['tipo']}")


def beca_socioeconomica():
    for i in estudiantes:
        nombre = i['nombre']
        carrera = i['carrera']
        promedio = i['promedio']
        asistencia = i['asistencia']
        deuda = i['deuda']
        estado = i['estado']
        beca = i['beca']

        cumple_prom = (80 <= promedio <= 100)
        cumple_asis = (90 <= asistencia <= 100)
        cumple_deud = (deuda == 0)
        cumple_esta = (estado == "Bajo" or estado == "Medio bajo")
        cumple_beca = (beca == False)
        if cumple_prom and cumple_asis and cumple_deud and cumple_esta and cumple_beca:
            i['beca'] = True
            i['tipo'] = 'Socioeconomica'
            print(f"{nombre} estudiante de {carrera} ha obtenido la beca tipo {i['tipo']}")


if __name__ == "__main__":
    print(f"Lista de alumnos con becas aceptadas:")
    beca_academica();
    beca_socioeconomica();
