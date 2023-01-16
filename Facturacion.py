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
ventana.geometry('1366x768')

x = Label(ventana, text='hola')
x.place(relx=0.5, rely=0.5)
#fondo = PhotoImage(file='media\\wallpaper.gif')

#canvas = Canvas(ventana, width=fondo.width(), height=fondo.height())
#canvas.pack()
#canvas.create_image(0, 0, image=fondo, anchor='nw')

ventana.mainloop()