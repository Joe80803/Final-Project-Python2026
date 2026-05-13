import tkinter as tk
import random
from PIL import ImageTk, Image
import tkinter.font as tkFont
window = tk.Tk()
# something
# imports the BeautifulSoup library, that lets us format site info in a readable way.

# takes the current site address we want to use and stores it as a variable called "URL"
brainrots = ["Ballerina Cappuccina", "Blueberrinni Octopussini","Bobrito Bandito", "Bombardiro Crocodilo", "Bombombini Gusini",
             "Boneca Ambalabu", "Brr Brr Patapim", "Brri Brri Bicus Dicus Bombicus", "Burbaloni Lulilolli", "Cappuccino Assassino",
             "Chef Crabracadabra","Chimpanzini Bananini", "Cocofanto Elefanto", "Frigo Camelo", "Frulli Frulla","Gangster Footera",
             "Garam Mararam & Madu Dung Dung", "Giraffa Celeste", "Glorbo Fruttodrillo", "Graipussi Medussi", "Il Cacto Hipopotamo",
             "La Vaca Saturno Saturnita", "Lirili Larila", "Orangutini Ananasini", "Pot Hotspot", "Rhino Toasterino", "Ta Ta Ta Sahur",
             "Tigrrullini Watermellini","Tracotucotulu Delapeladustuz","Tralalero Tralala","Tric Trac Baraboom","Trippi Troppi",
             "Trulimero Trulicina","Tung Tung Tung Sahur","U Din Din Din Din Dun","Zibra Zubra Zibralini", "Alessio", "Antonio",
             "Armodillo Fartillo", "Avocadini Guffo", "Bombardino Cignocino Toasterino", "Bearorito Applepitolirotito", "Bearcketini",
             "Bobrini Zucchini", "Bomboclat Crocolat", "Bombardiro Squido", "Buffalo Cactusuffalo", "Carlo", "Cameloni Meleloni",
             "Chimpanzini Cappuccini", "Cocosino Rhino", "Don Pitrolio", "Vroosh Boosh", "Dragonfruti Axuluti", "El Toro Loco",
             "Eaglucci Watermelucci", "Foxita Ananasita", "Gallo Radice", "Fritto Peppino Supremo", "Gorgonzilla", "Grr Grr Baraboom",
             "Gusino Tractorino", "Hamsterino Busitino", "Helicopter Fenicopter", "Ice Ice Bearlini Polari Orangini", "Johnny Applesllice",
             "Justin Beaver", "Lionessi Mayonessi", "Matteo", "Mama Pasta Mista", "Quesini Medussi", "Squalo Cocodilo", "Tracturo Dinosauro"
]


def playRound(currentSpot, score):

    correct = brainrots[currentSpot]


    wrongAnswers = random.sample(brainrots, 3)


    while correct in wrongAnswers:
        wrongAnswers = random.sample(brainrots, 3)


    options = wrongAnswers + [correct]


    random.shuffle(options)

    print("Which brainrot is this?")




    print("1.", options[0])
    print("2.", options[1])
    print("3.", options[2])
    print("4.", options[3])

    guess = input("Choose a number: ")


    selected = options[int(guess) - 1]

    if selected == correct:
        currentSpot, score = yourRight(currentSpot, score)
    else:
        currentSpot, score = tryAgain(currentSpot, score)


def yourRight(currentSpot,score):
    print("Your right!")
    currentSpot = currentSpot + 1
    score = score + 1
    if currentSpot == 20:
        end(score)
        return currentSpot, score
    else:
        playRound(currentSpot,score)
        return currentSpot, score


def tryAgain(currentSpot,score):
    print("Try again.")
    print("The Correct answer was "+brainrots[currentSpot]+".")
    currentSpot = currentSpot + 1
    if currentSpot == 20:
        end(score)
        return currentSpot,score
    else:
        playRound(currentSpot,score)
        return currentSpot,score


def review():
    print("Lets try the ones you got wrong.")


def end(score):
    print("You got a "+str(score)+"/10 correct.")
    more = input("Would you like to review the ones you missed? (YES/NO) ")
    if more == "YES":
        review()
    else:
        print("Thanks for playing!")




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

A = tk.Button(
    text= selected[0][1],
    width=30,
    height=5,
    bg="white",
    fg="black",
)

A.place(x=25, y=300)

B = tk.Button(
    text="B",
    width=30,
    height=5,
    bg="white",
    fg="black",
)

B.place(x=250, y=300)

C = tk.Button(
    text="C",
    width=30,
    height=5,
    bg="white",
    fg="black",
)

C.place(x=25, y=390)

D = tk.Button(
    text="D",
    width=30,
    height=5,
    bg="white",
    fg="black",
)

D.place(x=250, y=390)





window.mainloop()
