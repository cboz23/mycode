def main():
    # Predefined Zelda characters
    link = "Link"
    zelda = "Princess Zelda"
    ganon = "Ganon"
    sheik = "Sheik"

    # Get user's favorite Zelda character
    user_choice = input("Who is your favorite Legend of Zelda character? (Link, Princess Zelda, Ganon): ")

    # Check user's choice and respond accordingly
    if user_choice.lower() == link.lower():
        print("Great choice! Link is the hero of Hyrule, great at finding Koroks, and represents courage! Ya-ha-ha!")
    elif user_choice.lower() == zelda.lower():
        print("Princess Zelda is a key figure in the Legend of Zelda series, stoic in her duties, and represents Wisdom.")
    elif user_choice.lower() == ganon.lower():
        print("Ganon is the primary antagonist, a formidable foe, and represents Power.")
    elif user_choice.lower() == sheik.lower():
        print("You know that Sheik is just Zelda in disguise right?")
    else:
        print("Not sure about that character. Choose from Link, Princess Zelda, or Ganon.")

if __name__ == "__main__":
    main()
