from flask import Flask
import random

app = Flask(__name__)
# print(__name__)

random_num = random.randint(0, 9)
print(random_num)

@app.route('/')
def guess_number():
    return '<h1>Guess Number between 0 and 9</h1>'\
            '<img src='' width=200px />'


@app.route('/<int:number>')
def generate_random(number):
    if number > random_num:
        return "<h2 style='color:purple'>Too high, Try again!</h2>"\
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' />"
    elif number < random_num:
        return "<h2 style='color:red'>Too low, try again!</h2>"\
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' />"
    else:
        return "<h2 style='color:green'>You found me!</h2>"\
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' />"



if __name__ == '__main__':
    app.run(debug=True)