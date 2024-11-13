from flask import Flask, render_template
import random, requests, json, datetime as dt


app = Flask(__name__)

@app.route('/')
def index_page():
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
        # result = json.loads(res.text)
        result = res.json()
        age = result['age']

        # Gender data from genderize
        res = requests.get(f"https://api.genderize.io?name={name}")
        # result = json.loads(res.text)
        result = res.json()
        gender = result["gender"]
        prob = round(result["probability"]*100)
        
    except KeyError as e:
        print(e)
        print(result)


    return render_template("guess.html", name = name.title(), age=age, gender = gender, prob = prob, result= result)

@app.route('/blog')
def blog_page():
    res = requests.get('https://api.npoint.io/f83d799baae8f8930123')
    post_data = res.json()
    print(post_data)

    return render_template('blog.html', blog_post = post_data)


player_list = [
    {'id': 0, 'name': 'Omotayo, Omolola', 'role':'Acher'},
    {'id': 1,'name': 'Demilade, Ayetigba', 'role':'Sprint'},
    {'id': 2,'name': 'Onyinye, Gbenga', 'role':'Warrior'},
    {'id': 3,'name': 'Kemi, Fastus', 'role':'Fronter'},
]

@app.route('/players')
def players_page():
    return render_template('players.html', players = player_list)

if __name__ == "__main__" :
    app.run(debug=True)
