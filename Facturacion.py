from tkinter import *

class ventana_principal(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.crear_widgets()

    def crear_widgets(self):
        self.ventas = Button(self)
        self.ventas.config(width='20', height='20')
        self.ventas.pack(anchor='center')

ventana = Tk()
ventana.wm_title('Facturacion textil')
ventana.iconbitmap(default=".media\\favicon.ico")
ventana.config(bg='#404040', width='1366', height='768')

x = Frame(ventana, width='400', height='400', bg='black')
x.place(relx=0.5, rely=0.5)
#fondo = PhotoImage(file='media\\wallpaper.gif')

#canvas = Canvas(ventana, width=fondo.width(), height=fondo.height())
#canvas.pack()
#canvas.create_image(0, 0, image=fondo, anchor='nw')

ventana.mainloop()