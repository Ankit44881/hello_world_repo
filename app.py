from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1 style="font-size: 48px;">Get well Soon Nikku!</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
