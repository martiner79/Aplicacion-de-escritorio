
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#La primera parte será especificar la estructura los detalles de nuestra ventana

ventana_pr = tk.Tk()
ventana_pr.title("Proyecto - Aplicación")
ventana_pr.config(width=300, height=200)

#Barra de Menú

def nuevo():
    print("Nuevo archivo.")

def copiar():
    print("Copiar archivo")


barra_menu = tk.Menu()

menu_archivo = tk.Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Nuevo", command=nuevo)
menu_editar = tk.Menu(barra_menu, tearoff=0)
menu_editar.add_command(label="Copiar", command=copiar)

barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
barra_menu.add_cascade(label="Editar", menu=menu_editar)

ventana_pr.config(width=300, height=200, menu=barra_menu)


ventana_pr.mainloop()