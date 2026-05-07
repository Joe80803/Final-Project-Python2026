import tkinter as tk

from PIL import ImageTk, Image
import tkinter.font as tkFont
window = tk.Tk()

# imports the BeautifulSoup library, that lets us format site info in a readable way.

# takes the current site address we want to use and stores it as a variable called "URL"

window.title("AMAZING guess the brainrot quiz!")

window.geometry("500x500")

image = Image.open(r"C:\Users\zjmajor\OneDrive - Hatboro-Horsham School District\steal a brainrot base.jpeg")

resizedImage = image.resize((600,600))

photo = ImageTk.PhotoImage(resizedImage)

label1 = tk.Label(image=photo)

label1.image = photo

label1.place(x=-50,y=-50)

questionNumber = 1



label2 = tk.Label(
    window,
    text=("question" + str(questionNumber)),
    fg="black",
    bg="white",
    width= 20,
    height= 5,
    font=tkFont.Font(family="Comic sans", size=19, weight="bold", slant="italic")
)

label2.place(x=100,y=10)

window.mainloop()
