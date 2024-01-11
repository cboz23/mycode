import html
import requests

# Dictionary mapping category numbers to names
categories = {
    9:  "General Knowledge", 
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

def build_url():
    # Take user input for building the URL
    amount = input("Enter the number of questions you want: ")
    category = input("Choose a category number:\n" + "\n".join(f"{num}: {name}" for num, name in categories.items()) + "\n")
    difficulty = input("Choose difficulty (easy, medium, hard): ")
    q_type = input("Choose question type (multiple, boolean): ")

    # Build the URL with user input
    url = f"https://opentdb.com/api.php?amount={amount}&category={category}&difficulty={difficulty}&type={q_type}"
    return url

def main():
    # Build the URL based on user input
    url = build_url()

    # Fetch data from the API
    data = requests.get(url).json()

    # Check if the 'results' key exists in the data
    if 'results' in data:
        results = data['results']

        # Iterate through each result
        for index, question_data in enumerate(results, start=1):
            question = question_data['question']
            # Unescape HTML entities in the question
            question = html.unescape(question)

            print(f"\nQuestion {index}: {question}")

            # Combine correct and incorrect answers for user prompt
            all_answers = [html.unescape(answer) for answer in question_data['incorrect_answers']]
            correct_answer = html.unescape(question_data['correct_answer'])
            all_answers.append(correct_answer)

            # Shuffle the answers to avoid bias
            import random
            random.shuffle(all_answers)

            # Print the shuffled answers for user input
            for i, answer in enumerate(all_answers, start=1):
                print(f"  {i}. {answer}")

            # Prompt the user for input
            user_input = input("Enter the number of your answer: ")

            # Check if the user's answer is correct
            if user_input.isdigit() and 1 <= int(user_input) <= len(all_answers):
                user_answer = all_answers[int(user_input) - 1]
                if user_answer == correct_answer:
                    print("Correct!")
                else:
                    print(f"Wrong! The correct answer is: {correct_answer}")
            else:
                print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
