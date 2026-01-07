import flet as ft

def main(page: ft.Page):
    page.add(ft.ElevatedButton("РАБОТАЕТ!", on_click=lambda _: print("Нажато")))

ft.app(main)
