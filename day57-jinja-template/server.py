from flask import Flask, render_template
import random, requests, json, datetime as dt


app = Flask(__name__)

@app.route('/')
def index_def():
    val = random.randint(1, 33)
    current_year = dt.datetime.now().year
    return render_template("index.html", val = val, year= current_year)


@app.route('/guess/<name>')
def guess_page(name):

    result = ""
    gender = age = prob = None
    try :
        # Age data from agify
        res = requests.get(f"https://api.agify.io?name={name}")
        result = json.loads(res.text)
        age = result['age']

        # Gender data from genderize
        res = requests.get(f"https://api.genderize.io?name={name}")
        result = json.loads(res.text)
        gender = result["gender"]
        prob = round(result["probability"]*100)
        
    except KeyError as e:
        print(e)
        print(result)


    return render_template("guess.html", name = name.title(), age=age, gender = gender, prob = prob, result= result)


if __name__ == "__main__" :
    app.run(debug=True)
