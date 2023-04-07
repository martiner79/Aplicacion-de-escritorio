
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


#La primera parte será especificar la estructura los detalles de nuestra ventana

ventana_pr = tk.Tk()
ventana_pr.title("Proyecto - Aplicación")
ventana_pr.config(width=400, height=400)

# Tipo de widget boton

def boton_presionar():
    pass


boton = ttk.Button(text="Ejemplo-Boton", command=boton_presionar)
boton.place(x=10, y=10)

# Tipo de Widget Caja de texto (entry)

def imprimir_texto():
    print(entry.get())

entry = ttk.Entry()
entry.place(x = 170, y = 50)

boton = ttk.Button(text="Imprimir texto", command=imprimir_texto)
boton.place(x = 10, y = 50)

# Tipo dewidget Etiqueta (Label)

etiqueta = ttk.Label(text="Nombre:")
etiqueta.place(x=110, y=50) 



# Lista (Listbox) y la impresión de los datos por pantalla.


def imprimir_seleccion():
	op_cursor = lista.get(lista.curselection())
	print(op_cursor)
	

lista = tk.Listbox()
lista.insert(0, "Go", "Python", "C++", "Java")
lista.place(x=10, y=120, width=100, height=100)

etiqueta = ttk.Label(text="Marque un Lenguaje:")
etiqueta.place(x=10, y=100) 

boton = ttk.Button(text="Imprimir lista", command=imprimir_seleccion)
boton.place(x=10, y=230)


# Ejemplo de Lista desplegable


def combo_list():
    opcion = lista_d.get()
    print(opcion)


lista_d = ttk.Combobox(state="readonly", values=[1,3,5,7,9])
lista_d.place(x=170, y=110)

boton = ttk.Button(text="Listar", command=combo_list)
boton.place(x=170, y=230)


# Casilla de verificación (Checkbox)


def boton_checkbox():
    boton = bool.get()
    print(boton)


bool = tk.BooleanVar()
checkbutton = ttk.Checkbutton(text="Aceptar términos y condiciones", variable=bool)
checkbutton.place(x=10, y=270)
bool.set("False")

boton = ttk.Button(text="Aceptar", command=boton_checkbox)
boton.place(x=10, y=300)


#Imagen dentro de etiqueta
'''
imagen = tk.PhotoImage(file="/directory/image")

label = ttk.Label(image=imagen)
label.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5)
'''

#Barras de progreso

# Barra Horizontal

barra = ttk.Progressbar(maximum=100)
barra.place(x=170, y=300, width=100)
barra.step(50)
barra.start(50)

# Barra vertical

barra = ttk.Progressbar(orient=tk.VERTICAL, maximum=100)
barra.place(x=370, y=110, height=100)
barra.start(20)


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

ventana_pr.config(width=400, height=400, menu=barra_menu)

'''
#Cuadros de diálogo

# Retornan TRUE o FALSE

messagebox.askokcancel(title="Pregunta", message="¿Desea seguir?")
messagebox.askyesno(title="Pregunta", message="¿Desea cancelar?")
messagebox.askretrycancel(title="Pregunta", message="¿Desea reintentar?")

# Retornan OK

messagebox.showinfo(title="Info", message="Se ha descargado el Programa")
messagebox.showwarning(title="Advertencia", message="Los programas de terceros pueden contener virus")
messagebox.showerror(title="Error", message="El siguiente sitio no es seguro.¿Desea seguir?")
'''
ventana_pr.mainloop()


