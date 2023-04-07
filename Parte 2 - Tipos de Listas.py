
import tkinter as tk
from tkinter import ttk

# Estructura de nuestra ventana

ventana_pr = tk.Tk()
ventana_pr.title("Proyecto - Aplicación")
ventana_pr.config(width=300, height=200)


def imprimir_seleccion():
	op_cursor = lista.get(lista.curselection())
	print(op_cursor)

# A continuación Especificamos el uso de la lista (Listbox) y la impresión de los datos por pantalla.

lista = tk.Listbox()
lista.insert(0, "Go", "Python", "C++", "Java")
lista.place(x=10, y=35)

boton = ttk.Button(text="Imprimir lista", command=imprimir_seleccion)
boton.place(x=10, y=10)


# Ejemplo de Lista desplegable (Combobox)
'''
def combo_list():
    opcion = lista_d.get()
    print(opcion)


lista_d = ttk.Combobox(state="readonly", values=[1,3,5,7,9])
lista_d.place(x=10, y=10)

boton = ttk.Button(text="Listar", command=combo_list)
boton.place(x=170, y=10)

'''
ventana_pr.mainloop()