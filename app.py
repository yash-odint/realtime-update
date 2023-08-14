from flask import Flask, render_template, jsonify
import time

app = Flask(__name__)

def get_time():
    return time.strftime("%H:%M:%S")

@app.route("/time")
def show_time():
    return jsonify(result = get_time())

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=9999)