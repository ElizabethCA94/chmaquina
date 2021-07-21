from tkinter import *
# libreria para poder abrir y guardar archivos
from tkinter import ttk 
from tkinter import filedialog
#from pagina_principal import ventana_principal
#Python Imaging Library (PIL) es una librería gratuita que permite la edición de imágenes directamente desde Python. Soporta una variedad de formatos, incluídos los más utilizados como GIF, JPEG y PNG. Una gran parte del código está escrito en C
from PIL import Image, ImageTk
from tkinter import messagebox 

#ventana 1 ***********************************************
ventana = Tk()
ventana.title("DATOS MEMORIA Y KERNEL")
ventana.geometry("500x200")

global acumulador
acumulador = 3

global es_paso_a_paso 
es_paso_a_paso = False

global es_al_ejecutar
es_al_ejecutar = False

global z
z = 1 #ultimo digito de la cedula 1053835141 

global instrucciones_archivo 
instrucciones_archivo = []

global memoria_principal
memoria_principal = []

global instrucciones_ch
instrucciones_ch = []

global kernel 
kernel=10*z+9

global cantidad_de_comentarios 
cantidad_de_comentarios=0

global memoria
memoria=100

global errores
errores = []

#dicccionario de variables
global variables
variables = {}

global etiquetas
etiquetas = {}

#inserta el sistema operativo en la memoria principal 
i = 0 
def insertar_kernel(memoria, kernel):
    global memoria_principal
    global i
    if i < 1:
        i += 1
        #añade dentro de la memoria princial los datos, como la memoria principal se crea como un array de diccionarios, esto permite que se asgine un tipo y un valor a cada asignacion  
        memoria_principal.append({ 'tipo': 'acumulador',  'valor': 0})
        for i in range(1, kernel+1):
            memoria_principal.append({'tipo': 'SO', 'valor': 'CH maquina'})
        for i in range(kernel+1, memoria):
            memoria_principal.append({'tipo': 'vacio', 'valor': ''})

#verifica el tamaño del kernel y de la memoria
def verificar_memoria_kernel(memoria_usuario, kernel_usuario):
    global memoria
    global kernel
    memoria = memoria_usuario
    kernel = kernel_usuario
    if (int(memoria.isalpha())==True or not(memoria) or int(kernel.isalpha())==True or not(kernel)): #comprueba si el dato ingresado es un digito o esta vacio el campo que se debe ingresar
        messagebox.askokcancel(message="Datos incorrectos, el dato ingresado es obligatorio y debe ser un digito")
    elif (int(kernel) > 0 and int(memoria) > 0 and int(memoria) <= 9999 and int(kernel) < int(memoria)):
        memoria = int(memoria)
        kernel = int(kernel)
        insertar_kernel(memoria, kernel)
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
entrada_memoria.set(memoria)
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

#ventana 2 *****************************************************
ventana_principal = Tk()
ventana_principal.title("CH MAQUINA")
ventana_principal.geometry("3800x3000")

#realizamos el menu de opciones
menubar = Menu(ventana_principal)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Abrir", command=lambda: abrir_archivo())
menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_command(label="Ejecute", command=lambda: al_ejecutar())
menubar.add_command(label="Muestre memoria", command=lambda: mostrar_memoria_principal_en_pantalla())
menubar.add_cascade(label="Pausa")
menubar.add_command(label="Paso a paso", command=lambda: paso_a_paso())
menubar.add_cascade(label="Salir")
ventana_principal.configure(menu=menubar)

#creamos input de acomulador
Label(ventana_principal,text="Acomulador").grid(row=3, column=0, sticky='nw')
entrada_acomulador = IntVar()
entradaA = Entry(ventana_principal, textvariable=entrada_acomulador)
entradaA.grid(row=3, column=1)

#tabla que muestra las instrucciones de los archivos que se van a ejecutar
treeview_archivos = ttk.Treeview(ventana_principal, height=10, columns=2)
scrollbar = ttk.Scrollbar(ventana_principal, orient = "vertical", command=treeview_archivos.yview )
scrollbar.grid(row=6, column=1, sticky="nse")
treeview_archivos.configure(yscrollcommand=scrollbar.set)
treeview_archivos.grid(row=6, column=1, sticky='nsew')  

#imagen del computador
computer_image = ImageTk.PhotoImage(Image.open("./img/computadora.png"))
computer_image_label = Label(ventana_principal, image=computer_image)
computer_image_label.grid(row=1, column=3, padx=10, pady=10)
btn_text = StringVar()
modo = Button(ventana_principal, textvariable=btn_text).grid(row=2, column=3)
btn_text.set("Modo Kernel")

#tabla que muestra la memoria principal con el acomulador, el SO y las instrucciones de los archivos 
treeview_memoria_principal = ttk.Treeview(ventana_principal, height=10, columns=2)
scrollbar = ttk.Scrollbar(ventana_principal, orient = "vertical", command=treeview_memoria_principal.yview )
scrollbar.grid(row=6, column=4, sticky="nse")
treeview_memoria_principal.configure(yscrollcommand=scrollbar.set)
treeview_memoria_principal.grid(row=6, column=4, sticky='nsew')

#tabla que muestra las variables en la tabla de variables 
treeview_variables = ttk.Treeview(ventana_principal, height=10, columns=2)
treeview_variables.heading("#0", text = "POS")
treeview_variables.heading("#1", text = "Variables")
scrollbar = ttk.Scrollbar(ventana_principal, orient = "vertical", command=treeview_variables.yview )
scrollbar.grid(row=1, column=1, sticky="nse")
treeview_variables.configure(yscrollcommand=scrollbar.set)
treeview_variables.grid(row=1, column=1, sticky='nsew')

#tabla que muestra las etiquetas en la tabla de etiquetas 
treeview_etiquetas = ttk.Treeview(ventana_principal, height=10, columns=2)
treeview_etiquetas.heading("#0", text = "POS")
treeview_etiquetas.heading("#1", text = "Etiquetas")
scrollbar = ttk.Scrollbar(ventana_principal, orient = "vertical", command=treeview_etiquetas.yview )
scrollbar.grid(row=1, column=4, sticky="nse")
treeview_etiquetas.configure(yscrollcommand=scrollbar.set)
treeview_etiquetas.grid(row=1, column=4, sticky='nsew')


#metodo para cargar los archivos en la tabla que muestra las instrucciones de los archivos que se van a ejecutar
def abrir_archivo():
    global instrucciones_archivo
    archivo_abierto=filedialog.askopenfilename(initialdir="/Documents/ch-maquina/programs",
        title="Seleccione archivo",filetypes=(("ch files","*.ch"),
        ("all files","*.*")))
    if archivo_abierto!='':
        archivo=open(archivo_abierto, "r", )
        instrucciones_archivo = archivo.readlines()#Conversión del archivo de texto en una lista por renglones
        archivo.close()
        contador = kernel+1
        for index, instruccion in enumerate(instrucciones_archivo):
            instruccion = instruccion.strip("\n") 
            valor = instruccion.split(" ")
            #eliminamos los comentarios
            if(valor[0].find('//') != 0):
                valor[0] = valor[0].lower()
                instruccion_formateada = " ".join(valor)
                treeview_archivos.insert("" , 'end', text="00" + str(contador), values= (instruccion_formateada,))
                contador += 1 
        almacena_ch_en_memoria_principal(instrucciones_archivo)
        agregar_variables_en_memoria_principal()
        mostrar_memoria_principal_en_pantalla()
        mostrar_variables_en_pantalla(instrucciones_archivo)
        agregar_etiquetas(instrucciones_archivo)
        mostrar_etiquetas_en_pantalla()
        obtener_posicion_memoria_disponible()
        agregar_variables(instrucciones_archivo)


def almacena_ch_en_memoria_principal(instrucciones_archivo):
    global errores
    verificar_sintaxis(instrucciones_archivo)
    #print(len(errores))
    if(len(errores) == 0):
        msgbox = messagebox.askquestion(message="No hay errores, puede ejecutar!!")
        agregar_instrucciones_en_memoria_principal(instrucciones_archivo)
    else:
        ventana_errores = Tk()
        ventana_errores.title("VENTANA DE ERRORES")
        ventana_errores.geometry("500x200")
        Label(ventana_errores, text="Hay errores, no se puede ejecutar").grid(row=1, column=1)
        #tabla que muestra las instrucciones de los archivos que se van a ejecutar
        treeview_errores = ttk.Treeview(ventana_errores, height=10, columns=10)
        scrollbar = ttk.Scrollbar(ventana_errores, orient = "vertical", command=treeview_errores.yview )
        scrollbar.grid(row=2, column=1, sticky="nse")
        treeview_errores.configure(yscrollcommand=scrollbar.set)
        treeview_errores.grid(row=2, column=1, padx=10, sticky='nsew')
        for i in range(0, len(errores)):
            treeview_errores.insert("" , 'end', text="00" + str(i+1), values= (errores[i],))

#metodo para agregar las instrucciones del .ch en la memoria principal 
def agregar_instrucciones_en_memoria_principal(instrucciones_archivo):
    global kernel
    global cantidad_de_comentarios
    contador = kernel+1
    
    for index, instruccion in enumerate(instrucciones_archivo):
        instruccion = instruccion.strip("\n") 
        valor = instruccion.split(" ")
        
        if(valor[0].find('//') != 0):#verifica que no sea un comentario
            valor[0] = valor[0].lower()
            instruccion_formateada = "".join(valor) # une los elementos de la lista y retorna cadenas
            #array de diccionarios
            memoria_principal[contador] = {'tipo': 'instruccion', 'valor': instruccion_formateada}
            contador += 1
            instrucciones_ch.append({'tipo': 'instruccion', 'valor': instruccion_formateada})
        else:
            instrucciones_ch.append({'tipo': 'comentario'})
            cantidad_de_comentarios += 1

        
#metodo para mostrar en pantalla el valor de memoria, estos datos se muestran en la tabla de la memoria principal con el acomulador, el SO y las instrucciones de los archivos 
def mostrar_memoria_principal_en_pantalla():
    global memoria_principal
    #print(memoria_principal)
    #treeview_memoria_principal.delete(*treeview_memoria_principal.get_children())
    for i in range(0, len(memoria_principal)):
        treeview_memoria_principal.insert("" , 'end', text="00" + str(i), values= (memoria_principal[i]['valor'],))
    

#metodo para agregar diccionario de variables en el array de memoria principal
def agregar_variables_en_memoria_principal():
    global variables
    global memoria_principal
    posicion = posicion_memoria_principal()
    for llave in variables:
        memoria_principal[posicion] = {'tipo':'variable', 'valor': variables[llave]['valor'], 'nombre': llave}
        posicion += 1

#verificar en que posicion retorna la primer posicion vacia de memoria principal
def posicion_memoria_principal():
    global memoria_principal
    posicion = 0
    for instruccion in memoria_principal:
        #print(instruccion)
        if(instruccion['tipo']!='vacio'):
            posicion += 1
        else:
            return posicion

#metodo para agregar las variables del .ch en diccionario de variables y sus valores por defecto
def agregar_variables(instrucciones_archivo):
    for instruccion_interna in instrucciones_archivo:
        instruccion_interna = instruccion_interna.strip("\n") 
        instrucciones = instruccion_interna.split(" ")
        llave = instrucciones[1]
        #agregamos el valor por defecto de cada uno de los tipos de variables
        if(instrucciones[0].lower()=="nueva"):
            if(len(instrucciones)==3):
                if(instrucciones[2]=="I"):
                    instrucciones.append("0")
                elif(instrucciones[2]=="L"):
                    instrucciones.append("0")
                elif(instrucciones[2]=="R"):
                    instrucciones.append("0")
                elif(instrucciones[2]=="C"):
                    instrucciones.append(" ")
            variables[llave] = { 'tipo': instrucciones[2], 'valor': instrucciones[3] }
        if(instrucciones[0].lower()=="cargue"):
            #print(memoria_principal[0])
            memoria_principal[0]['valor'] = variables[llave]['valor']
            cargue()
        es_al_ejecutar = True
        if(es_al_ejecutar == True):
            paso_a_paso()
            
            msgbox = messagebox.askquestion(message="Desea continuar?")



#metodo para mostrar en pantalla las variables del archivo .ch
def mostrar_variables_en_pantalla(instrucciones_archivo):
    global variables
    global memoria_principal
    for index, pedasito_de_memoria in enumerate(memoria_principal):
        if pedasito_de_memoria['tipo'] == 'variable':
            nombre_variable = pedasito_de_memoria['nombre']
            treeview_variables.insert("" , 'end', text="00" + str(index), values= (nombre_variable,))

#metodo para agregar las etiquetas del .ch 
def agregar_etiquetas(instrucciones_archivo):
    global etiquetas
    global memoria_principal

    for instruccion_interna in instrucciones_archivo:
        instruccion_interna = instruccion_interna.strip("\n") #quitar espacios de la cadena al principio y al final
        instrucciones = instruccion_interna.split(" ") #lista que contiene como elementos la cadena 
        #agregamos el valor de las etiquetas
        if(instrucciones[0].lower()=="etiqueta"):
            etiquetas[instrucciones[1]] = {'valor': int(instrucciones[2])}

#metodo para encontrar la posicion la cual se le va a asignar a las etiquetas con relacion a las instrucciones del ch
def obtener_posicion_memoria_disponible():
    global memoria_principal
    index = 0
    while(memoria_principal[index]['tipo']=='acumulador' or memoria_principal[index]['tipo']=='SO'):
        index += 1
    return index

#metodo para mostrar en pantalla las variables del archivo .ch
def mostrar_etiquetas_en_pantalla():
    global etiquetas
    global cantidad_de_comentarios
    indice_memoria = obtener_posicion_memoria_disponible()
    for nombre_etiqueta in etiquetas:
        total = (indice_memoria + etiquetas[nombre_etiqueta]['valor']) - cantidad_de_comentarios + 1
        treeview_etiquetas.insert("" , 'end', text="00" + str(total), values= (nombre_etiqueta,))

#metodo para cambiar el modo al ejecutar paso a paso
def paso_a_paso():
    btn_text.set("Modo Usuario")
    Label(ventana_principal, text="Paso a paso").grid(row=0, column=3)
    es_paso_a_paso = True    
    
#metodo que se realiza al momento de ejecutar muestra si hay errores, sino los hay agrega muestra una nueva ventana con los errores 
def al_ejecutar():
    es_al_ejecutar = True
    

#metodo cargue
def cargue():
    entrada_acomulador.set(memoria_principal[0]['valor'])

#metodo que permite verificar sintaxis
def verificar_sintaxis(instrucciones_archivo):
    archivo = instrucciones_archivo
    palabra = []
    for instruccion in archivo:
        #print(instruccion)
        instruccion = instruccion.strip("\n") 
        palabra = instruccion.split(" ")
        palabra[0] = palabra[0].lower()
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
        elif(palabra[0] == "etiqueta"):
            funcion_error_etiqueta(palabra)   
        elif(palabra[0] == "vaya"):
            funcion_error_vaya(palabra) 
        elif(palabra[0] == "vayasi"):
            funcion_error_vaya_si(palabra)
        elif(palabra[0] == "retorne"):
            funcion_error_retorne(palabra)



#verficar sintaxis de las operaciones lea, muestra, imprima, elimine
def funcion_error(palabra):
    if(len(palabra)>2):
        errores.append("Error, se estan utilizando mas de 2 operandos en la operacion "+ palabra[0]) 
    elif(palabra[1] not in variables):
        errores.append("Error, la variable " + palabra[1] + " no ha sido asignada")
    


#verficar sintaxis al momento de que la operacion sea crear una nueva variable
def funcion_error_nueva(palabra):
    global variables
    tipos_datos = ["C", "I", "R", "L"]
    if(len(palabra)>4):
        errores.append("Error, se estan utilizando mas de 4 operandos en la operacion "+ palabra[0])

    if(len(palabra)==3):
        if(palabra[2]=="I"):
            palabra.append("0")
        elif(palabra[2]=="L"):
            palabra.append("0")
        elif(palabra[2]=="R"):
            palabra.append("0")
        elif(palabra[2]=="C"):
            palabra.append(" ")

    if((palabra[2]=="I") and (palabra[3].isdigit()==False)):
        errores.append("Error, el valor de inicializacion "  + palabra[3] + " no es correcto, en el tipo de dato " + palabra[2])
    elif((palabra[2]=="L") and not(palabra[3] == "1" or palabra[3] == "0")):
        errores.append("Error en el el valor de inicializacion  " + palabra[3]  + " no es correcto, en el tipo de dato " + palabra[2])
    elif((palabra[2]=="C") and not(palabra[3].isalpha()==True or palabra[3].isascii()==True)):
        errores.append("Error en el el valor de inicializacion  " + palabra[3]  + " no es correcto, en el tipo de dato " + palabra[2])
    elif((palabra[2]=="R") and (palabra[3].isdecimal()==False)):
        errores.append("Error en el el valor de inicializacion  " + palabra[3]  + " no es correcto, en el tipo de dato " + palabra[2]) 
    elif(palabra[1] not in variables):
        funcion_variable_nombre_valido_variable(palabra)
    elif(palabra[2] not in tipos_datos):
        errores.append("Error, el tipo de dato especificado " + +  palabra[2] + " no ha sido declarado" )
    print(errores)
#verifica que el nombre de la variable no sea una operacion
def funcion_variable_nombre_valido_variable(palabra):
    palabras_operaciones = ["cargue", "almacene","nueva", "lea", "sume", "reste", "multiplique", "divida", "potencia", "modulo", "concatene", "elimine", "extraiga", "Y", "O", "muestre", "vaya", "vayasi", "etiqueta", "retorne"]
    if(palabra[1] in palabras_operaciones):
        errores.append("Error, el nombre de la variable " + palabra[1] +" no es válido"  )
    else:
        variables[palabra[1]] = { 'tipo': palabra[2], 'valor': palabra[3] }
    print(errores)
#validan los errores de las funciones cargue, almacene, multiplique, sume, reste
def funcion_error_cargue_almacene_multiplique_sume_reste(palabra):
    if(len(palabra)>2):
        errores.append("Error, se estan utilizando mas de 2 operandos en la operacion "+ palabra[0])
    elif(palabra[1] not in variables):
        errores.append("Error, la variable " + palabra[1] + " no ha sido asignada")
    elif((variables[palabra[1]]['tipo'] == "L") or (variables[palabra[1]]['tipo'] == "C")):
        errores.append("Error, la variable " + palabra[1] + " no se puede ejecutar en la operacion " + palabra[0] + " porque su tipo de dato es " + variables[palabra[1]]['tipo']) 

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

#valida error de operacion potencia
def funcion_error_potencia(palabra):
    if(len(palabra)>2):
        errores.append("Error, se estan utilizando mas de 2 operandos en la operacion "+ palabra[0])
    elif(palabra[1] not in variables):
        errores.append("Error, la variable " + palabra[1] + " no ha sido asignada")
    elif((variables[palabra[1]]['tipo'] == "L") or (variables[palabra[1]]['tipo'] == "C")):
        errores.append("Error, la variable " + palabra[1] + " no se puede ejecutar en la operacion " + palabra[0] + " porque su tipo de dato es " + variables[palabra[1]]['tipo']) 
    elif((variables[palabra[1]]['valor'].isdigit()==False) or not(variables[palabra[1]]['valor'] <= 0)):
        errores.append("Error, la operacion "+ palabra[0] + " no permite elevar a una portencia " + variables[palabra[1]]['valor'] )

#verficar sintaxis en la operacion concatene
def funcion_error_concatene_extraiga(palabra):
    if(len(palabra)>2):
        errores.append("Error, se estan utilizando mas de 2 operandos en la operacion "+ palabra[0])
    elif(palabra[1] not in variables):
        errores.append("Error, la variable " + palabra[1] + " no ha sido asignada")
    elif((variables[palabra[1]]['tipo'] != "C")):
        errores.append("Error, la variable " + palabra[1] + " no se puede ejecutar en la operacion " + palabra[0] + " porque su tipo de dato es " + variables[palabra[1]]['tipo']) 
    elif((palabra[1].isalpha())==False):
        errores.append("Error, el operando no es alfanumerico "+ palabra[0])

#verficar sintaxis en la operacion concatene error Y O NOT
def funcion_error_y_o_no(palabra):
    if(len(palabra)>4):
        errores.append("Error, se estan utilizando mas de 4 operandos en la operacion " + palabra[0])
    elif(palabra[1] not in variables):
        errores.append("Error, la variable " + palabra[1] + " no ha sido asignada")
    elif((variables[palabra[1]]['tipo'] != "L")):
        errores.append("Error, la variable " + palabra[1] + " no se puede ejecutar en la operacion " + palabra[0] + " porque su tipo de dato es " + variables[palabra[1]]['tipo']) 
    
#verficar sintaxis en la operacion etiqueta
def funcion_error_etiqueta(palabra):
    if(len(palabra)>3):
        errores.append("Error, se estan utilizando mas de 2 operandos en la operacion "+ palabra[0])
    elif(palabra[1] not in etiquetas):
        funcion_variable_nombre_valido_etiqueta(palabra)
    elif(palabra[2].isdigit()==False):
        errores.append("Error, el valor " + palabra[2] + " no es válido para la operación " + palabra[0]  )

#verifica que el nombre de la etiqueta no sea una operacion
def funcion_variable_nombre_valido_etiqueta(palabra):
    palabras_operaciones = ["cargue", "almacene","nueva", "lea", "sume", "reste", "multiplique", "divida", "potencia", "modulo", "concatene", "elimine", "extraiga", "Y", "O", "muestre", "vaya", "vayasi", "etiqueta", "retorne"]
    if(palabra[1] in palabras_operaciones):
        errores.append("Error, el nombre de la de etiqueta " + palabra[1] +" no es válido"  )
    else:
        etiquetas[palabra[1]] = { 'valor': palabra[2] }

#verficar sintaxis en la operacion retorne
def funcion_error_retorne(palabra):
    if(len(palabra)>2):
        errores.append("Error, se estan utilizando mas de 2 operandos en la operacion "+ palabra[0])
    elif(palabra[1].isdigit()==False):
        errores.append("Error, el valor " + palabra[1] +" no es válido para la operación " + palabra[0])

#verficar sintaxis en la operacion vaya
def funcion_error_vaya(palabra):
    if(len(palabra)>2):
        errores.append("Error, se estan utilizando mas de 2 operandos en la operacion "+ palabra[0])

#verficar sintaxis en la operacion vaya_si
def funcion_error_vaya_si(palabra):
    if(len(palabra)>3):
        errores.append("Error, se estan utilizando mas de 3 operandos en la operacion "+ palabra[0])

ventana_principal.mainloop()


