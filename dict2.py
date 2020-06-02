# keys : values
# int  : int
# float: float
# str  : str
# ...

dic = {} # Declaración de un diccionario

lista = [
  1,
  "a",
  1.4
]

dic = {
  "nombre": "Manuel",
  "apellido_pat": "Gómez",
  "apellido_mat": "Rodríguez",
  10: "Diez",
  3.1415927: "Pi",
  "nombre1": "Pedro",
  "nombre2": "Pablo"
}
# NUNCA se deben duplicar las llaves en un diccionario, esto evita la ambigüedad
# Acceder a los valores de un diccionario
# print(dic[10])
# print(dic[3.1415927])
# print(dic["nombre"])
# print(dic["apellido_mat"])

dic = [
  {
    "nombre": "Manuel",
    "edad": 20,
    "ciudad": "Acapulco",
  },
  {
    "nombre": "Pablo",
    "edad": 19,
    "ciudad": "Altamirano"
  },
  {
    "nombre": "Pedro",
    "edad": 18,
    "ciudad": "San Marcos"
  }
]

dic[2]["estado"] = "Guerrero" # Agrega una nueva llave al tercer diccionario
dic[2]["edad"] = 22

# Iterar sobre un diccionario
for monito in dic:
  print(f'Nombre: {monito["nombre"]}')
  print(f'Edad: {monito["edad"]}')
  print(f'Ciudad: {monito["ciudad"]}\n')

dic[1].pop("ciudad")
del dic[0]["nombre"]

dic[1].clear()

for monito in dic:
  for key, value in monito.items():
    print(f'{key}: {value}')
  print('\n')

#
# Pedir al usuario una palabra de un menú de palabras (al menos 5) y dar su traducción en 
# uno de los siguientes idiomas:
# Inglés, Francés, Chino (simplificado), Ruso
#

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
]

print('''
      Elige una palabra de la siguiente lista:
      1) Árbol
      2) Perro
      3) Casa
      4) Lápiz
      5) Calle
''')
opc = int(input('Elige una opción del menú: '))
print('''
      A qué idioma quieres traducir:
      1) Inglés
      2) Francés
      3) Chino
      4) Ruso
''')
opc2 = int(input('Elige una opción del menú: '))

if opc == 1: key = "arbol"
elif opc == 2: key = "perro"
elif opc == 3: key = "casa"
elif opc == 4: key = "lapiz"
elif opc == 5: key = "calle"

if opc2 == 1: lang = "en"
elif opc2 == 2: lang = "fr"
elif opc2 == 3: lang = "ch"
elif opc2 == 4: lang = "ru"

for trad in dic:
  if trad["lang"] == lang:
    print(f'Traducción: {trad[key]}')
    break

# Tarea:
# Pedir al usuario el nombre de una moneda y mostrar su símbolo
# correspondiente, en caso de que la moneda no exista, preguntar al usuario si desea
# agregarla junto con su símbolo