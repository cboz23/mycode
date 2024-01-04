def ask_question(question, options):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    user_answer = input("Enter the number corresponding to your choice: ")
    return int(user_answer) - 1  # Adjusting to 0-based index

def sort_into_house():
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    points = [0, 0, 0, 0]

    # Questions
    questions = [
        "What trait do you value most?",
        "Which animal speaks to you?",
        "Choose a magical artifact:",
        "What's your favorite type of magic?",
    ]

    options = [
        ["Courage", "Kindness", "Wisdom", "Ambition"],
        ["Lion", "Badger", "Eagle", "Snake"],
        ["Sword of Gryffindor", "Hufflepuff Cup", "Ravenclaw Diadem", "Slytherin Locket"],
        ["Transfiguration", "Herbology", "Charms", "Potions"],
    ]

    # Ask questions and assign points
    for i in range(len(questions)):
        answer_index = ask_question(questions[i], options[i])
        points[answer_index] += 1

    # Determine the house with the highest points
    max_points_index = points.index(max(points))
    sorted_house = houses[max_points_index]

    print("\nCongratulations! You belong to", sorted_house)

if __name__ == "__main__":
    sort_into_house()
