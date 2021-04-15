from tkinter import *
# libreria para poder abrir y guardar archivos
from tkinter import ttk 
from tkinter import filedialog
#from pagina_principal import ventana_principal
#Python Imaging Library (PIL) es una librería gratuita que permite la edición de imágenes directamente desde Python. Soporta una variedad de formatos, incluídos los más utilizados como GIF, JPEG y PNG. Una gran parte del código está escrito en C
from PIL import Image, ImageTk
from tkinter import messagebox
import app

#root de la app
ventana = Tk()
ventana.title("Datos memoria y kernel")
#ventana.config(bg="white")
ventana.geometry("500x200")

#titulo para la entrada de datos
Label(text="Ingresa los tamaños de la memoria y el kernel").grid(row=1, column=2)

#creamos input de memoria
Label(text="Memoria").grid(row=2, column=2, sticky='nw')
entrada_memoria = StringVar()
entrada_memoria.set(100)
entradaM = Entry(ventana, textvariable=entrada_memoria)
entradaM.grid(row=2, column=3)
boton_memoria_kernel = Button(ventana, text="Validar Memoria y Kernel", command=lambda: verificar_memoria_kernel((entrada_memoria.get()),(entrada_kernel.get()))).grid(row=4, column=2)

#creamos input de kernel
Label(text="Kernel").grid(row=3, column=2, sticky='nw')
entrada_kernel = StringVar()
entrada_kernel.set(kernel) #10*z+9   z=1
entradaK = Entry(ventana, textvariable=entrada_kernel)
entradaK.grid(row=3, column=3)


#carga ventana 1
ventana.mainloop()