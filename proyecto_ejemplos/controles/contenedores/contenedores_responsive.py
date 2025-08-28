# Proyecto creado por [JuliaBujalanceRodriguez]
# Licencia: CC BY-ND 4.0 (https://creativecommons.org/licenses/by-nd/4.0/)
# Prohibida la redistribución con modificaciones sin autorización.

# Este es un ejemplo de 2 contenedores responsive que se ubican hacia ambos lados de la pantalla.
# Te invito a que lo pruebes, juegues y puedas aprender a utilizar de forma inicial el control 'Container'

# Importación obligatoria para poder usar el framework Flet
import flet as ft

# Función principal que será llamada al final al ejecutarse la aplicación
def main(page: ft.Page):
    
    # Configuración de página
    page.title = "Ejemplos básicos - Contenedores Responsive"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = 20
    
    # Crear los contenedores pasando la página como parámetro
    # Ambos contenedores ocuparán la mitad de la pantalla de forma responsive (sus controles internos también)
    contenedor_izquierdo = ClaseContenedor(page=page, text="Grid Izquierdo")
    contenedor_izquierdo = ClaseContenedor(page=page, text="Grid Derecho")
    
    # Diseño principal (dispuesto en un 'Row' o fila)
    page.add(
        ft.Row(
            controls=[contenedor_izquierdo, contenedor_izquierdo],
            spacing=20,
            expand=True,
            alignment=ft.MainAxisAlignment.SPACE_EVENLY
        )
    )

# cClase utilizada que hereda del control 'Container'
class ClaseContenedor(ft.Container):
    
    # función para crear la instancia de un contenedor
    def __init__(self, page, text="Texto de ejemplo", **kwargs):
        
        # inicializador heredado del control 'Container'
        super().__init__(**kwargs)
        
        # atributos personalizados (estos no tienen necesariamente que ver con las propiedades del control)
        self.page = page
        self.text = text
        self.numero_contenedores_internos = 20 
        
        # atributos que son propiedades del contenedor
        self.padding = 20
        self.bgcolor = ft.Colors.BLUE_GREY_100
        self.border_radius = 10
        self.expand = True
        
        # Aquí se construye directamente el contenido usando las funciones que hay a continuación
        self.content = self.construir_contenido()
    
    def construir_contenido(self):
        # devuelve el texto y el'GridView' contenido dentro de una Columna (para que se muevan hacia abajo)
        return ft.Column(
            controls=[
                ft.Text(self.text, size=20, weight="bold"),
                self.construir_objetos_internos()
            ],
            alignment=ft.MainAxisAlignment.START,
    )
    
    def construir_objetos_internos(self):        
        # devuelve un control 'GridView' que contiene pequeños contenedores en su interior
        return ft.GridView(
            controls=[
                ft.Container(
                    content=ft.Text(f"Item {i+1}"),
                    padding=10,
                    bgcolor=ft.Colors.AMBER_100,
                    border_radius=5,
                    width=100,
                    height=100,
                )
                for i in range(self.numero_contenedores_internos) # se itera sobre to
            ],
            runs_count=5,
            max_extent=150, # anchura/altura máxima de cada elemento
            expand=True
    )
        
# Para ejecutar la aplicación, en este caso de forma web
ft.app(target = main, view = ft.AppView.WEB_BROWSER)