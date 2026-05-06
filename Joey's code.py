import tkinter as tk
from PIL import ImageTk, Image
window = tk.Tk()
import requests

# imports the BeautifulSoup library, that lets us format site info in a readable way.
from bs4 import BeautifulSoup

# takes the current site address we want to use and stores it as a variable called "URL"

window.title("AMAZING guess the brainrot quiz!")

window.geometry("500x500")

image = Image.open(r"C:\Users\zjmajor\OneDrive - Hatboro-Horsham School District\steal a brainrot base.jpeg")

resizedImage = image.resize((600,600))

photo = ImageTk.PhotoImage(resizedImage)

label1 = tk.Label(image=photo)

label1.image = photo

label1.place(x=-50,y=-50)

label2 = tk.Label()

window.mainloop()
