import tkinter as tk
from tkinter import messagebox
import random

class DateNightApp:
    def __init__(self, master):
        self.master = master
        master.title("Date Night Food Suggester")

        self.food_choices = [
            "Italian (Pasta, Pizza)",
            "Japanese (Sushi, Ramen, Hibachi)",
            "Mexican (Tacos, Burritos)",
            "Mediterranean (Hummus, Kebabs, Shawarmas)",
            "Thai (Pad Thai, Curry)",
            "Indian (Curry, Biriyani, Tandoori)",
            "Steakhouse",
            "Vietnamese (Pho, Bahn Mi, Com Ga)",
            "Seafood (Crab, Shrimp, Lobster, Fish)",
            "Pizza",
            "Chicken (Wings, Fried Chicken, Chicken Sandwiches)",
            "Vegetarian/Vegan",
            "Food from your favorite local restaurant",
        ]

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Choose five food options for your date night (enter numbers 1-13):")
        self.label.pack()

        self.choices_var = tk.StringVar(value="")
        for i, choice in enumerate(self.food_choices, start=1):
            tk.Radiobutton(self.master, text=choice, variable=self.choices_var, value=choice).pack()

        self.submit_button = tk.Button(self.master, text="Submit", command=self.submit_choices)
        self.submit_button.pack()

    def submit_choices(self):
        user_selection = self.choices_var.get().split()
        if len(user_selection) != 5:
            messagebox.showinfo("Error", "You must select exactly five options.")
            return

        random_choices = random.sample(user_selection, k=3)

        user_final_choices = self.select_final_choices(random_choices)
        if user_final_choices is not None:
            final_choice = user_final_choices.pop()
            messagebox.showinfo("Result", f"Dinner has been decided! Enjoy some {final_choice} cuisine!")
        else:
            messagebox.showinfo("Error", "You must select exactly two options.")

    def select_final_choices(self, random_choices):
        final_choices_var = tk.StringVar(value="")
        for i, choice in enumerate(random_choices, start=1):
            tk.Radiobutton(self.master, text=choice, variable=final_choices_var, value=choice).pack()

        submit_button = tk.Button(self.master, text="Submit", command=lambda: self.display_final_choice(final_choices_var))
        submit_button.pack()

        self.submit_button.config(state="disabled")
        self.label.config(text="Now, choose two from the following three options:")

        self.master.mainloop()
        return final_choices_var.get().split()

    def display_final_choice(self, final_choices_var):
        self.master.quit()
        final_choice = final_choices_var.get().split()
        if len(final_choice) == 2:
            messagebox.showinfo("Result", f"Dinner has been decided! Enjoy some {final_choice[0]} and {final_choice[1]} cuisine!")
        else:
            messagebox.showinfo("Error", "You must select exactly two options.")
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = DateNightApp(root)
    root.mainloop()

