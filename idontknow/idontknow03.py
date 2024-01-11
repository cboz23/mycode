import tkinter as tk
from tkinter import messagebox
import random
import time
import sys

def loading_spinner(label):
    spinner = "|/-\\"
    for _ in range(10):
        for char in spinner:
            label.config(text=char)
            label.update_idletasks()
            time.sleep(0.1)

def read_food_choices(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def suggest_food():
    # Read food choices from the file
    food_choices = read_food_choices('food_choices.txt')

    # Create a tkinter window
    window = tk.Tk()
    window.title("Food Suggestion App")

    # Create a label for the spinner
    spinner_label = tk.Label(window, text="")
    spinner_label.pack()

    # Run the loading spinner in a separate thread
    loading_thread = threading.Thread(target=loading_spinner, args=(spinner_label,))
    loading_thread.start()

    # Ask the user to select five choices
    messagebox.showinfo("Food Choices", "Choose five food options for your date night (enter numbers 1-{}):".format(len(food_choices)))
    for i, choice in enumerate(food_choices, start=1):
        messagebox.showinfo("Food Choices", f"{i}. {choice}")

    user_selection = set()
    while len(user_selection) < 5:
        try:
            choice_number = int(messagebox.askstring("Food Selection", "Enter the number of your choice: "))
            if 1 <= choice_number <= len(food_choices):
                user_selection.add(food_choices[choice_number - 1])
            else:
                messagebox.showerror("Invalid Choice", "Invalid choice. Please enter a number between 1 and {}.".format(len(food_choices)))
        except ValueError:
            messagebox.showerror("Invalid Input", "Invalid input. Please enter a number.")

    # Stop the loading spinner thread
    loading_thread.join()

    # Display the final food choices
    messagebox.showinfo("Final Choices", f"Your final choices: {', '.join(user_selection)}")

if __name__ == "__main__":
    suggest_food()

