import random
import json

class PlanificadorComidas:
    def __init__(self, tipo_dieta="Omnívora"):
        self.tipo_dieta = tipo_dieta
        self.ingredientes = {
            "Verduras": {"Espinaca": 23, "Brócoli": 55, "Zanahoria": 41},
            "Proteínas": {"Pollo": 165, "Pavo": 135, "Pescado": 206, "Tofu": 76, "Lentejas": 116},
            "Carbohidratos": {"Arroz integral": 111, "Quinoa": 120, "Pan integral": 247},
            "Grasas": {"Aguacate": 160, "Frutos secos": 607, "Semillas de chía": 486},
            "Frutas": {"Manzana": 52, "Banana": 89, "Fresas": 32},
            "Líquidos": {"Agua": 0, "Infusiones": 1, "Leche vegetal": 40}
        }

    def generar_menu_diario(self):
        menu = {}
        total_calorias = 0
        for comida, categorias in {"Desayuno": ["Carbohidratos", "Frutas", "Líquidos"],
                                   "Almuerzo": ["Verduras", "Proteínas", "Carbohidratos", "Grasas"],
                                   "Cena": ["Verduras", "Proteínas", "Líquidos"]}.items():
            seleccion = [random.choice(list(self.ingredientes[categoria].keys())) for categoria in categorias]
            calorias = sum(self.ingredientes[categoria][ingrediente] for categoria, ingrediente in zip(categorias, seleccion))
            total_calorias += calorias
            menu[comida] = {"Ingredientes": seleccion, "Calorías": calorias}
        return menu
    
    def generar_menu_semanal(self):
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        return {dia: self.generar_menu_diario() for dia in dias}
    
    def generar_lista_compras(self):
        menu_semanal = self.generar_menu_semanal()
        lista_compras = {}
        for comidas in menu_semanal.values():
            for detalles in comidas.values():
                for ingrediente in detalles["Ingredientes"]:
                    lista_compras[ingrediente] = lista_compras.get(ingrediente, 0) + 1
        return lista_compras

    def guardar_json(self, nombre_archivo):
        datos = {
            "Menú semanal": self.generar_menu_semanal(),
            "Lista de compras": self.generar_lista_compras()
        }
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
        print(f"Datos guardados en {nombre_archivo}")

class PlanificadorComidasVegetariano(PlanificadorComidas):
    def __init__(self):
        super().__init__(tipo_dieta="Vegetariana")
        self.ingredientes["Proteínas"] = {"Tofu": 76, "Lentejas": 116, "Garbanzos": 164, "Frijoles": 127, "Seitán": 120}

class PlanificadorComidasVegano(PlanificadorComidas):
    def __init__(self):
        super().__init__(tipo_dieta="Vegana")
        self.ingredientes["Proteínas"] = {"Tofu": 76, "Lentejas": 116, "Garbanzos": 164, "Frijoles": 127, "Seitán": 120}
        self.ingredientes["Líquidos"] = {"Agua": 0, "Infusiones": 1}
        self.ingredientes["Grasas"] = {"Frutos secos": 607, "Semillas de chía": 486}

# Elección del usuario
opciones = {"1": PlanificadorComidas, "2": PlanificadorComidasVegetariano, "3": PlanificadorComidasVegano}
while True:
    print("Seleccione el tipo de dieta:")
    print("1. Omnívora\n2. Vegetariana\n3. Vegana\n4. Salir")
    eleccion = input("Ingrese el número de su elección: ")
    
    if eleccion == "4":
        print("Saliendo del programa...")
        break
    elif eleccion in opciones:
        planificador = opciones[eleccion]()
        archivo = "menu_" + planificador.tipo_dieta.lower() + ".json"
        planificador.guardar_json(archivo)
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")


