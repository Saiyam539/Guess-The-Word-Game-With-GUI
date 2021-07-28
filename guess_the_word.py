from tkinter import *
import random

window = Tk()
window.minsize(500,500)
window.maxsize(500,500)
window.title("Guess The Word Game")
window.config(bg="light blue")

word_list = ["programmer","computer","python","coding","keyboard","mouse","monitor","laptop"]
random_words = random.randint(1,len(word_list)-1)
print(word_list[random_words])

def main_function():
    global random_words
    word = user_guess.get()
    
    if word==word_list[random_words]:
        message.config(text="Your guess is correct!!!\nYou won the game\nThanks For Playing!",fg="green")
        
    
    elif word != word_list[random_words]:
        message.config(text="Your Guess is wrong!!\nTry Again",fg="red")
    
    else:
        message.config(text="Please enter a valid input.")

heading = Label(window,text="Guess The Word Game",font=("bold",40),bg="light green")
heading.pack(fill=X)

label_1 = Label(window,text="Computer has taken a random word.\nGuess that word.",font=("bold",30),bg="light blue")
label_1.pack()

label_2 = Label(window,text="Enter your Guess here:- ",font=("bold",25),bg="light blue")
label_2.place(x=10,y=150)

user_guess = Entry(window,font=("bold",25),width=9,bg="light green")
user_guess.place(x=300,y=150)

enter_button = Button(window,text="Enter",font=("bold",25),bg="light green",command=lambda:main_function())
enter_button.place(x=200,y=210)

message = Message(window,font=("bold",30),width=500,bg="light blue")
message.place(x=85,y=290)

window.mainloop()