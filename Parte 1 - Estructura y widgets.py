import tkinter as tk
from tkinter import ttk

# Estructura de nuestra ventana

ventana_pr = tk.Tk()
ventana_pr.title("Proyecto - Aplicación")
ventana_pr.config(width=300, height=200)

def boton_presionar():
    pass

def imprimir_texto():
    print(entry.get())

# Tipo de widget boton

boton = ttk.Button(text="Esto es un ejemplo", command=boton_presionar)
boton.place(x=10, y=10)

# Tipo de Widget Caja de texto (entry)

entry = ttk.Entry()
entry.place(x = 160, y = 50)
boton = ttk.Button(text="Imprimir texto", command=imprimir_texto)
boton.place(x = 10, y = 50)

# Tipo dewidget Etiqueta (Label)

etiqueta = ttk.Label(text="Nombre:")
etiqueta.place(x=100, y=50) 


ventana_pr.mainloop()