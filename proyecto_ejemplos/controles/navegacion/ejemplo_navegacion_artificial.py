# Proyecto creado por JuliaBujalanceRodriguez
# Licencia: CC BY-ND 4.0 (https://creativecommons.org/licenses/by-nd/4.0/)
# Prohibida la redistribución con modificaciones sin autorización.

# Este es un ejemplo de navegación artificial (sin usar la propia incorporada en el navegador en el cual
# se va a ejecutar este programa) para practicar y entender cómo funciona.
# Te invito a que lo pruebes, juegues y puedas aprender a utilizarlo de forma inicial.

# Importación obligatoria para poder usar el framework Flet
import flet as ft

# Función principal que será llamada al final al ejecutarse la aplicación
def main(page: ft.Page):
    page.title = "Ejemplos Básicos - Navegación Adelante y Atrás"
    page.theme_mode = "light"
    contenido_pagina = ft.Column(expand=True)  # Contenido incialmente creado
    pila_hacia_atras = []    # Historial hacia atrás
    pila_hacia_delante = [] # Historial hacia adelante

    # Función para ir a una nueva vista independientemente de cuál sea esa
    def navegar_a(contenido_nuevo, desde_usuario=True):
        
        if desde_usuario:
            pila_hacia_atras.append(contenido_pagina.controls[:])  # Se guarda la vista actual
            pila_hacia_delante.clear()  # Se pierde el "adelante" si vas a una nueva ruta

        contenido_pagina.controls.clear()
        contenido_nuevo()
        page.update()

    # Función para restaurar los controles de la página cuando vuelve atrás
    def ir_atras(e):
        if pila_hacia_atras:
            pila_hacia_delante.append(contenido_pagina.controls[:])  # Guarda la vista actual
            contenido_pagina.controls.clear()
            contenido_pagina.controls.extend(pila_hacia_atras.pop())
            page.update()

    # Función para restaurar los controles de la página cuando va hacia delante
    def ir_adelante(e):
        if pila_hacia_delante:
            pila_hacia_atras.append(contenido_pagina.controls[:])  # Guarda la vista actual
            contenido_pagina.controls.clear()
            contenido_pagina.controls.extend(pila_hacia_delante.pop())
            page.update()

    # Vistas de ejemplo
    def vista_inicio():
        contenido_pagina.controls.append(ft.Text("🏠 Página de inicio"))
        contenido_pagina.controls.append(ft.ElevatedButton("Ir a Opción 1", on_click=lambda e: navegar_a(vista_opcion1)))
        contenido_pagina.controls.append(ft.ElevatedButton("Ir a Opción 2", on_click=lambda e: navegar_a(vista_opcion2)))

    def vista_opcion1():
        contenido_pagina.controls.append(ft.Text("📄 Te encuentras en la opción 1"))
        contenido_pagina.controls.append(ft.TextField(label="Escribe aquí un dato (que no se debe perder)"))
        contenido_pagina.controls.append(ft.ElevatedButton("Ir a Opción 2", on_click=lambda e: navegar_a(vista_opcion2)))
        contenido_pagina.controls.append(ft.ElevatedButton("Ir a Inicio", on_click=lambda e: navegar_a(vista_inicio)))

    def vista_opcion2():
        contenido_pagina.controls.append(ft.Text("⚙️ Te encuentras en la opción 2"))
        contenido_pagina.controls.append(ft.TextField(label="Aquí puedes escribir otro dato"))
        contenido_pagina.controls.append(ft.ElevatedButton("Ir a Inicio", on_click=lambda e: navegar_a(vista_inicio)))
        contenido_pagina.controls.append(ft.ElevatedButton("Ir a Inicio", on_click=lambda e: navegar_a(vista_opcion1)))

    # Botones de navegación simulando un navegador
    controles_navegacion = ft.Row([
        ft.IconButton(icon=ft.Icons.ARROW_BACK, on_click=ir_atras, tooltip="Atrás"),
        ft.IconButton(icon=ft.Icons.ARROW_FORWARD, on_click=ir_adelante, tooltip="Adelante"),
    ])

    # Añadimos a la página los controles de navegación y el contenido que se muestra
    page.add(
        ft.Column([
            controles_navegacion,
            contenido_pagina
        ], expand=True)
    )

    # Vista inicial sin guardar en back_stack
    navegar_a(vista_inicio, desde_usuario=False)  

# Para ejecutar la aplicación
ft.app(target=main, view= ft.AppView.WEB_BROWSER)