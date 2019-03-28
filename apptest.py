from flask import Flask, render_template


from wms.forms.test import LoginForm

app = Flask(__name__)
app.secret_key='secret'

@app.route('/')
def index():
    form = LoginForm
    return render_template('login.html',form = form)