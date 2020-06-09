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
            'last_name2': 'Ramírez',
        },
        'title': '',
        'organization': '',
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
            'cellphone': 7440192543,
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
for registro in agenda:
    print(f'{registro["name"]["first_name"]} {registro["name"]["last_name"]}, {registro["title"]}\n{registro["organization"]}')
    print('\n')
