# Planificador_comidas_saludables


Planificador de Comidas con Exportación a JSON

Este programa genera un menú semanal de comidas basado en diferentes grupos de ingredientes y lo exporta a un archivo JSON.

Clases y Métodos:
------------------
- `PlanificadorComidas(tipo_dieta="Omnívora")`: Inicializa el planificador con una dieta específica y una lista de ingredientes categorizados.
- `generar_menu_diario() -> dict`: Genera un menú diario con opciones aleatorias para desayuno, almuerzo y cena.
- `generar_menu_semanal() -> dict`: Genera un menú semanal con comidas diarias.
- `generar_lista_compras() -> dict`: Crea una lista de compras basada en los ingredientes del menú semanal.
- `guardar_json(nombre_archivo: str)`: Guarda el menú semanal y la lista de compras en un archivo JSON.

Uso del Programa:
------------------
1. Crear una instancia del `PlanificadorComidas`.
2. Llamar al método `guardar_json("nombre_archivo.json")` para exportar el menú y la lista de compras.

Ejemplo de Uso:
---------------
```python
planificador = PlanificadorComidas()
planificador.guardar_json("menu_semanal.json")
```
Esto generará un archivo `menu_semanal.json` con el menú semanal y la lista de compras.
