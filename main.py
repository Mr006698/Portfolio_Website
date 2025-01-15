from flask import Flask, render_template
from datetime import date

app = Flask(__name__)
@app.route('/')
def index() -> str:
    return render_template('index.html', year=date.today().strftime('%Y'))


@app.route('/cv')
def cv() -> str:
    return render_template('cv.html', year=date.today().strftime('%Y'))


@app.route('/projects')
def projects() -> str:
    #return render_template('projects.html')
    pass


if __name__ == '__main__':
    app.run(debug=True)
