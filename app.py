from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home Page')

@app.route('/about')
def about():
    return render_template('about.html', title='About Page', data='about')

if __name__ == '__main__':
    app.run(debug=True)