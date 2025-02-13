from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1>" \
            "<p>This is Paragraph</p>" \
            "<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExM29lajRvMzlvd2ZxcXN4MXhuZW1yYjJhZHEyNmUzdG1hY3M1NGY2ZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/YRVP7mapl24G6RNkwJ/giphy.gif' width=200 alt='kitten_image' />"

def make_bold(function):
    def wrapper():
        return '<b>' + function() + '</b>'
    return wrapper

def make_emphasis(function):
    def wrapper():
        return '<em>' + function() + '</em>'
    return wrapper

def make_underlined(function):
    def wrapper():
        return '<u>' + function() + '</u>'
    return wrapper


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return 'Bye!'

@app.route('/<name>/<int:number>')
def greet(name, number):
    return f'Hello there {name}, you are {number} years old.!'


if __name__ == '__main__':
    # run the app in debug mode to automate
    app.run(debug=True)