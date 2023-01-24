from variables_globales import *
from tkinter import TOP, Button, Frame, PhotoImage, Tk, Toplevel
from Clientes import caja_cargar_cliente, caja_modificar_cliente, caja_listar_clientes


class programa(Tk):
    def __init__(self):
        super().__init__()

        self.comprobar_darkmode()

        self.wm_title('Facturacion textil')
        self.geometry('1280x720')
        self.iconbitmap(default='.media\\favicon.ico')
        self['bg'] = colores_principales['bg']

        self.img_salir = PhotoImage(file='.media\\salir.png')
        self.salir = Button(self,
                            **colores_principales,
                            border=0,
                            text='Salir',
                            compound=TOP,
                            image=self.img_salir,
                            command=self.destroy)
        self.salir.place(relx=0.01, rely=0.5, anchor='w')

        self.img_darkmode = PhotoImage(file='.media\\oscuro.png')
        self.img_lightmode = PhotoImage(file='.media\\claro.png')

        self.boton_dark = Button(self,
                                 **colores_principales,
                                 border=0,
                                 compound=TOP,
                                 command=self.switch_darkmode)
        self.boton_dark.place(relx=0.99, rely=0.11, anchor='se')

        if dark_mode == True:
            self.boton_dark.config(text='Modo: oscuro', image=self.img_darkmode)

        else:
            self.boton_dark.config(text='Modo: claro', image=self.img_lightmode)

    def comprobar_darkmode(self):
        if dark_mode == False:
            colores_principales['bg'] = '#909090'
            colores_principales['activebackground'] = '#808080'

        else:
            colores_principales['bg'] = '#454545'
            colores_principales['activebackground'] = '#353535'

    def switch_darkmode(self):
        global dark_mode

        if dark_mode == True:
            dark_mode = False

        else: dark_mode = True

        self.comprobar_darkmode()


class caja_principal(Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self['bg'] = colores_principales['bg']
        self.boton_1 = Button(self, **colores_principales)
        self.boton_1.place(relwidth=0.3, relheight=1, relx=0.1)

        self.boton_2 = Button(self, **colores_principales)
        self.boton_2.place(relwidth=0.3, relheight=1, relx=0.4)

        self.boton_3 = Button(self, **colores_principales)
        self.boton_3.place(relwidth=0.3, relheight=1, relx=0.7)

        self.cargar_widgets()

    def cambiar(self):
        self.destroy()

        nueva_caja = caja_multiuso(self.master)
        nueva_caja.place(**medidas_principales)

    def cargar_widgets(self):
        self.img_ventas = PhotoImage(file='.media\\venta.png')
        self.boton_1.config(image=self.img_ventas,
                            text='Ventas',
                            compound=TOP,
                            border=0,
                            command=self.cambiar)
        
        self.img_clientes = PhotoImage(file='.media\\cliente.png')
        self.boton_2.config(image=self.img_clientes,
                            text='Clientes',
                            compound=TOP,
                            border=0,
                            command=self.cambiar)
        
        self.img_articulos = PhotoImage(file='.media\\articulo.png')
        self.boton_3.config(image=self.img_articulos,
                            text='Articulos',
                            compound=TOP,
                            border=0,
                            command=self.cambiar)
        

class caja_multiuso(caja_principal):
    def __init__(self, master=None):
        super().__init__(master)

        self.boton_atras = Button(self)
        self.boton_atras.config(**colores_principales,
                                text='Atras',
                                border=0,
                                command=self.cambiar)
        self.boton_atras.place(relx=0)
        
    def cambiar(self):
        self.destroy()

        nueva_caja = caja_principal(self.master)
        nueva_caja.place(**medidas_principales)

    def nueva_ventana(self, boton):
        nueva = Toplevel(self)

        if boton['text'] == 'Cargar':
            nueva.geometry('400x400')
            nueva.wm_title('Cargar cliente')
            caja_cargar_cliente(nueva)
            
        elif boton['text'] == 'Editar':
            nueva.geometry('400x400')
            nueva.wm_title('Modificar cliente')
            caja_modificar_cliente(nueva)

        elif boton['text'] == 'Listar':
            nueva.geometry('1280x400')
            nueva.wm_title('Listar clientes')
            caja_listar_clientes(nueva)

    def cargar_widgets(self):
        self.img_cargar = PhotoImage(file='.media\\cargar.png')
        self.boton_1.config(image=self.img_cargar,
                            text='Cargar',
                            compound=TOP,
                            border=0,
                            command=lambda: self.nueva_ventana(self.boton_1))

        self.img_editar = PhotoImage(file='.media\\editar.png')
        self.boton_2.config(image=self.img_editar,
                            text='Editar',
                            compound=TOP,
                            border=0,
                            command=lambda: self.nueva_ventana(self.boton_2))

        self.img_listar = PhotoImage(file='.media\\listar.png')
        self.boton_3.config(image=self.img_listar,
                            text='Listar',
                            compound=TOP,
                            border=0,
                            command=lambda: self.nueva_ventana(self.boton_3))

principal = programa()

caja = caja_principal(principal)
caja.place(**medidas_principales)

principal.mainloop()