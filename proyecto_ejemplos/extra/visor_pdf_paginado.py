# Proyecto creado por JuliaBujalanceRodriguez
# Licencia: CC BY-ND 4.0 (https://creativecommons.org/licenses/by-nd/4.0/)
# Prohibida la redistribución con modificaciones sin autorización.

# Este es un ejemplo de visor de PDF con paginación integrada y renderizado de páginas dentro de la app
# ¿Cómo funciona? -> Abre un pdf local (desde la carpeta de Descargas), paginado y renderizado dentro de la app.
# Recomendación de uso: 
    # Mostrar el pdf dentro de la aplicación sin depender de un programa externo,
    # Añadir funcionalidades extra
    # Controlar la presentación mientras se mantiene al usuario dentro de la app.

# Importación obligatoria para poder usar el framework Flet
import flet as ft

# PyMuPDF -> biblioteca de Python que permite leer, modificar, analizar y renderizar archivos PDF (y otros formatos)
import fitz

import base64
from platformdirs import user_downloads_path
from pathlib import Path

# Función principal
def main(page: ft.Page):
    page.title = "Visor PDF paginado"
    page.horizontal_alignment = ft.Alignment(0,0)
    page.bgcolor = ft.Colors.GREY_200

    ruta_carpeta_descargas = Path(user_downloads_path())
    nombre_archivo_pdf = "ejemplo.pdf"
    ruta_pdf = ruta_carpeta_descargas / nombre_archivo_pdf

    if not ruta_pdf.exists():
        page.add(ft.Text(f"No se encontró el archivo: {ruta_pdf}", color=ft.Colors.RED))
        return

    try:
        documento = fitz.open(str(ruta_pdf))
    except Exception as e:
        page.add(ft.Text(f"Error al abrir el PDF: {e}", color=ft.Colors.RED))
        return

    total_paginas = documento.page_count
    pagina_actual = 0

    control_imagen = ft.Image()
    texto_pagina = ft.Text(size=12)

    # Funciones relacionadas con la página -> actualización y navegación

    def actualizar_pagina():
        nonlocal pagina_actual  # variable declarada fuera de la función
       
        boton_anterior_pagina.disabled = pagina_actual == 0
        boton_siguiente_pagina.disabled = pagina_actual == total_paginas - 1

        page.update()

    def ir_pagina_anterior(e):
        nonlocal pagina_actual
        if pagina_actual > 0:
            pagina_actual -= 1
            actualizar_pagina()

    def ir_pagina_siguiente(e):
        nonlocal pagina_actual
        if pagina_actual < total_paginas - 1:
            pagina_actual += 1
            actualizar_pagina()
            
    # Botones paginación pdf
    boton_anterior_pagina = ft.IconButton( ft.Icons.ARROW_BACK, on_click=ir_pagina_anterior, icon_size=20 )
    boton_siguiente_pagina = ft.IconButton( ft.Icons.ARROW_FORWARD, on_click=ir_pagina_siguiente, icon_size=20 )
    
    # Contenido página
    page.add(
        ft.Column(
            [
                # Fila navegación
                ft.Row(
                    [boton_anterior_pagina, texto_pagina, boton_siguiente_pagina],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                # Columna contenido imagen pdf
                ft.Column(
                    [control_imagen],
                    scroll=ft.ScrollMode.AUTO,
                    height=page.height - page.height * 0.15,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=5,
        )
    )
    
    # Al iniciar, se actualiza la página del pdf
    actualizar_pagina()
    page.update()

# Para ejecutar la aplicación
ft.app(target=main, view=ft.WEB_BROWSER)