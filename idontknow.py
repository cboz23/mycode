import random

def suggest_food():
    # Food options for date night
    food_choices = [
        "Italian (Pasta, Pizza)",
        "Japanese (Sushi, Ramen)",
        "Mexican (Tacos, Burritos)",
        "Mediterranean (Hummus, Kebabs, Shawarmas)",
        "Thai (Pad Thai, Curry)",
        "Indian",
        "Steakhouse",
        "Seafood",
        "Pizza",
        "Vegetarian/Vegan",
        "Food from your favorite local restaurant",
    ]

    # Ask the user to select three choices
    print("Choose three food options for your date night (enter numbers 1-11):")
    for i, choice in enumerate(food_choices, start=1):
        print(f"{i}. {choice}")

    user_selection = set()
    while len(user_selection) < 3:
        try:
            choice_number = int(input("Enter the number of your choice: "))
            if 1 <= choice_number <= len(food_choices):
                user_selection.add(food_choices[choice_number - 1])
            else:
                print("Invalid choice. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Randomly select two choices from the user's selection
    random_choices = random.sample(user_selection, k=2)

    # Ask the user to choose one from the two random choices
    print("\nYou selected these three options:")
    for i, choice in enumerate(user_selection, start=1):
        print(f"{i}. {choice}")

    print("\nNow, choose one from the following two options:")
    for i, choice in enumerate(random_choices, start=1):
        print(f"{i}. {choice}")

    user_final_choice = int(input("Enter the number of your final choice: "))
    if 1 <= user_final_choice <= 2:
        print(f"\nGreat choice! Enjoy your {random_choices[user_final_choice - 1]} cuisine on your date night.")
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    suggest_food()

