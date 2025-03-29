# Planificador_comidas_saludables

Explicación del código
Este programa en Python utiliza Programación Orientada a Objetos (POO) para crear un Planificador de Comidas Saludables .
Su propósito es generar menús diarios y semanales de manera aleatoria, así como una lista de compras basada en esos menús.

1️⃣ ClasePlanificadorComidas
Esta clase contiene los métodos y atributos necesarios para generar planos de comida.

Atributos

def __init__(self, tipo_dieta="Omnívora"):
tipo_dieta: Permite especificar el tipo de dieta (ejemplo: vegana, sin gluten). Por defecto, es "Omnívora".

self.ingredientes: Diccionario que almacena categorías de alimentos con su respectivo contenido calórico (por 100g).

2️⃣ Métodogenerar_menu_diario()

def generar_menu_diario(self):
Genera un menú diario con 3 comidas (desayuno, almuerzo y cena), eligiendo aleatoriamente alimentos de cada categoría.

Desayuno :

1 carbohidrato

1 fruta

1 líquido

Almuerzo :

1 verdura

1 proteína

1 carbohidrato

1 grasa saludable

Cena :

1 verdura

1 proteína

1 líquido

Ejemplo de salida para un día:

{
    "Desayuno": ["Quinoa", "Banana", "Leche vegetal"],
    "Almuerzo": ["Brócoli", "Pescado", "Arroz integral", "Aguacate"],
    "Cena": ["Zanahoria", "Tofu", "Infusiones"]
}
3️⃣ Métodogenerar_menu_semanal()

def generar_menu_semanal(self):
Crea un menú semanal generando un menú diario para cada día de la semana.

Devuelve un diccionario con los días de la semana como claves y los menús como valores.

Ejemplo de salida:

Editar
{
    "Lunes": {"Desayuno": [...], "Almuerzo": [...], "Cena": [...]},
    "Martes": {"Desayuno": [...], "Almuerzo": [...], "Cena": [...]},
    ...
}
4️⃣ Métodogenerar_lista_compras()

def generar_lista_compras(self):
Registre el menú semanal y cuente cuántas veces aparece cada ingrediente.

Devuelve un diccionario con los ingredientes y la cantidad total a comprar.

Ejemplo de salida:
{
    "Quinoa": 2,
    "Banana": 3,
    "Brócoli": 4,
    "Pescado": 3,
    "Leche vegetal": 2,
    ...
}
5️⃣ Uso del programa

planificador = PlanificadorComidas()
menu_semanal = planificador.generar_menu_semanal()
lista_compras = planificador.generar_lista_compras()
Crea un objeto planificador.

Genera un menú semanal .

Obtiene la lista de compras basada en los menús.

Finalmente, imprime el menú y la lista de compras:

print("Menú semanal sugerido:")
for dia, comidas in menu_semanal.items():
    print(f"{dia}: {comidas}")

print("\nLista de compras sugerida:")
print(lista_compras)
🔥 Resumen
✅ Genera menús saludables aleatoriamente.
✅ Permite planificar todas las comidas de la semana.
✅ Crea automáticamente una lista de compras.
✅ Usa POO para mejorar la organización del código.
