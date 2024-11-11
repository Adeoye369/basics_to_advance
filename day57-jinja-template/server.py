from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index_def():
    val = random.randint(1, 33)
    return render_template("index.html", val = val)

if __name__ == "__main__" :
    app.run(debug=True)
