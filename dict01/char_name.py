def main():
    marvelchars = {
        "Starlord": {"real name": "peter quill", "powers": "dance moves", "archenemy": "Thanos"},
        "Mystique": {"real name": "raven darkholme", "powers": "shape shifter", "archenemy": "Professor X"},
        "Hulk": {"real name": "bruce banner", "powers": "super strength", "archenemy": "adrenaline"},
        "Spidey": {"real name": "peter parker", "powers": "spider powers", "archenemy": "Green Goblin"}
    }

    # Get user input for the character name
    char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk, or Spidey): ").capitalize()

    # Check if the entered character name is valid
    if char_name not in marvelchars:
        print("Invalid character name. Please choose Starlord, Mystique, Hulk, or Spidey.")
        return

    # Get user input for the character statistic
    char_stat = input("What statistic do you want to know about? (real name, powers, archenemy): ").lower()

    # Check if the entered character statistic is valid
    if char_stat not in marvelchars[char_name]:
        print("Invalid character statistic. Please choose real name, powers, or archenemy.")
        return

    # Retrieve the value from the dictionary using the user inputs
    value = marvelchars[char_name][char_stat]

    # Print the combined information
    print(f"{char_name}'s {char_stat} is: {value.capitalize()}")

if __name__ == "__main__":
    main()
