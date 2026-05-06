from tkinter import *
import random
import datetime

operador = ''

precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebidas = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

def clic_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)

def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)

def obtener_resultado():
    global operador
    resultado =str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''

def revisar_check():
    x =0
    for c in cuadros_comidas:
        if variables_comidas[x].get() == 1:
            cuadros_comidas[x].config(state=NORMAL)
            if cuadros_comidas[x].get() == c:
                cuadros_comidas[x].delete(0, END)
            cuadros_comidas[x].focus()
        else:
            cuadros_comidas[x].config(state=DISABLED)
            texto_comidas[x].set('0')
        x+=1

    x = 0
    for c in cuadros_bebidas:
        if variables_bebidas[x].get() == 1:
            cuadros_bebidas[x].config(state=NORMAL)
            if cuadros_bebidas[x].get() == c:
                cuadros_bebidas[x].delete(0, END)
            cuadros_bebidas[x].focus()
        else:
            cuadros_bebidas[x].config(state=DISABLED)
            texto_bebidas[x].set('0')
        x += 1

    x = 0
    for c in cuadros_postres:
        if variables_postres[x].get() == 1:
            cuadros_postres[x].config(state=NORMAL)
            if cuadros_postres[x].get() == c:
                cuadros_postres[x].delete(0, END)
            cuadros_postres[x].focus()
        else:
            cuadros_postres[x].config(state=DISABLED)
            texto_postres[x].set('0')
        x += 1

def total():
    subtotal_comida =0
    p =0
    for cantidad in texto_comidas:
        subtotal_comida += (float(cantidad.get())*precios_comida[p])
        p+=1

    subtotal_bebidas =0
    p =0
    for cantidad in texto_bebidas:
        subtotal_bebidas += (float(cantidad.get())*precios_bebidas[p])
        p+=1

    subtotal_postres =0
    p =0
    for cantidad in texto_postres:
        subtotal_postres += (float(cantidad.get())*precios_postres[p])
        p+=1

    sub_total = subtotal_comida + subtotal_bebidas + subtotal_postres
    impuestos = sub_total *0.7
    total = impuestos + sub_total

    var_costo_comida.set(f'${round(subtotal_comida,2)}')
    var_costo_bebidas.set(f'${round(subtotal_bebidas,2)}')
    var_costo_postres.set(f'${round(subtotal_postres,2)}')
    var_subtotal.set(f'${round(sub_total,2)}')
    var_impuestos.set(f'${round(impuestos,2)}')
    var_total.set(f'${round(total,2)}')

def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f'N# - {random.randint(1000,9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos:\t{num_recibo}\t\t{fecha_recibo}')
    texto_recibo.insert(END, f'*'*70+ '\n')
    texto_recibo.insert(END, 'Items\t\tCant.\tCosto Items\n')
    texto_recibo.insert(END, f'-'*70+ '\n')

    x = 0
    for comida in texto_comidas:
        if comida.get() !='0':
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t'
                                     f'${int(comida.get())*precios_comida[x]}\n')
            x +=1
    x = 0
    for bebidas in texto_bebidas:
        if bebidas.get() !='0':
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebidas.get()}\t'
                                     f'${int(bebidas.get())*precios_bebidas[x]}\n')
            x +=1

    x = 0
    for postres in texto_postres:
        if postres.get() !='0':
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t{postres.get()}\t'
                                     f'${int(postres.get())*precios_postres[x]}\n')
            x +=1
#iniciar tkinter
aplicacion = Tk()

#Tamaño de la ventana
aplicacion.geometry("1020x670+0+0")

#titulo de la ventnana
aplicacion.title("Mi Restaurante -Sistema de Facturacion")

#color de fondo de la ventana
aplicacion.configure(bg="burlywood") # bg -> background

#Panel superior
panel_superior = Frame(aplicacion,bd=1, relief=SUNKEN)
panel_superior.pack(side=TOP)

#etiqueta titulo
etiqueta_titulo = Label(panel_superior,text="Sistema de Facturacion", fg= 'azure4',
                        font = ("Dosis",30),bg = 'burlywood', width=20) #fg = es color de frente
etiqueta_titulo.grid(row=0, column=0)

#panel izquierdo
panel_izquiera = Frame(aplicacion,bd=1, relief=SUNKEN)
panel_izquiera.pack(side=LEFT)

#PANEL COSTOS
panel_costos = Frame(panel_izquiera,bd=1, relief=SUNKEN,bg='azure4',padx=59)
panel_costos.pack(side=BOTTOM)

#panel comidas
panel_comidas = LabelFrame(panel_izquiera,text="Comidas",font=("Dosis",18, "bold"),
                           bd=1, relief=SUNKEN, fg="azure4")
panel_comidas.pack(side=LEFT)

#panel bebidas
panel_bebidas = LabelFrame(panel_izquiera,text="Bebidas",font=("Dosis",18, "bold"),
                           bd=1, relief=SUNKEN, fg="azure4")
panel_bebidas.pack(side=LEFT)

#panel postres
panel_postres = LabelFrame(panel_izquiera,text="Postres",font=("Dosis",18, "bold"),
                           bd=1, relief=SUNKEN, fg="azure4")
panel_postres.pack(side=LEFT)

#Panel derecha
panel_derecha = Frame(aplicacion,bd=1, relief=SUNKEN)
panel_derecha.pack(side=RIGHT)

#panel calculadora
panel_calculadora = Frame(panel_derecha,bd=1, relief=SUNKEN, bg="burlywood")
panel_calculadora.pack()

#panel recibo
panel_recibo = Frame(panel_derecha,bd=1, relief=SUNKEN, bg="burlywood")
panel_recibo.pack()

#panel botones
panel_botones = Frame(panel_derecha,bd=1, relief=SUNKEN, bg="burlywood")
panel_botones.pack()

#lista de productos
lista_comidas = ['pollo', 'cordero','salmon','merluza','kebab','pizza1','pizza2','pizza3']
lista_bebidas = ['agua','soda','jugo','cola','vino1','vino2','cerveza1','cerveza2']
lista_postres = ['helado','Fruta','brownies','flan','mousse','pastel1','pastel2','pastel3']
#generar items comida
variables_comidas =[]
cuadros_comidas = []
texto_comidas = []
contador = 0
for comida in lista_comidas:
    #crear checkbutton
    variables_comidas.append('')
    variables_comidas[contador] = IntVar()
    comida = Checkbutton(panel_comidas, text=comida.title(),font =('Dosis', 19, 'bold'),
                         onvalue=1, offvalue=0,variable=variables_comidas[contador],command=revisar_check)
    comida.grid(row=contador, column=0, sticky=W)

    #crear los cuadros de entrada
    cuadros_comidas.append('')
    texto_comidas.append('')
    texto_comidas[contador] = StringVar()
    texto_comidas[contador].set('0')
    cuadros_comidas[contador] = Entry(panel_comidas,
                                      font=('Dosis', 18, 'bold'),
                                      bd=1,
                                      width=6,
                                      state=DISABLED,
                                      textvariable=texto_comidas[contador])
    cuadros_comidas[contador].grid(row=contador,
                                   column=1)

    contador += 1

#generar items bebidas
variables_bebidas =[]
cuadros_bebidas = []
texto_bebidas = []
contador = 0
for bebidas in lista_bebidas:
    #crear checkbotton
    variables_bebidas.append('')
    variables_bebidas[contador] = IntVar()
    bebidas = Checkbutton(panel_bebidas, text=bebidas.title(),font =('Dosis', 19, 'bold'),
                         onvalue=1, offvalue=0,variable=variables_bebidas[contador],command=revisar_check)
    bebidas.grid(row=contador, column=0, sticky=W)
    #crear los datos de entrada
    cuadros_bebidas.append('')
    texto_bebidas.append('')
    texto_bebidas[contador] = StringVar()
    texto_bebidas[contador].set('0')
    cuadros_bebidas[contador] = Entry(panel_bebidas,
                                      font=('Dosis', 18, 'bold'),
                                      bd=1,
                                      width=6,
                                      state=DISABLED,
                                      textvariable=texto_bebidas[contador])
    cuadros_bebidas[contador].grid(row=contador,
                                   column=1)
    contador += 1

#generar items postres
variables_postres =[]
cuadros_postres = []
texto_postres = []
contador = 0
for postres in lista_postres:
    #crear los checkbutton
    variables_postres.append('')
    variables_postres[contador] = IntVar()
    postres = Checkbutton(panel_postres, text=postres.title(),font =('Dosis', 19, 'bold'),
                         onvalue=1, offvalue=0,variable=variables_postres[contador],command=revisar_check)
    postres.grid(row=contador, column=0, sticky=W)
    # crear los datos de entrada
    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')
    cuadros_postres[contador] = Entry(panel_postres,
                                      font=('Dosis', 18, 'bold'),
                                      bd=1,
                                      width=6,
                                      state=DISABLED,
                                      textvariable=texto_postres[contador])
    cuadros_postres[contador].grid(row=contador,
                                   column=1)
    contador += 1

#variables
var_costo_comida = StringVar()

#etiquetas de costo y compos de entrada
etiqueta_costo_comida = Label(panel_costos,
                              text='Costo comida',
                              font =('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_comida.grid(row =0, column=0)

texto_costo_comida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row =0, column=1,padx=41)

#variables
var_costo_bebidas = StringVar()

#etiquetas de costo y compos de entrada
etiqueta_costo_bebidas = Label(panel_costos,
                              text='Costo bebidas',
                              font =('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_bebidas.grid(row =1, column=0)

texto_costo_bebidas = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_bebidas)
texto_costo_bebidas.grid(row =1, column=1,padx=41)


#variables
var_costo_postres = StringVar()

#etiquetas de costo y compos de entrada
etiqueta_costo_postres = Label(panel_costos,
                              text='Costo postres',
                              font =('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_postres.grid(row =2, column=0)

texto_costo_postres = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_postres)
texto_costo_postres.grid(row =2, column=1,padx=41)

#variables
var_subtotal = StringVar()

#etiquetas de costo y compos de entrada
etiqueta_subtotal = Label(panel_costos,
                              text='Subtotal',
                              font =('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_subtotal.grid(row =0, column=2)

texto_subtotal = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_subtotal)
texto_subtotal.grid(row =0, column=3,padx=41)

#variables
var_impuestos = StringVar()

#etiquetas de costo y compos de entrada
etiqueta_impuestos = Label(panel_costos,
                              text='Impuestos',
                              font =('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_impuestos.grid(row =1, column=2)

texto_impuestos = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_impuestos)
texto_impuestos.grid(row =1, column=3,padx=41)

#variables
var_total = StringVar()

#etiquetas de costo y compos de entrada
etiqueta_total = Label(panel_costos,
                              text='Total',
                              font =('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_total.grid(row =2, column=2)

texto_total = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_total)
texto_total.grid(row =2, column=3,padx=41)

#botones
botones = ['total','recibo','guardar','resetear']
botones_creados =[]

columnas = 0
for botone in botones:
    botone = Button(panel_botones,
                    text= botone.title(),
                    font=('Dosis', 11, 'bold'),
                    fg='white',
                    bg='azure4',
                    bd=1,
                    width=9)
    botones_creados.append(botone)
    botone.grid(row=0,column=columnas)
    columnas += 1
botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
#area de recibo
texto_recibo =Text(panel_recibo,
                   font=('Dosis', 12, 'bold'),
                   bd=1,
                   width=42,
                   height=10)
texto_recibo.grid(row=0,column=0)

#calculadora
visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis', 16, 'bold'),
                          width=28,
                          bd=1)
visor_calculadora.grid(row=0,column=0, columnspan=4)
botones_calculadora = ['7','8','9','+','4','5','6','-','1','2','3','*','R','B','0','/']

botones_guardados =[]

fila =1
columna = 0
for botone in botones_calculadora:
    botone = Button(panel_calculadora,
                    text= botone.title(),
                    font=('Dosis', 12, 'bold'),
                    fg ='white',
                    bg='azure4',
                    bd=1,
                    width=8)
    botones_guardados.append(botone)
    botone.grid(row=fila,column=columna)
    if columna == 3:
        fila += 1
    columna += 1

    if columna == 4:
        columna =0

botones_guardados[0].config(command=lambda : clic_boton('7'))
botones_guardados[1].config(command=lambda : clic_boton('8'))
botones_guardados[2].config(command=lambda : clic_boton('9'))
botones_guardados[3].config(command=lambda : clic_boton('+'))
botones_guardados[4].config(command=lambda : clic_boton('4'))
botones_guardados[5].config(command=lambda : clic_boton('5'))
botones_guardados[6].config(command=lambda : clic_boton('6'))
botones_guardados[7].config(command=lambda : clic_boton('-'))
botones_guardados[8].config(command=lambda : clic_boton('1'))
botones_guardados[9].config(command=lambda : clic_boton('2'))
botones_guardados[10].config(command=lambda : clic_boton('3'))
botones_guardados[11].config(command=lambda : clic_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda : clic_boton('0'))
botones_guardados[15].config(command=lambda : clic_boton('/'))

#evitar maximizar
aplicacion.resizable(0, 0)

#evitar que la pantalla se cierre
aplicacion.mainloop()
