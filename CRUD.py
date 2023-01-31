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
                                      command=self.f_crear)
        self.b_modificar.place(relx=0.5, rely=0.4, anchor='center', relwidth=0.9)

        self.b_eliminar = ttk.Button(self.fr_botones,
                                     text='Eliminar',
                                     command=self.f_eliminar)
        self.b_eliminar.place(relx=0.5, rely=0.6, anchor='center', relwidth=0.9)

        self.cargar_widgets()

    def f_atras(self):
        self.destroy()

    def f_guardar(self):
        pass
    
    def f_cancelar(self):
        for widget in self.fr_atributos.winfo_children():
            widget.destroy()

    def f_salir(self):
        self.master.destroy()