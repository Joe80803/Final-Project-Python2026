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
    text=(str(questionNumber)),
    fg="black",
    bg="white",
    width= 5,
    height= 3,
    font=tkFont.Font(family="Comic sans", size=20, weight="bold", slant="italic")
)

label2.place(x=1, y=2)

label3 = tk.Label(
    window,
    text=("Which brainrot is this?"),
    fg="black",
    bg="white",
    width= 100,
    height= 3,
    font=tkFont.Font(family="Comic sans", size=15, weight="bold", slant="italic")
)

label3.place(x=-345,y=200)

window.mainloop()
