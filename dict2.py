dic = [
    {
        "lang": "en",
        "arbol": "Tree",
        "perro": "Dog",
        "casa": "House",
        "lapiz": "Pencil",
        "calle": "Street",
    },
    {
        "lang": "fr",
        "arbol": "Arbre",
        "perro": "Chien",
        "casa": "Maison",
        "lapiz": "Crayon",
        "calle": "Rue",
    },
    {
        "lang": "ch",
        "arbol": "树木",
        "perro": "狗",
        "casa": "宅",
        "lapiz": "铅笔",
        "calle": "街头",
    },
    {
        "lang": "ru",
        "arbol": "дерево",
        "perro": "собака",
        "casa": "дом",
        "lapiz": "карандаш",
        "calle": "улица",
    },
    {
        "mascota": "Perro",
        "pez": "Payaso",
        "herramienta": "Martillo"
    }
]

# Obtener la longitud de un diccionario
# print(len(dic[2]))
# print(len(dic[-1]))

# Copiar un diccionario
nuevo_dic = dic[-1].copy()
nuevo_dic[3.1415927] = "PI"
# print(dic)
print('\nnuevo: \n', nuevo_dic)

# Crear un diccionario a partir de otros diccionarios

dic2 = {"computadora": "dell", "teléfono": "huawei", }
dic3 = {"tv": "LG", "refigerador": "daewoo", }

mas_nuevo_dic = {"primero": nuevo_dic, "segundo": dic2, "tercero": dic3}
# print('\nmas nuevo: \n', mas_nuevo_dic)

# Iterar un diccionario
# Mostramos las keys de nuevo_dic
# for element in nuevo_dic:
#     print(element)

# # Mostramos los values de nuevo_dic
# for element in nuevo_dic:
#     print(nuevo_dic[element])

# # Mostramos llaves y valores del diccionario
# for element in nuevo_dic:
#     print(f'{element}: {nuevo_dic[element]}')

# print(nuevo_dic.items())
# x = list(nuevo_dic.items())
# print(dict(mascota=x[0][1]))

# Mostrar las llaves de un diccionario
# print(len(nuevo_dic.keys()))
# print(list(dic[-2].keys()))
print(len(dic[-2].keys()))

# Mostrar los valores de un diccionario
print(nuevo_dic.values())

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

agenda = {
    "key1": "value1",
    "key2": 1234567890,
    "key3": {
        "subkey1": "subvalue1"
    }
}
