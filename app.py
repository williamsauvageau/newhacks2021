from flask import Flask, render_template
import random
#import os
#os.system("python todo.py")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

motivationalmessages = ["The best time to plant a tree was 20 years ago. The second best time is now.",
                        "The secret of getting ahead is getting started.",
                        "We are what we repeatedly do. Excellence, then, is not an act, but a habit.",
                        "Keep your eyes on the stars, and your feet on the ground.",
                        "If you cannot do great things, do small things in a great way.",
                        "Nothing will work unless you do."]
choice = random.choice(motivationalmessages)

@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'

@app.route('/motivational')
def motivational():
    return render_template('motivational.html', choice=choice)

@app.route('/todo')
def todo():
    return render_template('todo.html')

#stuff = {
    #"Task": [],
    #"Date added": "2",
    #"Date needed by": "3",
    #"Importace": "4",
    #"Other comments": "5",
#}

#stuff ["Task"].append("Clean")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
