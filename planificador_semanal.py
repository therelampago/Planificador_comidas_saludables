mport random
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
        return {
            "Desayuno": [random.choice(list(self.ingredientes["Carbohidratos"].keys())),
                          random.choice(list(self.ingredientes["Frutas"].keys())),
                          random.choice(list(self.ingredientes["Líquidos"].keys()))],
            "Almuerzo": [random.choice(list(self.ingredientes["Verduras"].keys())),
                          random.choice(list(self.ingredientes["Proteínas"].keys())),
                          random.choice(list(self.ingredientes["Carbohidratos"].keys())),
                          random.choice(list(self.ingredientes["Grasas"].keys()))],
            "Cena": [random.choice(list(self.ingredientes["Verduras"].keys())),
                      random.choice(list(self.ingredientes["Proteínas"].keys())),
                      random.choice(list(self.ingredientes["Líquidos"].keys()))]
        }
    
    def generar_menu_semanal(self):
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        return {dia: self.generar_menu_diario() for dia in dias}
    
    def generar_lista_compras(self):
        menu_semanal = self.generar_menu_semanal()
        lista_compras = {}
        for comidas in menu_semanal.values():
            for ingredientes in comidas.values():
                for ingrediente in ingredientes:
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

# Uso del programa
planificador = PlanificadorComidas()
planificador.guardar_json("menu_semanal.json")

