#!/usr/bin/env python3
import html

trivia = {
        "category": "Entertainment: Film",
        "type": "multiple",
        "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
        "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
        "incorrect_answers": [
            "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
            "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
            "&quot;Round up the usual suspects.&quot;"
        ]
    }

def main():
    question = html.unescape(trivia["question"])
    correct = html.unescape(trivia["correct_answer"])
    incorrect1 = html.unescape(trivia["incorrect_answers"][0])
    incorrect2 = html.unescape(trivia["incorrect_answers"][1])
    incorrect3 = html.unescape(trivia["incorrect_answers"][2])

    print(question)
    print("A) " + correct)
    print("B) " + incorrect1)
    print("C) " + incorrect2)
    print("D) " + incorrect3)
    user_answer = input("Enter the letter corresponding to your answer: ").upper()

    if user_answer == "A":
        print("Correct! " + correct)
    else:
        print("Incorrect. The correct answer is A) " + correct)

if __name__ == "__main__":
    main()

