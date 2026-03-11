from flask import Flask

app = Flask(__name__)  # __name__ -> "flask.py"

@app.route("/") # endpoint When user visits "/", this function will  automatically be called
def home():
    return "This is the Home Page"

@app.route("/about")
def about():
    return "This is page about us"

if __name__ == "__main__":
    app.run(debug=True) # debug=True -> auto reload the server when code changes