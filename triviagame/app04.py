from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
import random
import html
import requests
import pdb

app = Flask(__name__)

def build_url(amount, category, difficulty, q_type):
    return f"https://opentdb.com/api.php?amount={amount}&category={category}&difficulty={difficulty}&type={q_type}"

@app.route('/', methods=['GET', 'POST'])
def index():

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

    questions = []
    correct_answers = {}

    if request.method == 'POST':
        amount = request.form['amount']
        category = request.form['category']
        difficulty = request.form['difficulty']
        q_type = request.form['q_type']

        url = build_url(amount, category, difficulty, q_type)
        data = requests.get(url).json()

        if 'results' in data:
            results = data['results']

            for index, question_data in enumerate(results):
                question = html.unescape(question_data['question'])
                correct_answer = html.unescape(question_data['correct_answer'])
                incorrect_answers = [html.unescape(answer) for answer in question_data['incorrect_answers']]
                all_answers = [correct_answer] + incorrect_answers
                random.shuffle(all_answers)
                
                questions.append({
                    'index': index,
                    'question': question,
                    'answers': all_answers,
                })

                correct_answers[index] = correct_answer
            
            print(f"Questions: {questions}")
            print(f"Correct Answers: {correct_answers}")
        
        return render_template('index04.html', questions=questions, categories=categories, correct_answers=correct_answers)

    return render_template('index04.html', categories=categories, correct_answers={})
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=2224)

