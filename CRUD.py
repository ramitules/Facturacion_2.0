from tkinter import ttk

class interfaz_crud(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.place(relx=0.5, rely=0.5, relwidth=0.8, relheight=0.6, anchor='center')

        self.fr_botones = ttk.Frame(self)
        self.fr_botones.place(relx=0, y=0, relwidth=0.1, relheight=1)

        self.fr_lista = ttk.Frame(self)
        self.fr_lista.place(relx=0.1, y=0, relwidth=0.65, relheight=1)

        self.fr_atributos = ttk.Frame(self)
        self.fr_atributos.place(relx=0.75, y=0, relwidth=0.25, relheight=1)

        self.b_atras = ttk.Button(self.fr_botones,
                                  text='Atras',
                                  command=self.f_atras)
        self.b_atras.place(relx=0, rely=0, relwidth=0.5)

        self.b_crear = ttk.Button(self.fr_botones,
                                  text='Crear',
                                  command=self.f_crear)
        self.b_crear.place(relx=0.5, rely=0.2, anchor='center', relwidth=0.9)

        self.b_modificar = ttk.Button(self.fr_botones,
                                      text='Modificar',
                                      command=self.f_modificar)
        self.b_modificar.place(relx=0.5, rely=0.4, anchor='center', relwidth=0.9)

        self.b_eliminar = ttk.Button(self.fr_botones,
                                     text='Eliminar',
                                     command=self.f_eliminar)
        self.b_eliminar.place(relx=0.5, rely=0.6, anchor='center', relwidth=0.9)

    def f_crear(self):
        self.boton_aceptar = ttk.Button(self.fr_atributos,
                                        text='Aceptar',
                                        command=self.f_aceptar_crear)
        self.boton_aceptar.place(relx=0.05, rely=0.93, relwidth=0.4)

        self.boton_cancelar = ttk.Button(self.fr_atributos,
                                         text='Cancelar',
                                         command=self.f_cancelar)
        self.boton_cancelar.place(relx=0.5, rely=0.93, relwidth=0.4)

    def f_atras(self):
        self.destroy()

    def f_guardar(self):
        pass
    
    def f_cancelar(self):
        for widget in self.fr_atributos.winfo_children():
            widget.destroy()