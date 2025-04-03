# Planificador_comidas_saludables

Planificador de Comidas con Exportación a JSON

Este programa genera un menú semanal de comidas basado en diferentes grupos de ingredientes y lo exporta a un archivo JSON.

Clases y Métodos:
------------------
- `PlanificadorComidas(tipo_dieta="Omnívora")`: Inicializa el planificador con una dieta específica y una lista de ingredientes categorizados.
- `PlanificadorComidasVegetariano()`: Clase hija que hereda de `PlanificadorComidas` y ajusta la dieta para excluir carnes.
- `PlanificadorComidasVegano()`: Clase hija que hereda de `PlanificadorComidas` y ajusta la dieta para excluir todos los productos de origen animal.
- `generar_menu_diario() -> dict`: Genera un menú diario con opciones aleatorias para desayuno, almuerzo y cena.
- `generar_menu_semanal() -> dict`: Genera un menú semanal con comidas diarias.
- `generar_lista_compras() -> dict`: Crea una lista de compras basada en los ingredientes del menú semanal.
- `guardar_json(nombre_archivo: str)`: Guarda el menú semanal y la lista de compras en un archivo JSON.

Uso del Programa:
------------------
1. El usuario puede elegir entre las dietas: Omnívora, Vegetariana o Vegana.
2. Basado en la elección del usuario, se genera un menú y una lista de compras.
3. Llamar al método `guardar_json("nombre_archivo.json")` para exportar el menú y la lista de compras.

Ejemplo de Uso:
---------------
```python
planificador = PlanificadorComidas()
planificador.guardar_json("menu_semanal.json")

planificador_veg = PlanificadorComidasVegetariano()
planificador_veg.guardar_json("menu_vegetariano.json")

planificador_vegano = PlanificadorComidasVegano()
planificador_vegano.guardar_json("menu_vegano.json")
```
Esto generará archivos JSON con los menús semanales y las listas de compras.
"""
#Explicación por secciones
1. Importación de Módulos

import random
import json
random : Se usa para seleccionar aleatoriamente los ingredientes de cada comida.

json : Permite guardar los datos del menú semanal y la lista de compras en un archivo JSON.

2. Definición de la Clase BasePlanificadorComidas

class PlanificadorComidas:
    def __init__(self, tipo_dieta="Omnívora"):
        self.tipo_dieta = tipo_dieta
Esta es la clase principal que gestiona la planificación de comidas.

Se inicializa con un tipo de dieta (por defecto, "Omnívora").

Diccionario de ingredientes

self.ingredientes = {
    "Verduras": {"Espinaca": 23, "Brócoli": 55, "Zanahoria": 41},
    "Proteínas": {"Pollo": 165, "Pavo": 135, "Pescado": 206, "Tofu": 76, "Lentejas": 116},
    "Carbohidratos": {"Arroz integral": 111, "Quinoa": 120, "Pan integral": 247},
    "Grasas": {"Aguacate": 160, "Frutos secos": 607, "Semillas de chía": 486},
    "Frutas": {"Manzana": 52, "Banana": 89, "Fresas": 32},
    "Líquidos": {"Agua": 0, "Infusiones": 1, "Leche vegetal": 40}
}
Se definen diferentes grupos de alimentos con sus respectivos valores calóricos (en calorías por cada 100g).

3. Generación del Menú Diario

def generar_menu_diario(self):
    menu = {}
    total_calorias = 0
menu: Almacena los platos de cada comida del día.

total_calorias: Acumula las calorías de todo el día.

Selección de Ingredientes y Cálculo de Calorías

for comida, categorias in {"Desayuno": ["Carbohidratos", "Frutas", "Líquidos"],
                           "Almuerzo": ["Verduras", "Proteínas", "Carbohidratos", "Grasas"],
                           "Cena": ["Verduras", "Proteínas", "Líquidos"]}.items():
    seleccion = [random.choice(list(self.ingredientes[categoria].keys())) for categoria in categorias]
    calorias = sum(self.ingredientes[categoria][ingrediente] for categoria, ingrediente in zip(categorias, seleccion))
    total_calorias += calorias
    menu[comida] = {"Ingredientes": seleccion, "Calorías": calorias}
Se seleccionan ingredientes al azar de las categorías correspondientes a Desayuno, Almuerzo y Cena .

Se calcula la cantidad total de calorías de cada comida.

Se almacena la información en menu.

4. Generación del Menú Semanal

def generar_menu_semanal(self):
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    return {dia: self.generar_menu_diario() for dia in dias}
Se genera un menú para cada día de la semana llamando a generar_menu_diario().

5. Generación de la Lista de Compras

def generar_lista_compras(self):
    menu_semanal = self.generar_menu_semanal()
    lista_compras = {}
    for comidas in menu_semanal.values():
        for detalles in comidas.values():
            for ingrediente in detalles["Ingredientes"]:
                lista_compras[ingrediente] = lista_compras.get(ingrediente, 0) + 1
    return lista_compras
Se obtiene el menú semanal y se cuentan las veces que se repite cada ingrediente.

Se almacena en lista_compras.

6. Guardar los Datos en un Archivo JSON



def guardar_json(self, nombre_archivo):
    datos = {
        "Menú semanal": self.generar_menu_semanal(),
        "Lista de compras": self.generar_lista_compras()
    }
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)
    print(f"Datos guardados en {nombre_archivo}")
Se genera el menú semanal y la lista de compras.

Se guardan los datos en un archivo JSON con formato legible ( indent=4).

7. Clases Hijas para Diferentes Tipos de Dietas
Dieta vegetariana


class PlanificadorComidasVegetariano(PlanificadorComidas):
    def __init__(self):


