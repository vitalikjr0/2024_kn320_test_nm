from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Вітаємо на головній сторінці!</h1>'

@app.route('/help')
def help():
    return '<h1>Вам потрібна допомога?</h1>'

# Екзамен
@app.route('/info')
def info():
    return '<h1>Ура я зробив завдання на екзамен!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
