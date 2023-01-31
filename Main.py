from tkinter import TOP, Button, Frame, PhotoImage, ttk
from ttkthemes import ThemedTk, ThemedStyle
from Facturas import caja_cargar_factura
from CRUD_articulos import crud_articulos
from CRUD_clientes import crud_clientes


class programa(ThemedTk):
    def __init__(self):
        super().__init__()

        self.estilo = ThemedStyle(self).theme_use('equilux')

        #self.comprobar_darkmode()

        self.wm_title('Facturacion textil')
        self.iconbitmap(default='.media\\favicon.ico')
        self.configure(background='#464646', width=1280, height=720)

        self.img_salir = PhotoImage(file='.media\\salir_b.png')

        self.salir = ttk.Button(self, text='Salir', compound=TOP,
                                command=self.destroy)
        self.salir.place(relx=0.01, rely=0.5, anchor='w')

        self.cargar_widgets()

    def cargar_widgets(self):
        fr_principal = ttk.Frame(self)
        fr_principal.place(relx=0.5, rely=0.5, relwidth=0.4, relheight=0.2, anchor='center')

        boton_1 = ttk.Button(fr_principal, text='Ventas', compound=TOP,
                             command=self.ventas)
        boton_2 = ttk.Button(fr_principal, text='Clientes', compound=TOP,
                             command=self.clientes)
        boton_3 = ttk.Button(fr_principal, text='Articulos', compound=TOP,
                             command=self.articulos)
        
        boton_1.place(relwidth=0.33, relheight=1, relx=0)
        boton_2.place(relwidth=0.33, relheight=1, relx=0.33)
        boton_3.place(relwidth=0.33, relheight=1, relx=0.66)

    def ventas(self):
        pass

    def clientes(self):
        fr_secundario = crud_clientes(self)
        pass

    def articulos(self):
        fr_secundario = crud_articulos(self)
        pass

        #self.img_darkmode = PhotoImage(file='.media\\oscuro.png')
        #self.img_lightmode = PhotoImage(file='.media\\claro.png')

        #self.boton_dark = Button(self,
        #                         **colores_principales,
        #                         border=0,
        #                         compound=TOP,
        #                         command=self.switch_darkmode)
        #self.boton_dark.place(relx=0.99, rely=0.11, anchor='se')

        #if dark_mode == True:
        #    self.boton_dark.config(text='Modo: oscuro', image=self.img_darkmode)

        #else:
        #    self.boton_dark.config(text='Modo: claro', image=self.img_lightmode)

    #def comprobar_darkmode(self):
    #    if dark_mode == False:
    #        colores_principales['bg'] = '#909090'
    #        colores_principales['activebackground'] = '#808080'

    #    else:
    #        colores_principales['bg'] = '#454545'
    #        colores_principales['activebackground'] = '#353535'

    #def switch_darkmode(self):
    #    global dark_mode

    #    if dark_mode == True:
    #        dark_mode = False

    #    else: dark_mode = True

    #    self.comprobar_darkmode()

principal = programa()
principal.mainloop()