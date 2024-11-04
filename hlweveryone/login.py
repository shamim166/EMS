from customtkinter import *
from PIL import Image
from tkinter import messagebox

# Predefined username and password
USERNAME = "shamim"
PASSWORD = "1234"

def login():
    if usernameEntry.get() == '' or userpass.get() == '':
        messagebox.showerror('Error', 'All fields are required')
    elif usernameEntry.get() == USERNAME and userpass.get() == PASSWORD:
        messagebox.showinfo('Success', 'Login Successful')
    else:
        messagebox.showerror('Error', 'Invalid Username or Password')
        root.destroy()
        import ems

root = CTk()
root.geometry('930x478')
root.resizable(0, 0)
root.title("Login Page")

# Load and display background image
image = CTkImage(Image.open('cover3.jpg'), size=(930, 478))
imagelebel = CTkLabel(root, image=image, text="")
imagelebel.place(x=0, y=0)

# Username and password entry fields
usernameEntry = CTkEntry(root, placeholder_text='Enter Your Username', width=160, height=35,
                         fg_color="#F7F7F7", border_color="#1F6AA5", corner_radius=0, text_color='black')
usernameEntry.place(x=50, y=150)

userpass = CTkEntry(root, placeholder_text='Enter Your Password', width=160, height=35,
                    fg_color="#F7F7F7", border_color="#1F6AA5", corner_radius=0, show='*', text_color='black')
userpass.place(x=50, y=200)

# Login button with command to call login function
loginButton = CTkButton(root, text='Login', height=35, cursor='hand2', command=login)
loginButton.place(x=60, y=250)

root.mainloop()
