import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()

window.title("AMAZING guess the brainrot quiz!")

window.geometry("500x500")

background = tk.Image(r"C:\Users\zjmajor\OneDrive - Hatboro-Horsham School District\steal a brainrot base.jpeg")

label = tk.Label(
    text="",
    fg="",
    bg="",
    width=25,
    height=5
)

label.place(x=150, y=50)

window.mainloop()
