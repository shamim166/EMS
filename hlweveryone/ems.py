from customtkinter import *
from PIL import Image  # Import the Image module from PIL

window = CTk()
window.geometry('930x800')
window.resizable(0, 0)
window.title("Employee Management System")

# Load and display logo image
logo = CTkImage(Image.open('logo.png'), size=(930, 250))
logolabel = CTkLabel(window, image=logo)
logolabel.grid(row=0, column=0)  # Corrected spelling of "column"

window.mainloop()
