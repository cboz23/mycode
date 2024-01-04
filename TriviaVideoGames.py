#!/usr/bin/env python3
import html

trivia_questions = [
    {
        "type": "multiple",
        "difficulty": "easy",
        "category": "Entertainment: Video Games",
        "question": "League of Legends, DOTA 2, Smite and Heroes of the Storm are all part of which game genre?",
        "correct_answer": "Multiplayer Online Battle Arena (MOBA)",
        "incorrect_answers": [
            "Real Time Strategy (RTS)",
            "First Person Shooter (FPS)",
            "Role Playing Game (RPG)"
        ]
    },
    {
        "type": "boolean",
        "difficulty": "medium",
        "category": "Entertainment: Video Games",
        "question": "Pistons were added to Minecraft in Beta 1.5.",
        "correct_answer": "False",
        "incorrect_answers": [
            "True"
        ]
    },
    {
        "type": "multiple",
        "difficulty": "medium",
        "category": "Entertainment: Video Games",
        "question": "Which horror movie had a sequel in the form of a video game released in August 20, 2002?",
        "correct_answer": "The Thing",
        "incorrect_answers": [
            "The Evil Dead",
            "Saw",
            "Alien"
        ]
    },
    {
        "type":"multiple",
        "difficulty":"hard",
        "category":"Entertainment: Books",
        "question":"Which author co-wrote &quot;The Communist Manifesto&quot; alongside Karl Marx?","correct_answer":"Friedrich Engels",
        "incorrect_answers":[
            "Robert Owen",
            "Alexander Kerensky",
            "Paul Lafargue"
        ]
    },
    {
        "type":"multiple",
        "difficulty":"medium",
        "category":"History",
        "question":"The Herero genocide was perpetrated in Africa by which of the following colonial nations?",
        "correct_answer":"Germany",
        "incorrect_answers":[
            "Britain",
            "Belgium",
            "France"
        ]
    },
    {
        "type":"multiple",
        "difficulty":"medium",
        "category":"Entertainment: Video Games",
        "question":"Which of the following Terran units from the RTS game Starcraft was first introduced in the expansion Brood War?",
        "correct_answer":"Medic",
        "incorrect_answers":[
            "Wraith",
            "Science Vessel",
            "SCV"
        ]
    },
    {
        "type":"multiple",
        "difficulty":"medium",
        "category":"Entertainment: Comics",
        "question":"What is the designation given to the Marvel Cinematic Universe?",
        "correct_answer":"Earth-199999",
        "incorrect_answers":[
            "Earth-616",
            "Earth-10005",
            "Earth-2008"
        ]
    },
    {
        "type":"boolean",
        "difficulty":"easy",
        "category":"Mythology",
        "question":"In Norse mythology, Thor once dressed as a woman.",
        "correct_answer":"True",
        "incorrect_answers":[
            "False"
        ]
    },
    {
        "type":"multiple",
        "difficulty":"hard",
        "category":"Politics",
        "question":"Which letter do you need to have on a European driver license in order to ride any motorbikes?",
        "correct_answer":"A",
        "incorrect_answers":[
            "X",
            "D",
            "B"
        ]
    },
    {
        "type":"multiple",
        "difficulty":"easy",
        "category":"Entertainment: Video Games",
        "question":"Which Kirby game first introduced Copy Abilities?",
        "correct_answer":"Kirby&#039;s Adventure",
        "incorrect_answers":[
            "Kirby Super Star",
            "Kirby&#039;s Dream Land 2",
            "Kirby&#039;s Dream Land"
        ]
    },
    # Add more questions as needed
]

def display_question(question):
    question_text = html.unescape(question["question"])
    correct_answer = html.unescape(question["correct_answer"])
    incorrect_answers = [html.unescape(ans) for ans in question["incorrect_answers"]]

    print(question_text)

    options = {"A": correct_answer}
    options.update({chr(ord('A') + i): incorrect_answers[i] for i in range(len(incorrect_answers))})

    for option, answer in options.items():
        print(f"{option}) {answer}")

    user_answer = input("Enter the letter corresponding to your answer: ").upper()

    if user_answer in options and options[user_answer] == correct_answer:
        print("Correct! " + correct_answer)
    else:
        print(f"Incorrect. The correct answer is A) {correct_answer}")


def main():
    print("Welcome to the Trivia Game!")
    print("Press Ctrl+C to exit.")

    try:
        for question in trivia_questions:
            display_question(question)
            print("\n" + "=" * 30 + "\n")  # Add a separator between questions

    except KeyboardInterrupt:
        print("\nExiting Trivia Game.")

if __name__ == "__main__":
    main()
