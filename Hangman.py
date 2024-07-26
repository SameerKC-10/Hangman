from tkinter import *
import random
import turtle


root = Tk()
root.geometry("700x700")
root.title("Hangman Game by @Samkumarchandwani")
top = Toplevel()
top.geometry("650x200")
top.title("Choose a Theme")

Fruits = ["apple", "banana", "mango", "watermelon"]
Countries = ["pakistan", "england", "oman", "jamaica"]
Animals = ["tiger", "fish", "blue whale", "gorilla"]

def main():
    global wrongs
    global word  # Main function
    global user
    global t
    t = turtle.Turtle()     # initialzing cursor      
    word = random.choice(Theme) # Choosing the word the user has to guess           
    visual(word) # Sending the chosen word into a function that will display the underscores based on the words
    entry_label = Label(root, text="Letter:", font="Ariel 18")  
    entry_label.grid(row=5, column=0, pady=50)
    user = Entry(root, width=3,font="Ariel 12")   # where user will type 
    user.grid(row=5, column=1, pady=50)
    guess_button = Button(root, text="Guess", font="Ariel 12", command=lambda: guess(user.get()))
    guess_button.grid(row=5, column=2, pady=50)
    wrong_label = Label(root, text="Letters guessed wrong: ", font="Ariel 16", anchor="w")
    wrong_label.grid(row=6, column=0, columnspan=4)
    wrongs = 0 #Variable to count the wrong of the user


def update(wrongs):
    if wrongs == 1:
        t.speed(10)
        t.penup()
        t.back(200)
        t.left(90)
        t.back(250)
        t.right(90)
        t.pendown()

        t.begin_fill()
        t.forward(300)
        t.left(90)
        t.forward(30)
        t.left(90)
        t.forward(300)
        t.left(90)
        t.forward(30)
        t.end_fill()
        t.penup()
        t.back(30)
        t.left(90)
        t.forward(200)
        t.pendown()

        t.begin_fill()
        t.left(90)
        t.forward(500)
        t.right(90)
        t.forward(30)
        t.right(90)
        t.forward(500)
        t.end_fill()
        t.penup()
        t.back(500)
        t.left(90)
        t.pendown()

        t.begin_fill()
        t.forward(250)
        t.right(90)
        t.forward(30)
        t.right(90)
        t.forward(250)
        t.end_fill()
        t.penup()
        t.back(250)
        t.left(90)
        t.pendown()

        t.begin_fill()
        t.forward(60)
        t.right(90)
        t.forward(30)
        t.right(90)
        t.forward(60)
        t.end_fill()
    if wrongs == 2:
        t.penup()
        t.back(60)
        t.left(90)
        t.back(15)
        t.pendown()

        t.width(4)
        t.circle(40)
    if wrongs == 3:
        t.speed(3)
        t.penup()
        t.left(90)
        t.forward(80)
        t.pendown()

        t.width(7)
        t.forward(170)
    if wrongs == 4:
        t.penup()
        t.back(140)
        t.right(45)
        t.pendown()

        t.forward(100)
        t.penup()
        t.back(100)
        t.left(90)
        t.pendown()

        t.forward(100)
    if wrongs == 5:
        t.penup()
        t.back(100)
        t.right(45)
        t.forward(140)
        t.pendown()

        t.right(45)
        t.forward(120)
        t.penup()
        t.back(120)
        t.left(90)
        t.pendown()

        t.forward(120)
        t.width(3)
        t.penup()
        t.back(120)
        t.right(45)
        t.back(210)
        t.right(90)
        t.forward(15)
        t.right(45)
        t.pendown()

        t.forward(20)

        t.penup()
        t.right(45)
        t.back(15)
        t.pendown()

        t.right(45)
        t.forward(20)

        t.penup()
        t.back(20)
        t.right(45)
        t.forward(40)
        t.left(45)
        t.pendown()
        t.forward(20)

        t.penup()
        t.back(20)
        t.right(45)
        t.forward(15)
        t.left(135)
        t.pendown()
        t.forward(20)

        t.penup()
        t.forward(2000)

def word_update(letter, position):
    if len(position) == 1:
        txt = Label(root, text=letter, font="Ariel 24")
        txt.grid(row=4, column=position)
    if len(position) > 1:
        for pos in position:
            text = Label(root, text=letter, font="Ariel 24")
            text.grid(row=4, column=pos)

def wrongs_visual(wrong_letter):
    wrong_label = Label(root, text=wrong_letter, font="Ariel 20")
    wrong_label.grid(row=6, column=wrongs+4)


def guess(letter):
    global wrongs
    letter.lower() # turns user input to lowercase 
    user.delete(0,END)  # Clears the input box
    print(f"User guessed letter {letter}") # For debugging
    pos = []
    for i in range(len(word)):   #for every letter in the word
        if word[i] == letter: 
            pos.append(i)     #append position of guessed letter to list
    if len(pos) == 0:
        wrongs += 1   
        print(f"{wrongs} wrongs")   # for debugging
        update(wrongs)
        wrongs_visual(letter)
    print(pos)
    word_update(letter, pos) # to put letters on screen function


def visual(word):
    colum = 0  #setting a variable so that it can be changed with each Label positioning
    for i in word:
        print(i)   # For debugging
        if i == " ": # checks if there is a space in the words and displays a space to show separation
            x = Label(root, text=" ", font="Ariel 52")
            x.grid(row=4, column=colum, padx=5)
        else:                                                  # for every letter displays an underscore with incremented column positioning
            x = Label(root, text="_", font="Ariel 52")
            x.grid(row=4, column=colum, padx=5)
        colum += 1


def display(theme):             # Displaying Users choice of theme at top of main window
    theme_display = Label(root, text=f"Theme: {theme}", font="Ariel 28")
    theme_display.grid(row=0, column=0, columnspan=10)
    #theme_display.place(relx=0, rely=0, anchor="nw")  # Displays users choice of theme in the top left corner

Theme = ""
def theme_selection(x): 
    global Theme                # Procedure that sets Theme to the users choice
    if x == "f":
        Theme = Fruits
        theme_name = "Fruits"
    elif x == "c":
        Theme = Countries
        theme_name = "Countries"
    elif x == "a":
        Theme = Animals
        theme_name = "Animals"
    top.destroy()
    display(theme_name)
    main()

theme_label = Label(top, text="Pick a Theme", font="Impact 55")  # Pick a Theme Label and positioning
theme_label.grid(row=0, column=0, columnspan=3)

fruit_button = Button(top, text="Fruits", font="Ariel 32", command=lambda: theme_selection("f")) #Button for Fuits
fruit_button.grid(row=1, column=0, padx=15)

country_button = Button(top, text="Countries", font="Ariel 32", command=lambda: theme_selection("c"))  # Button for Country theme
country_button.grid(row=1, column=1, padx=15)

animal_button = Button(top, text="Animals", font="Ariel 32", command=lambda: theme_selection("a"))  # Button For animal theme
animal_button.grid(row=1, column=2, padx=15)



root.mainloop()