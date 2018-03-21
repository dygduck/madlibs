"""A madlib game that compliments its users."""

from random import choice, sample, randint

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]

MADLIB_FILES = ["madlib.html", "madlib2.html", "madlib3.html"]

@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")
    n = randint(1, 14)
    compliments = sample(AWESOMENESS, n)

    return render_template("compliment.html",
                           person=player,
                           compliments=compliments,
                           number=n)

@app.route('/game')
def show_madlib_form():
    answer = request.args.get("yesno")
    if answer == "yes":
        return render_template("game.html")

    else:
        return render_template("goodbye.html")


@app.route('/madlib', methods=["POST", "GET"])
def show_madlib():

    if method == "POST":
        input_dict = request.form
    else: 
        input_dict = request.args

    name = input_dict.get("person")
    color = input_dict.get("color")
    noun = input_dict.get("noun")
    adjective = input_dict.get("adjective")
    superheroes = input_dict.get("superhero")


    return render_template(choice(MADLIB_FILES), color=color, noun=noun,
                           adjective=adjective, person=name,
                           superhero=superheroes)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
