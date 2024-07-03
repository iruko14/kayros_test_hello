from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return redirect("/redi")

@app.route("/redi")
def hello_world():
    return "<p>Redirection from \
                page completed.!</p>"

if __name__ == "__main__":
    app.run(debug=True)