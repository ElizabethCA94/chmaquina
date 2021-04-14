from tkinter import *
# libreria para poder abrir y guardar archivos
from tkinter import ttk 
from tkinter import filedialog
#from pagina_principal import ventana_principal
#Python Imaging Library (PIL) es una librería gratuita que permite la edición de imágenes directamente desde Python. Soporta una variedad de formatos, incluídos los más utilizados como GIF, JPEG y PNG. Una gran parte del código está escrito en C
from PIL import Image, ImageTk
from tkinter import messagebox 
import memoria_kernel

#root de la app
ventana = Tk()
ventana.title("Datos memoria y kernel")
#ventana.config(bg="white")
ventana.geometry("500x200")



global z
z = 1 #ultimo digito de la cedula 1053835141 

global instrucciones_archivo 
instrucciones_archivo = []

global memoria_principal
memoria_principal = [100]

global kernel 
kernel=10*z+9

global memoria
memoria=100

global errores
errores = []

#dicccionario de variables
global variables
variables = {}

global etiquetas
etiquetas = {}

global lista_rutas
lista_rutas = []


#inserta el sistema operativo en la memoria principal 
i = 0 
def insertar_kernel(memoria_principal, kernel):
    global i
    if i < 1:# borra un nuevo kernel
        i += 1
        memoria_principal.append("ACOMULADOR")
        for i in range(1, int(kernel)+1):
            memoria_principal.append("SISTEMA OPERATIVO")
        #print(memoria_principal)

#verifica si al establecer el kernel hay espacio o no para cambiarlo por ese valor
def verificar_memoria_kernel(memoria, kernel):
    print(memoria)
    if (int(memoria.isalpha())==True or not(memoria) or int(kernel.isalpha())==True or not(kernel)): #comprueba si el dato ingresado es un digito o esta vacio el campo que se debe ingresar
        messagebox.askokcancel(message="Datos incorrectos, el dato ingresado es obligatorio y debe ser un digito")
    elif (int(kernel) > 0 and int(memoria) > 0 and int(memoria) <= 9999 and int(kernel) < int(memoria)):
        insertar_kernel(memoria_principal, kernel)
        memoria_kernel.insertar_memoria_y_kernel(memoria, kernel)
        msgbox = messagebox.askquestion(message="Datos correctos!!")
        if msgbox == 'yes':
            ventana.destroy()
    else:
        messagebox.askokcancel(message="Datos incorrectos, la memoria debe ser menor a 9999 posiciones y el tamaño del kernel debe ser menor al tamaño de la memoria")


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

#ventana 2
ventana_principal = Tk()
ventana_principal.geometry("3800x3000")

#realizamos el menu de opciones
menubar = Menu(ventana_principal)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Abrir", command=lambda: abrir_archivo())
menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_command(label="Ejecute", command=lambda: verificar_sintaxis(instrucciones_archivo))
menubar.add_cascade(label="Muestre memoria")
menubar.add_cascade(label="Pausa")
menubar.add_cascade(label="Paso a paso")
menubar.add_cascade(label="Salir")
ventana_principal.configure(menu=menubar)

#creamos input de acomulador
Label(ventana_principal,text="Acomulador").grid(row=3, column=0, sticky='nw')
entrada_acomulador = IntVar()
entradaA = Entry(ventana_principal, textvariable=entrada_acomulador)
entradaA.grid(row=3, column=1)

#carga de instrucciones de los archivos
treeview_archivos = ttk.Treeview(ventana_principal, height=10, columns=2)
scrollbar = ttk.Scrollbar(ventana_principal, orient = "vertical", command=treeview_archivos.yview )
scrollbar.grid(row=6, column=1, sticky="nse")
treeview_archivos.configure(yscrollcommand=scrollbar.set)
treeview_archivos.grid(row=6, column=1, sticky='nsew')
    

#caja de texto para las variables
texto_variables = Text(ventana_principal,width=20, height=20)
texto_variables.grid(row=6, column=2)

#imagen del computador
computer_image = ImageTk.PhotoImage(Image.open("./img/computadora.png"))
computer_image_label = Label(ventana_principal, image=computer_image)
computer_image_label.grid(row=1, column=3, padx=10, pady=10)
boton_kernel_usuario = Button(ventana_principal, text="Modo Usuario").grid(row=2, column=3)

#mostrar lo del pc
carga_datos_pantalla = Listbox(ventana_principal, width=20, height=20)
scroll = Scrollbar(ventana_principal, orient = VERTICAL)

#Creo un menu desplegable para establecer modo kernel o modo usuario
opciones=["kernel","usuario"]#Estas seran las opciones
var=StringVar()#es la variable que se encontrara como primera opcion
var.set(opciones[0])

#mostrar instrucciones paso a paso
treeview_archivos_paso_a_paso = ttk.Treeview(ventana_principal, columns=2, height=10)

scrollbar = ttk.Scrollbar(ventana_principal, orient=VERTICAL, command=treeview_archivos_paso_a_paso.yview)
scrollbar.grid(row=6, column=4, sticky="ns", padx="7")

treeview_archivos_paso_a_paso.configure(yscrollcommand=scrollbar.set)
treeview_archivos_paso_a_paso.grid(row=6, column=4, sticky="nsew")

#metodo para cargar los archivos en la caja de texto con scroll
def abrir_archivo():
    global instrucciones_archivo
    archivo_abierto=filedialog.askopenfilename(initialdir="/Documents/ch-maquina/programs",
        title="Seleccione archivo",filetypes=(("ch files","*.ch"),
        ("all files","*.*")))
    if archivo_abierto!='':
        archivo=open(archivo_abierto, "r", )
        instrucciones_archivo = archivo.readlines()#Conversión del archivo de texto en una lista por renglones
        archivo.close()
        for i in range(0, len(instrucciones_archivo)):
            treeview_archivos.insert("" , 'end', text="00" + str(i+1), values= (instrucciones_archivo[i],))

#verificar sintaxis
def verificar_sintaxis(instrucciones_archivo):
    archivo = instrucciones_archivo
    palabra = []
    for instruccion in archivo:
        print(instruccion)
        instruccion = instruccion.strip("\n") 
        palabra = instruccion.split(" ")
        if(palabra[0] == "cargue"):
            funcion_error_cargue_almacene_multiplique_sume_reste(palabra)
        elif(palabra[0] == "almacene"):
            funcion_error_cargue_almacene_multiplique_sume_reste(palabra)
        elif(palabra[0] == "nueva"):
            funcion_error_nueva(palabra)            
        elif(palabra[0] == "lea"):
            funcion_error(palabra)
        elif(palabra[0] == "sume"):
            funcion_error_cargue_almacene_multiplique_sume_reste(palabra)
        elif(palabra[0] == "reste"):
            funcion_error_cargue_almacene_multiplique_sume_reste(palabra) 
        elif(palabra[0] == "multiplique"):
            funcion_error_cargue_almacene_multiplique_sume_reste(palabra)  
        elif(palabra[0] == "divida"):
            funcion_error_divida_modulo(palabra)  
        elif(palabra[0] == "potencia"):
            funcion_error_potencia(palabra)
        elif(palabra[0] == "modulo"):
            funcion_error_divida_modulo(palabra)  
        elif(palabra[0] == "concatene"):
            funcion_error_concatene_extraiga(palabra)   
        elif(palabra[0] == "elimine"):
            funcion_error(palabra)  
        elif(palabra[0] == "extraiga"):
            funcion_error_concatene_extraiga(palabra)
        elif(palabra[0] == "Y"):
            funcion_error_y_o_no(palabra)  
        elif(palabra[0] == "O"):
            funcion_error_y_o_no(palabra)
        elif(palabra[0] == "NO"):
            funcion_error_y_o_no(palabra)
        elif(palabra[0] == "muestre"):
            funcion_error(palabra)  
        elif(palabra[0] == "imprima"):
            funcion_error(palabra)   
        elif(palabra[0] == "vaya"):
            funcion_error_vaya(palabra) 
        elif(palabra[0] == "vayasi"):
            funcion_error_vaya_si(palabra)
        elif(palabra[0] == "etiqueta"):
            funcion_error_etiqueta(palabra)
        elif(palabra[0] == "retorne"):
            funcion_error_retorne(palabra)
        else:
            funcion_error_comentario(palabra)    


#verficar sintaxis de las operaciones lea, muestra, imprima, elimine
def funcion_error(palabra):
    if(len(palabra)>2):
        errores.append("Error, se estan utilizando mas de 2 operandos en la operacion "+ palabra[0]) 
    elif(palabra[1] not in variables):
        errores.append("Error, la variable " + palabra[1] + " no ha sido asignada")
    print(errores)

#error comentarios o operaciones no declaradas
def funcion_error_comentario(palabra):
    comentario = ['//', ' ']
    if(palabra[0] in comentario):
        errores.append("Error, no es una operación valida " + palabra[1])

#error nueva
def funcion_error_nueva(palabra):
    global variables
    tipos_datos = ["C", "I", "R", "L"]
    if(len(palabra)>4):
        errores.append("Error, se estan utilizando mas de 4 operandos en la operacion "+ palabra[0])
    elif((palabra[2]=="I") and (palabra[3].isdigit()==False)):
        errores.append("Error, el valor de inicializacion "  + palabra[3] + " no es correcto, en el tipo de dato " + palabra[2])
    elif((palabra[2]=="L") and not(palabra[3] == "1" or palabra[3] == "0")):
        errores.append("Error en el el valor de inicializacion  " + palabra[3]  + " no es correcto, en el tipo de dato " + palabra[2])
    elif((palabra[2]=="C") and (palabra[3].isalpha()==False)):
        errores.append("Error en el el valor de inicializacion  " + palabra[3]  + " no es correcto, en el tipo de dato " + palabra[2])
    elif((palabra[2]=="R") and (palabra[3].isdecimal()==False)):
        errores.append("Error en el el valor de inicializacion  " + palabra[3]  + " no es correcto, en el tipo de dato " + palabra[2]) 
    elif(palabra[1] not in variables):
        funcion_variable_nombre_valido_variable(palabra)
    elif(palabra[2] not in tipos_datos):
        errores.append("Error, el tipo de dato especificado " + +  palabra[2] + " no ha sido declarado" )

#verifica que el nombre no sea una operacion
def funcion_variable_nombre_valido_variable(palabra):
    palabras_operaciones = ["cargue", "almacene","nueva", "lea", "sume", "reste", "multiplique", "divida", "potencia", "modulo", "concatene", "elimine", "extraiga", "Y", "O", "muestre", "vaya", "vayasi", "etiqueta", "retorne"]
    if(palabra[1] in palabras_operaciones):
        errores.append("Error, el nombre de la variable " + palabra[1] +" no es válido"  )
    else:
        variables[palabra[1]] = { 'tipo': palabra[2], 'valor': palabra[3] }

#validan los errores de las funciones cargue, almacene, multiplique, sume, reste
def funcion_error_cargue_almacene_multiplique_sume_reste(palabra):
    if(len(palabra)>2):
        errores.append("Error, se estan utilizando mas de 2 operandos en la operacion "+ palabra[0])
    elif(palabra[1] not in variables):
        errores.append("Error, la variable " + palabra[1] + " no ha sido asignada")
    elif((variables[palabra[1]]['tipo'] == "L") or (variables[palabra[1]]['tipo'] == "C")):
        errores.append("Error, la variable " + palabra[1] + " no se puede ejecutar en la operacion " + palabra[0] + " porque su tipo de dato es " + variables[palabra[1]]['tipo']) 
    print(errores)

#validan los errores de las funciones divida, modulo
def funcion_error_divida_modulo(palabra):
    if(len(palabra)>2):
        errores.append("Error, se estan utilizando mas de 2 operandos en la operacion "+ palabra[0])
    elif(palabra[1] not in variables):
        errores.append("Error, la variable " + palabra[1] + " no ha sido asignada")
    elif((variables[palabra[1]]['tipo'] == "L") or (variables[palabra[1]]['tipo'] == "C")):
        errores.append("Error, la variable " + palabra[1] + " no se puede ejecutar en la operacion " + palabra[0] + " porque su tipo de dato es " + variables[palabra[1]]['tipo']) 
    elif(variables[palabra[1]]['valor'] == "0"):
        errores.append("Error, la operacion "+ palabra[0] + " no permite dividir entre " + variables[palabra[1]]['valor'] )

#valida error de la potencia
def funcion_error_potencia(palabra):
    if(len(palabra)>2):
        errores.append("Error, se estan utilizando mas de 2 operandos en la operacion "+ palabra[0])
    elif(palabra[1] not in variables):
        errores.append("Error, la variable " + palabra[1] + " no ha sido asignada")
    elif((variables[palabra[1]]['tipo'] == "L") or (variables[palabra[1]]['tipo'] == "C")):
        errores.append("Error, la variable " + palabra[1] + " no se puede ejecutar en la operacion " + palabra[0] + " porque su tipo de dato es " + variables[palabra[1]]['tipo']) 
    elif((variables[palabra[1]]['valor'].isdigit()==False) or not(variables[palabra[1]]['valor'] <= 0)):
        errores.append("Error, la operacion "+ palabra[0] + " no permite elevar a una portencia " + variables[palabra[1]]['valor'] )

#error concatene
def funcion_error_concatene_extraiga(palabra):
    if(len(palabra)>2):
        errores.append("Error, se estan utilizando mas de 2 operandos en la operacion "+ palabra[0])
    elif(palabra[1] not in variables):
        errores.append("Error, la variable " + palabra[1] + " no ha sido asignada")
    elif((variables[palabra[1]]['tipo'] != "C")):
        errores.append("Error, la variable " + palabra[1] + " no se puede ejecutar en la operacion " + palabra[0] + " porque su tipo de dato es " + variables[palabra[1]]['tipo']) 
    elif((palabra[1].isalpha())==False):
        errores.append("Error, el operando no es alfanumerico "+ palabra[0])

#error y_o
def funcion_error_y_o_no(palabra):
    if(len(palabra)>4):
        errores.append("Error, se estan utilizando mas de 4 operandos en la operacion " + palabra[0])
    elif(palabra[1] not in variables):
        errores.append("Error, la variable " + palabra[1] + " no ha sido asignada")
    elif((variables[palabra[1]]['tipo'] != "L")):
        errores.append("Error, la variable " + palabra[1] + " no se puede ejecutar en la operacion " + palabra[0] + " porque su tipo de dato es " + variables[palabra[1]]['tipo']) 
    
#error etiqueta
def funcion_error_etiqueta(palabra):
    if(len(palabra)>3):
        errores.append("Error, se estan utilizando mas de 2 operandos en la operacion "+ palabra[0])
    elif(palabra[2].isdigit()==False):
        errores.append("Error, el valor " + palabra[2] + " no es válido para la operación " + palabra[0]  )
    elif(palabra[1] not in etiquetas):
        funcion_variable_nombre_valido_etiqueta(palabra)

    #verifica que el nombre no sea una operacion
def funcion_variable_nombre_valido_etiqueta(palabra):
    palabras_operaciones = ["cargue", "almacene","nueva", "lea", "sume", "reste", "multiplique", "divida", "potencia", "modulo", "concatene", "elimine", "extraiga", "Y", "O", "muestre", "vaya", "vayasi", "etiqueta", "retorne"]
    if(palabra[1] in palabras_operaciones):
        errores.append("Error, el nombre de la de etiqueta " + palabra[1] +" no es válido"  )
    else:
        etiquetas[palabra[1]] = { 'valor': palabra[2] }

#error_retorne
def funcion_error_retorne(palabra):
    if(len(palabra)>2):
        errores.append("Error, se estan utilizando mas de 2 operandos en la operacion "+ palabra[0])
    elif(palabra[1].isdigit()==False):
        errores.append("Error, el valor " + palabra[1] +" no es válido para la operación " + palabra[0])

#error_vaya
def funcion_error_vaya(palabra):
    if(len(palabra)>2):
        errores.append("Error, se estan utilizando mas de 2 operandos en la operacion "+ palabra[0])
    elif(palabra[1] not in etiquetas):
        errores.append("Error, la etiqueta " + palabra[1] + " no ha sido asignada")
    elif(etiquetas[palabra[1]]['valor'].isdigit()==False):
        errores.append("Error, el valor " + etiqueta[palabra[1]]['valor']  + " no es válido para la operación " + palabra[0]  )

#error_vaya_si
def funcion_error_vaya_si(palabra):
    if(len(palabra)>3):
        errores.append("Error, se estan utilizando mas de 3 operandos en la operacion "+ palabra[0])
    elif(palabra[1] not in etiquetas):
        errores.append("Error, la etiqueta " + palabra[1] + " no ha sido asignada")
    elif(palabra[2] not in etiquetas):
        errores.append("Error, la etiqueta " + palabra[2] + " no ha sido asignada")
    elif(etiquetas[palabra[1]]['valor'].isdigit()==False):
        errores.append("Error, el valor " + etiqueta[palabra[1]]['valor']  + " no es válido para la operación " + palabra[0]  )
    elif(etiquetas[palabra[2]]['valor'].isdigit()==False):
        errores.append("Error, el valor " + etiqueta[palabra[2]]['valor']  + " no es válido para la operación " + palabra[0]  )

ventana_principal.mainloop()


