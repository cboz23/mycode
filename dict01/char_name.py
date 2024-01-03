def main():
    
    marvelchars = {
        "Starlord": {"real name": "peter quill", "powers": "dance moves", "archenemy": "Thanos"},
        "Mystique": {"real name": "raven darkholme", "powers": "shape shifter", "archenemy": "Professor X"},
        "Hulk": {"real name": "bruce banner", "powers": "super strength", "archenemy": "adrenaline"},
        "Spidey": {"real name": "peter parker", "powers": "spider powers", "archenemy": "Green Goblin"}
        }

    char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk, or Spidey): ").capitalize()

    char_stat = input("What statistic do you want to know about? (real name, powers, archenemy): ").lower()

    value = marvelchars[char_name][char_stat]

    print(f"{char_name}'s {char_stat} is: {value.capitalize()}")

if __name__ == "__main__":
    main()

