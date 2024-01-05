import random

def suggest_food():
    # Food options for date night
    food_choices = [
        "Italian (Pasta, Pizza)",
        "Japanese (Sushi, Ramen, Hibachi)",
        "Mexican (Tacos, Burritos)",
        "Mediterranean (Hummus, Kebabs, Shawarmas)",
        "Thai (Pad Thai, Curry)",
        "Indian (Curry, Biriyani, Tandori)",
        "Steakhouse",
        "Vietnamese (Pho, Bahn Mi, Com Ga)",
        "Seafood (Crab, Shrimp, Lobster, Fish)",
        "Pizza",
        "Chicken (Wings, Fried Chicken, Chicken Sandwiches)",
        "Vegetarian/Vegan",
        "Food from your favorite local restaurant",
    ]

    # Ask the user to select five choices
    print("Choose five food options for your date night (enter numbers 1-13):")
    for i, choice in enumerate(food_choices, start=1):
        print(f"{i}. {choice}")

    user_selection = set()
    while len(user_selection) < 5:
        try:
            choice_number = int(input("Enter the number of your choice: "))
            if 1 <= choice_number <= len(food_choices):
                user_selection.add(food_choices[choice_number - 1])
            else:
                print("Invalid choice. Please enter a number between 1 and 13.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    if len(user_selection) != 5:
        print("You must select exactly five options. Exiting.")
        return

    # Randomly select three choices from the user's selection
    random_choices = random.sample(list(user_selection), k=3)

    # Ask the user to choose two from the three random choices
    print("\nYou selected these five options:")
    for i, choice in enumerate(user_selection, start=1):
        print(f"{i}. {choice}")

    print("\nNow, choose two from the following three options:")
    for i, choice in enumerate(random_choices, start=1):
        print(f"{i}. {choice}")

    user_final_choices = set()
    while len(user_final_choices) < 2:
        try:
            choice_number = int(input("Enter the number of your final choices: "))
            if 1 <= choice_number <= 3:
                user_final_choices.add(random_choices[choice_number - 1])
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    if len(user_final_choices) == 2:
        final_choice = user_final_choices.pop()
        print(f"\nDinner has been decided! Enjoy some {final_choice} cuisine! If you're disappointed in the selection, then it seems you know what you really want!")
    else:
        print("You must select exactly two options. Exiting.")

if __name__ == "__main__":
    suggest_food()
