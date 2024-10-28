from flask import Flask

def make_h1(func):
    def wpfun(*args, **kw):
        return f"<h1> {func(*args)} </h1>"
    return wpfun

def make_bold_italic(func):
    def wpfunc(*args, **kw):
        return f"<i><b>{func(*args)}</b></i>"
    return wpfunc

app = Flask(__name__)

@app.route('/')
@make_h1
# @make_bold_italic
def hello_world():
    return "<p> Hello Flask</p>"

@app.route('/user/<username>')
@make_bold_italic
def user_page(username):
    return f"<h2> This User is {username} </h2>"

@app.route('/user/<name>/<float:price>')
def cost_page(name, price):
    return f"""
<ul>
    <li> {name} : <span>{price}</span></li>
    <li> {name} : <span>{price*2}</span></li>
<ul>
"""

if __name__ == "__main__":
    app.run(debug=True)