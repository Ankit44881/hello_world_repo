from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
    <html>
        <head>
            <style>
                body {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    font-size: 10vw; /* Responsive font size */
                }
            </style>
        </head>
        <body>
            <h1>Get well Soon Nikku beta!</h1>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
