from flask import Flask, jsonify, render_template
import json
import os

app = Flask(__name__, static_folder='static', template_folder='templates', static_url_path="/")

config = {}

with open('config.json', 'r') as file:
    config = json.load(file)


@app.route("/ping")
def heartbeat():
    return jsonify({"status": "Pong!"})


@app.route('/')
def index():
    return render_template('index.jinja', sections=config['shortcuts'])

if __name__ == "__main__":
    app.run(debug=os.getenv("FLASK_DEBUG", "False") == "True")