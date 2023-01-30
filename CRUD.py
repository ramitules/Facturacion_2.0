from tkinter import Button, Frame

class interfaz_crud(Frame):
    def __init__(self, master=None):
        self.fondo = '#2E2E2E'
        self.fondo_sec = '#3E3E3E'

        super().__init__(master, width=1000, height=400, bg=self.fondo)
        self.place(relx=0.5, rely=0.5, anchor='center')

        self.fr_botones = Frame(self, background=self.fondo)
        self.fr_botones.place(x=0, y=0, width=100, relheight=1)

        self.fr_lista = Frame(self, background=self.fondo_sec)
        self.fr_lista.place(x=100, y=0, width=700, relheight=1)

        self.fr_atributos = Frame(self, background=self.fondo)
        self.fr_atributos.place(x=900, y=0, width=200, relheight=0.99)

        self.b_nuevo = Button(self.fr_botones,
                              background=self.fondo_sec,
                              foreground='#FFFFFF',
                              border=0,
                              text='Crear',
                              command=self.f_crear)
        self.b_nuevo.place(relx=0.5, rely=0.2, anchor='center', relwidth=0.9)

        self.b_modificar = Button(self.fr_botones,
                                  background=self.fondo_sec,
                                  foreground='#FFFFFF',
                                  border=0,
                                  text='Modificar',
                                  command=self.f_crear)
        self.b_modificar.place(relx=0.5, rely=0.4, anchor='center', relwidth=0.9)

        self.b_eliminar = Button(self.fr_botones,
                                 background=self.fondo_sec,
                                 foreground='#FFFFFF',
                                 border=0,
                                 text='Eliminar',
                                 command=self.f_eliminar)
        self.b_eliminar.place(relx=0.5, rely=0.6, anchor='center', relwidth=0.9)

        self.cargar_widgets()

    def cargar_widgets(self):
        pass

    def f_crear(self):
        pass

    def f_modificar(self):
        pass

    def f_eliminar(self):
        pass

    def f_guardar(self):
        pass
    
    def f_cancelar(self):
        for widget in self.fr_atributos.winfo_children():
            widget.destroy()

    def f_salir(self):
        self.master.destroy()