import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
import random
import string
import os.path


def generate_password():
    password_entry.delete(0, tk.END)
    length = int(length_entry.get())
    password = ''.join(random.choices(string.ascii_letters +
                                      string.digits + string.punctuation, k=length))
    password_entry.insert(0, password)


def copy_password(event):
    password = password_entry.get()
    window.clipboard_clear()
    window.clipboard_append(password)
    messagebox.showinfo("Copiado", "La contraseña se copió al portapapeles")


def exit_app():
    window.destroy()


window = tk.Tk()
window.title("Generador de Contraseñas")
window.geometry("970x900")

# Establecer el color de fondo de la ventana a negro
window.configure(background="#1C044D")

length_label = ttk.Label(window, text="Longitud de la contraseña:")
length_label.pack(pady=(50, 5))
length_label.pack()

length_entry = ttk.Entry(window)
length_entry.pack()

generate_button = ttk.Button(
    window, text="Generar contraseña", command=generate_password)
# Separación adicional entre el botón "Generar contraseña" y el campo de contraseña
generate_button.pack(pady=(10, 5))

# Establecer estilo para el campo de contraseña
style = ttk.Style()
style.configure("BW.TEntry", foreground="#27FF00", background="28046C")

password_entry = ttk.Entry(window, style="BW.TEntry")
password_entry.pack()

# Enlazar el evento de clic izquierdo para copiar la contraseña
password_entry.bind("<Button-1>", copy_password)
password_entry.pack(pady=(10))

# Crear un botón para salir de la aplicación
exit_button = ttk.Button(window, text="Salir", command=exit_app)
# Separación adicional entre el campo de contraseña y el botón "Salir"

# Cambia "imagen.png" al nombre de tu archivo de imagen
image_path = r"c:\Users\Usuario\OneDrive\PROGRAMACION\PROGRAMACION\PROYECTOS_PERSONALES\Generador de Contraseñas\img\wnime Perfil.jpg"
 
if os.path.exists(image_path):
    # El archivo existe, ahora puedes abrirlo
    image = Image.open(image_path)
else:
    print("El archivo de imagen no existe en la ruta especificada:", image_path)


image = Image.open(image_path)
# Ajusta el tamaño de la imagen según sea necesario
image = image.resize((500, 400))
image_tk = ImageTk.PhotoImage(image)

image_label = ttk.Label(window, image=image_tk)
image_label.pack()
exit_button.pack(pady=(5, 10))

window.mainloop()
