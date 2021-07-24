import random
from flask import Flask

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1 style="color:red"> This is a number guessing game to start playing add &divide; in browser url bar and then enter your desired number</h1>' \
           '<img src="https://media.giphy.com/media/L40sNfcoJs5Op5afQU/giphy.gif" alt="game-gif">'


@app.route('/<number>')
def user_input(number):
    if int(number) < random_number:
        return '<h1 style="color:red"> sorry the number is low Try again </h1>' \
               '<img src ="https://media.giphy.com/media/BEob5qwFkSJ7G/giphy.gif" alt="sad">'
    elif int(number) > random_number:
        return '<h1 style="color:purple">Sorry the number is high try again </h1>' \
               '<img src = "https://media.giphy.com/media/ULKnZ7hW07rlS/giphy.gif" alt="sad-img">'
    elif int(number) == random_number:
        return '<h1 style = "color:green"> Congratulations you have guessed it correctly</h1>' \
               '<img src = "https://media.giphy.com/media/xT0xezQGU5xCDJuCPe/giphy.gif" alt="congratulations">'


if __name__ == "__main__":
    app.run(debug=True)
