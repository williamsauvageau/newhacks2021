from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'

motivationalmessages = ["Message 1", "Message 2", "Message 3", "Message 4"]
random.choice(motivationalmessages)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
