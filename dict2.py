# Agenda telefónica moderna
# Datos necesarios:
# - Nombre
# - Segundo nombre
# - Apellido paterno
# - Apellido materno
# - Título
# - Organización
# - Tipo de número (celular, laboral, particular, principal,...)
# - Número(s) de teléfono(s)
# - Tipo de Correo electrónico (particular, laboral, otro)
# - Correo(s) electrónico(s)
# - Notas
# - Grupo
# - Sobrenombre
# - Cumpleaños
# - Relación
import datetime

agenda = [
    {
        'name': {
            'first_name': 'Juan',
            'second_name': 'Arturo',
            'last_name': 'González',
            'last_name2': 'Gutiérrez',
        },
        'title': '',
        'organization': 'FacMat',
        'phone_number': {
            'cellphone': 7448372684,
            'work': 7447228192,
            'home': 7441003745,
        },
        'email': {
            'personal': 'juanito29@gmail.com',
            'work': 'jagonzalez@trabajo.com',
            'other': 'elneneconsentido@gmail.com',
        },
        'notes': ['Reprobarlo este semestre', 'Pasarlo en el que sigue'],
        'groups': [],
        'nickname': 'Prieto',
        'birthday': datetime.date(2000, 6, 1),
        'relationship': 'Alumno',
    },
    {
        'name': {
            'first_name': 'Camilo',
            'second_name': '',
            'last_name': 'Santiago',
            'last_name2': 'Gutiérrez',
        },
        'title': 'Profesor',
        'organization': 'Facultad de Matemáticas',
        'phone_number': {
            'cellphone': '',
            'work': 7449301548,
            'home': 7440192846,
        },
        'email': {
            'personal': 'camilosantiago@gmail.com',
            'work': 'csantiago@otrotrabajo.com',
            'other': 'elcamilo@gmail.com',
        },
        'notes': [],
        'groups': ['Profesores'],
        'nickname': 'El camo',
        'birthday': datetime.date(1982, 2, 10),
        'relationship': 'Colega',
    }
]

# Acceder a la subllave 'first_name' del diccionario 'name'
# print(agenda[0]['name']['first_name'])

# Acceder al elemento 2 de la lista de la llave 'notas'
# print(agenda[0]['notes'][1])

# Mostrar primer nombre y primer apellido de todos los registros de la agenda
# for registro in agenda:
#     string = f'{registro["name"]["first_name"][0]}{registro["name"]["last_name"][0]} {registro["name"]["first_name"]} {registro["name"]["last_name"]}'
#     if registro["title"] != "":
#         string += ', ' + registro["title"]
#     if registro["organization"] != "":
#         string += '\n' + registro["organization"]
#     print(string)
#     print()

# Salida de información
# JP Juan Pérez
# FacMat

# CS Camilo Santiago Pérez, Profesor
# Facultad de Matemáticas

# Función de búsqueda que permita al usuario encontrar un registro en la agenda
# por medio del nombre(s) y/o apellido(s)
#

# Juan Manuel Rodríguez

# Escribe el término de búsqueda: Manuel Pérez


def get_names(registro, st):
    if registro["name"]["first_name"].lower() == st.lower() or registro["name"]["second_name"].lower() == st.lower() or registro["name"]["last_name"].lower() == st.lower() or registro["name"]["last_name2"].lower() == st.lower():
        string = f'{registro["name"]["first_name"][0]}{registro["name"]["last_name"][0]} {registro["name"]["first_name"]} {registro["name"]["last_name"]} '
        if registro["phone_number"]["cellphone"] != "":
            string += f'Celular: {registro["phone_number"]["cellphone"]} '
        if registro["phone_number"]["work"] != "":
            string += f'Trabajo: {registro["phone_number"]["work"]} '
        if registro["phone_number"]["home"] != "":
            string += f'Casa: {registro["phone_number"]["home"]} '
        return string
    return False


def search_contact(name):
    if ' ' in name.lower():
        st = name.split(' ')
        for registro in agenda:
            if get_names(registro, st[0]) != False:
                print(get_names(registro, st[0]))
            if get_names(registro, st[0]) == False and get_names(registro, st[1]) != False:
                print(get_names(registro, st[1]))
    else:
        for registro in agenda:
            print(get_names(registro, name))
            print()
    return


search_contact("jaime GUtIérreZ")
