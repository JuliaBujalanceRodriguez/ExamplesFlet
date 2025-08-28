# Proyecto creado por JuliaBujalanceRodriguez
# Licencia: CC BY-ND 4.0 (https://creativecommons.org/licenses/by-nd/4.0/)
# Prohibida la redistribución con modificaciones sin autorización.

# Este es un ejemplo de una traducción básica a través de un diccionario usando controles propios de Flet.
# Te invito a que lo pruebes, juegues y puedas aprender de este ejemplo.

# Importación obligatoria para poder usar el framework Flet
import flet as ft

# Diccionario de traducciones
traducciones = {
   "es": {
       "texto_bienvenida": "Hola, ¿cómo estás?",
       "texto_boton": "Presionar"
   },
   "en": {
       "texto_bienvenida": "Hello, how are you?",
       "texto_boton": "Press"
   },
   "fr": {
       "texto_bienvenida": "Bonjour, comment ça va ?",
       "texto_boton": "Appuyer"
   }
}

# Función principal
def main(page: ft.Page):
    # Idioma por defecto
    idioma = "es"

    # Creamos anteriormente los controles que serán añadidos a la página principal
    texto_salida = ft.Text(traducciones[idioma]["texto_bienvenida"])
    boton_idioma = ft.ElevatedButton(traducciones[idioma]["texto_boton"])

    # Creamos la función para cambiar idioma antes de que sea asignada al selector (dropdown)
    def change_language(e):
        idioma_seleccionado = e.control.value
        texto_salida.value = traducciones[idioma_seleccionado]["texto_bienvenida"]
        boton_idioma.text = traducciones[idioma_seleccionado]["texto_boton"]
        page.update()

    dropdown = ft.Dropdown(
    options=[
        ft.dropdown.Option("es"),
        ft.dropdown.Option("en"),
        ft.dropdown.Option("fr")
    ],
    value=idioma,
    on_change=change_language
    )

    # Añadimos aquí los controles para que aparezcan en la página
    page.add(ft.Column([
    dropdown, texto_salida, boton_idioma
    ], horizontal_alignment= ft.CrossAxisAlignment.CENTER, alignment= ft.MainAxisAlignment.SPACE_BETWEEN, height= page.height * 0.5))

# Esencial para ejecutar el programa
ft.app(target=main, view=ft.AppView.WEB_BROWSER)