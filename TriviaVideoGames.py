#!/usr/bin/env python3
import html

VG1trivia = {
        "type":"multiple",
        "difficulty":"easy",
        "category":"Entertainment: Video Games",
        "question":"League of Legends, DOTA 2, Smite and Heroes of the Storm are all part of which game genre?",
        "correct_answer":"Multiplayer Online Battle Arena (MOBA)",
        "incorrect_answers": [
             "Real Time Strategy (RTS)",
             "First Person Shooter (FPS)",
             "Role Playing Game (RPG)"
        ]
    },
VG2trivia = {
        "type":"boolean",
        "difficulty":"medium",
        "category":"Entertainment: Video Games",
        "question":"Pistons were added to Minecraft in Beta 1.5.",
        "correct_answer":"False",
        "incorrect_answers":[
             "True"
        ]
    },
VG3trivia = {
        "type":"multiple",
        "difficulty":"medium",
        "category":"Entertainment: Video Games",
        "question":"Which horror movie had a sequel in the form of a video game released in August 20, 2002?",
        "correct_answer":"The Thing",
        "incorrect_answers":[
            "The Evil Dead",
            "Saw",
            "Alien"
        ]
    },
VG4trivia = {
        "type":"multiple",
        "difficulty":"hard","category":"Entertainment: Books","question":"Which author co-wrote &quot;The Communist Manifesto&quot; alongside Karl Marx?","correct_answer":"Friedrich Engels","incorrect_answers":["Robert Owen","Alexander Kerensky","Paul Lafargue"]},{"type":"multiple","difficulty":"medium","category":"History","question":"The Herero genocide was perpetrated in Africa by which of the following colonial nations?","correct_answer":"Germany","incorrect_answers":["Britain","Belgium","France"]},{"type":"multiple","difficulty":"medium","category":"Entertainment: Video Games","question":"Which of the following Terran units from the RTS game Starcraft was first introduced in the expansion Brood War?","correct_answer":"Medic","incorrect_answers":["Wraith","Science Vessel","SCV"]},{"type":"multiple","difficulty":"medium","category":"Entertainment: Comics","question":"What is the designation given to the Marvel Cinematic Universe?","correct_answer":"Earth-199999","incorrect_answers":["Earth-616","Earth-10005","Earth-2008"]},{"type":"boolean","difficulty":"easy","category":"Mythology","question":"In Norse mythology, Thor once dressed as a woman.","correct_answer":"True","incorrect_answers":["False"]},{"type":"multiple","difficulty":"hard","category":"Politics","question":"Which letter do you need to have on a European driver license in order to ride any motorbikes?","correct_answer":"A","incorrect_answers":["X","D","B"]},{"type":"multiple","difficulty":"easy","category":"Entertainment: Video Games","question":"Which Kirby game first introduced Copy Abilities?","correct_answer":"Kirby&#039;s Adventure","incorrect_answers":["Kirby Super Star","Kirby&#039;s Dream Land 2","Kirby&#039;s Dream Land"]}]

trivia = {
        "category": "Entertainment: Video Games",
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
