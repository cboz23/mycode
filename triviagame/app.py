from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
import random
import html
import requests

app = Flask(__name__)

categories = {
    9: "General Knowledge",
    10: "Entertainment- Books",
    11: "Entertainment- Film",
    12: "Entertainment- Music",
    13: "Entertainment- Musicals & Theater",
    14: "Entertainment- Television",
    15: "Entertainment- Video Games",
    16: "Entertainment- Board Games",
    17: "Science- Nature",
    18: "Science- Computers",
    19: "Science- Mathematics",
    20: "Mythology",
    21: "Sports",
    22: "Geography",
    23: "History",
    24: "Politics",
    25: "Art",
    26: "Celebrities",
    27: "Animals",
    28: "Vehicles",
    29: "Entertainment- Comics",
    30: "Science- Gadgets",
    31: "Entertainment- Japanese Anime & Manga",
    32: "Entertainment- Cartoon Animations"
}

def build_url(amount, category, difficulty, q_type):
    return f"https://opentdb.com/api.php?amount={amount}&category={category}&difficulty={difficulty}&type={q_type}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        amount = request.form['amount']
        category = request.form['category']
        difficulty = request.form['difficulty']
        q_type = request.form['q_type']

        url = build_url(amount, category, difficulty, q_type)

        data = requests.get(url).json()

        if 'results' in data:
            results = data['results']
            questions = []

            for question_data in results:
                question = html.unescape(question_data['question'])
                all_answers = [html.unescape(answer) for answer in question_data['incorrect_answers']]
                correct_answer = html.unescape(question_data['correct_answer'])
                all_answers.append(correct_answer)
                random.shuffle(all_answers)

                questions.append({
                    'question': question,
                    'answers': all_answers,
                    'correct_answer': correct_answer
                })

            return render_template('index.html', questions=questions, categories=categories)

    return render_template('index.html', categories=categories)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=2224)
