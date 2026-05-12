import random
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

def intro():
    print("Hello and welcome to the Guess the Brainrot quiz.")
    print("There will be 10 questions and you will be graded so do your best.")
    input("Good Luck! (type anything to move on) ")
    playRound(0, 0)

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
    if currentSpot == 10:
        end(score)
        return currentSpot, score
    else:
        playRound(currentSpot,score)
        return currentSpot, score


def tryAgain(currentSpot,score):
    print("Try again.")
    print("The Correct answer was "+brainrots[currentSpot]+".")
    currentSpot = currentSpot + 1
    if currentSpot == 10:
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



intro()