import random

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
        desayuno = [random.choice(list(self.ingredientes["Carbohidratos"].keys())),
                    random.choice(list(self.ingredientes["Frutas"].keys())),
                    random.choice(list(self.ingredientes["Líquidos"].keys()))]
        almuerzo = [random.choice(list(self.ingredientes["Verduras"].keys())),
                    random.choice(list(self.ingredientes["Proteínas"].keys())),
                    random.choice(list(self.ingredientes["Carbohidratos"].keys())),
                    random.choice(list(self.ingredientes["Grasas"].keys()))]
        cena = [random.choice(list(self.ingredientes["Verduras"].keys())),
                random.choice(list(self.ingredientes["Proteínas"].keys())),
                random.choice(list(self.ingredientes["Líquidos"].keys()))]
        return {"Desayuno": desayuno, "Almuerzo": almuerzo, "Cena": cena}
    
    def generar_menu_semanal(self):
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        return {dia: self.generar_menu_diario() for dia in dias}
    
    def generar_lista_compras(self):
        menu_semanal = self.generar_menu_semanal()
        lista_compras = {}
        for dia, comidas in menu_semanal.items():
            for tipo, ingredientes in comidas.items():
                for ingrediente in ingredientes:
                    if ingrediente in lista_compras:
                        lista_compras[ingrediente] += 1
                    else:
                        lista_compras[ingrediente] = 1
        return lista_compras

# Uso del programa
planificador = PlanificadorComidas()
menu_semanal = planificador.generar_menu_semanal()
lista_compras = planificador.generar_lista_compras()

print("Menú semanal sugerido:")
for dia, comidas in menu_semanal.items():
    print(f"{dia}: {comidas}")

print("\nLista de compras sugerida:")
print(lista_compras)
