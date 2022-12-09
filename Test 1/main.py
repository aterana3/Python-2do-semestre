import json

archivo = open("directorio.json")
contenido = json.load(archivo)
cargos_registrados = []
departamentos_registrados = []
personal = []

def run():
    crearDepartamentos()
    crearCargos()
    crearPersonal()
    imprimir()


def crearCargos():
    for persona in contenido:
        cargo = persona['cargo']
        if cargo not in cargos_registrados:
            cargos_registrados.append(cargo)


def crearDepartamentos():
    for persona in contenido:
        departamento = persona['departamento']
        if departamento not in departamentos_registrados:
            departamentos_registrados.append(departamento)


def crearPersonal():
    for persona in contenido:
        apellidos = persona['apellidos']
        nombres = persona['nombres']
        datos = {
            'apellidos': apellidos,
            'nombres': nombres,
            'cargos': [],
            'departamentos': [],
        }
        if datos not in personal:
            personal.append(datos)
    cargarCargos()
    cargarDepartamentos()


def cargarCargos():
    for persona in personal:
        apellidos = persona['apellidos']
        nombres = persona['nombres']
        cargos = persona['cargos'];
        for docente in contenido:
            cargo = docente['cargo']
            if docente['nombres'] == nombres and docente['apellidos'] == apellidos:
                cargos.append(cargo);


def cargarDepartamentos():
    for persona in personal:
        apellidos = persona['apellidos']
        nombres = persona['nombres']
        departamentos = persona['departamentos'];
        for docente in contenido:
            departamento = docente['departamento']
            if docente['nombres'] == nombres and docente['apellidos'] == apellidos:
                departamentos.append(departamento);


def imprimir():
    for persona in personal:
        apellidos = persona['apellidos']
        nombres = persona['nombres']
        departamentos = persona['departamentos']
        cargos = persona['cargos']
        print("")
        print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
        print(f"{nombres} {apellidos}")
        print(f"Cargos:")
        for cargo in cargos:
            print(f"{cargo}")
        print("")

        print(f"Departamentos:")
        for departamento in departamentos:
            print(f"{departamento}")
        print("")
        print(f"Total de departamentos trabajados: {len(departamentos)}")
        print(f"Total de cargos trabajados: {len(cargos)}")
        print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
    print(f"Total de usuarios registrados: {len(personal)}")
    print("")

    print("")
    print("Lista de departamentos registrados")
    for departamento in departamentos_registrados:
        print(f"{departamento}")
    print(f"Total de departamentos: {len(departamentos_registrados)}")
    print("")

    print("")
    print("Lista de cargos registrados")
    for cargo in cargos_registrados:
        print(f"{cargo}")
    print(f"Total de cargos: {len(cargos_registrados)}")
    print("")


if __name__ == "__main__":
    run()