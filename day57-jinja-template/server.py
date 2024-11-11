from flask import Flask, render_template
import random, datetime as dt

app = Flask(__name__)

@app.route('/')
def index_def():
    val = random.randint(1, 33)
    current_year = dt.datetime.now().year
    return render_template("index.html", val = val, year= current_year)

if __name__ == "__main__" :
    app.run(debug=True)
