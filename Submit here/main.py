import turtle

# ===== Screen setting =====
screen = turtle.Screen()
screen.setup(700, 700)
screen.title("Gallow in turtle")
screen.bgcolor("white")
screen.tracer(0)          

pen = turtle.Turtle()
pen.hideturtle()
pen.pensize(3)
pen.speed(0)

# ===== Gallow (drawing before the game) =====
pen.penup()
pen.goto(-100, -100)
pen.pendown()
pen.goto(100, -100)       # earth
pen.penup()
pen.goto(0, -100)
pen.pendown()
pen.goto(0, 150)          # post
pen.goto(80, 150)         # crossbar
pen.goto(80, 120)         # rope

# ===== text panel =====
info = turtle.Turtle()
info.hideturtle()
info.penup()




# ===== Game settings =====
word = "rabbit"   # task #1: insert your own word (any word you want)
guessed = ""
wrong = 0
won = False
attemptLimit = len(set(word)) + 6
myAttempt = 0
sameLetter = False
letterEmpty = False

for attempt in range(attemptLimit+1):     # task #2: how many attempts should be?🤔
    
    # --- 1. showing word or mistakes number ---
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    info.clear()
    if(sameLetter):
        info.goto(-300, -305)
        info.write("You've already entered this letter!", font=("Arial", 12, "italic"))
    if(letterEmpty):
            info.goto(-300, -305)
            info.write("Your Input must not be empty!", font=("Arial", 12, "italic"))
    info.goto(-300, -200)
    info.write("Word: " + display, font=("Arial", 18, "normal"))
    info.goto(-300, -235)
    info.write("Mistakes: " + str(wrong) + " / 6", font=("Arial", 14, "normal"))
    info.goto(-300, -270)
    info.write("Your Attempt: " + str(myAttempt) + " / " + str(attemptLimit), font=("Arial", 14, "normal"))
    screen.update()        # ← showing all before the second word enter
    if won:
        break
    if(wrong >= 6 or myAttempt > attemptLimit):
        won = False
        break
    # --- 2. word enter ---
    letter = screen.textinput("Gallow", "Your letter:")
    letterEmpty = False
    if letter == "":
        letter = ""
        letterEmpty = True
    letter = letter.strip().lower()
    myAttempt+=1
    # --- 3. checking ---
    if (letter in guessed and letter != ""):
        sameLetter = True
        
    elif letter in word:
        sameLetter = False
        guessed += letter
    else:
        sameLetter = False
        wrong += 1
        guessed+=letter
        # drawing new part of body
        pen.penup()
        if wrong == 1:                    # head
            pen.goto(80, 80)
            pen.pendown()
            pen.circle(20)
        elif wrong == 2:                  # body
            pen.goto(80, 80)
            pen.pendown()
            pen.goto(80, 40)
        elif wrong == 3:                  # left hand
            pen.goto(80, 70)
            pen.pendown()
            pen.goto(60, 50)
        elif wrong == 4:                  # task #3: I suddenly forgot how to draw right hand, will you help?
            pen.goto(80, 70)
            pen.pendown()
            pen.goto(100, 50)
            
        elif wrong == 5:                  # left leg
            pen.goto(80, 40)
            pen.pendown()
            pen.goto(60, 10)
        elif wrong == 6:                  # right leg
            pen.goto(80, 40)
            pen.pendown()
            pen.goto(100, 10)

    

    # --- 4. checking the win ---
    win = True
    for letter in word:
        if letter not in guessed:
            win = False
    if win:
        won = True

# ===== Final =====
info.goto(-300, -335)
if won:
    info.write("Winner winner chicken dinner! Word is: " + word, font=("Arial", 18, "bold"))
else:
    info.write("You lose. Word was: " + word, font=("Arial", 18, "bold"))

screen.update()
turtle.done()