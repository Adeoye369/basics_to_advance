from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/user')
def display_profile():
    return render_template('myprofile.html')

if __name__ == "__main__":
    app.run(debug=True)