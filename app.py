from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h2> Hello I am Binita</h2>"

if __name__ == '__main__':
    app.run(debug=True)