#Hangman game engine
import random
def hangman():

    WordList = ["challenge","tree","computer","sanglier","electrical","space","letter","summer","windows","rice","interface","winner"]
    x=random.choice(WordList)
    y = ""
    z = ""
    life = 10
    for i in x :
        y += "_ "
 
    for i in x:
        z += i + " "

    while life >0 and y != z:
        print(f"{y} You still have {life} lives")
        letter:str = str(input(f" Choose a letter ? You have {life} lives "))

        if letter == x:
            print (f"Good job you find the word ! You still have {life} lives !")
            break

        if len(letter) != 1 or letter.isalpha() != True:
            print("Please enter a single letter or if you have find the word, the word completely")
            continue

        if letter in z:
            for i in range(len(z)):
                if z[i] == letter:
                    y = y[:i] + letter + y[i + 1:] 
        else:
            life = life-1
            print (f"oh nooo, you lost a life, letter {letter.upper()} is not here")

    if y == z:
            print (f"Good job you find the word ! You still have {life} lives !")
    else:
        print("You lose, you no longer have any life ")

hangman()
