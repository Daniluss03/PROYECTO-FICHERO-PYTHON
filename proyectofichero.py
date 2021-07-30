from tkinter import*
from tkinter import filedialog as Filedialog
from io import open


ruta = ""    # la  utilizaremos para almacenar la ruta del fichero

def nuevo():
    global ruta
    mensaje.set("Nuevo Fichero")
    ruta=""
    texto.delete(1.0,"end")
    root.title(" Mi editor ") 
def abrir():
    global ruta
    mensaje.set("Abrir Fichero")
    ruta = Filedialog.askopenfilename(
        initialdir='.',
        filetype=(("ficheros de texto","*.txt"),),
        title="Abrir un nuevo fichero ")
    if ruta !="":
        fichero=open(ruta,'r')
        contenido=fichero.read()
        texto.delete(1.0,'end')
        texto.insert('insert',contenido)
        fichero.close()
        root.title(ruta + " - Mi editor ")    
def guardar():
    global ruta
    mensaje.set("Guardar Fichero")
    if ruta !="":
        contenido=texto.get(1.0,'end-1c')# el enos 1 c es para el salto de linea
        fichero =open(ruta,'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set(" Fichero guardado correctamente")
    else:
        guardar_como()         
def guardar_como():
    global ruta
    mensaje.set(" Guardar Fichero como ")
    fichero=Filedialog.asksaveasfile(title="guardar fichero ",mode='2',defaultextension="txt")
    if fichero is not None:
        ruta= fichero.name
        contenido=texto.get(1.0,'end-1c')# el enos 1 c es para el salto de linea
        fichero =open(ruta,'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set(" Fichero guardado correctamente")
    else:
        mensaje.set("guardado cancelado")
        ruta =""    


#configuracion de la raiz 
root=Tk()
root.title("Mi Editor")


# menu superior 
menubar=Menu(root)
filemenu =Menu(menubar,tearoff=0)
filemenu.add_command(label="Nuevo",command=nuevo)
filemenu.add_command(label="Abrir",command=abrir)
filemenu.add_command(label="Guardar ",command=guardar)
filemenu.add_command(label="Guardar como",command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Salir",command=root.quit)
menubar.add_cascade(menu=filemenu,label="Archivo")
#caja de texto central
texto=Text(root)
texto.pack(fill= "both",expand=1)
texto.config(bd=0,padx=6,pady=4,font=("Consolas",12))

#monitor inferior
mensaje=StringVar()
mensaje.set("Bienvenido a tu editor ")
monitor=Label(root,textvar=mensaje,justify='left')
monitor.pack(side="left")


root.config(menu=menubar)
#finalmente bucle de la aplicacion
root.mainloop()
