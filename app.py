from flask import Flask, jsonify, render_template
import random, json

app = Flask(__name__)

# Function to load a JSON file
def load_data(file_name):
    with open(f"data/{file_name}") as f:
        return json.load(f)

# Load databases into memory
databases = {
    "animalTrivia": load_data("animal_trivia.json"),
    "bibleSwordDrill": load_data("bible_sword_drill.json"),
    "bibleTrivia": load_data("bible_trivia.json"),
    "randomTrivia": load_data("random_trivia.json"),
    "fillInBlank": load_data("fill_in_blank.json"),
    "pictionary": load_data("pictionary.json")
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/getPrompt/<category>")
def get_prompt(category):
    if category in databases:
        return jsonify({"prompt": random.choice(databases[category])})
    return jsonify({"error": "Category not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
