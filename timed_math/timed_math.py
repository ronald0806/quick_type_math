import tkinter as tk
from tkinter import simpledialog, messagebox
import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 25
TOTAL_PROBLEMS = 20

class TimedMathGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quick Type Math")

        self.label = tk.Label(root, text=" Think you're quick enough to solve math? Click *Start* to begin typing!")
        self.label.pack(pady=10)

        self.start_button = tk.Button(root, text="Start", command=self.start_game)
        self.start_button.pack(pady=10)

        self.time_label = tk.Label(root, text="")
        self.time_label.pack(pady=10)

    def generate_problem(self):
        left = random.randint(MIN_OPERAND, MAX_OPERAND)
        right = random.randint(MIN_OPERAND, MAX_OPERAND)
        operator = random.choice(OPERATORS)

        expr = str(left) + " " + operator + " " + str(right)
        answer = eval(expr)
        return expr, answer

    def show_result(self, total_time, wrong):
        result_str = f"Good job! You finished in {total_time} seconds. You got {wrong} wrong answers."
        messagebox.showinfo("Game Over", result_str)
        self.label.config(text="Press *Start* to play again!")

    def start_game(self):
        self.start_button.config(state=tk.DISABLED)
        self.label.config(text="---------")

        start_time = time.time()
        wrong = 0

        for i in range(TOTAL_PROBLEMS):
            expr, answer = self.generate_problem()
            while True:
                guess = simpledialog.askstring("Math Problem", f"Problem #{i + 1}: {expr} = ")
                if guess == str(answer):
                    break
                wrong += 1

        end_time = time.time()
        total_time = round(end_time - start_time, 2)

        self.label.config(text="---------")
        self.show_result(total_time, wrong)
        self.start_button.config(state=tk.NORMAL)


if __name__ == "__main__":
    root = tk.Tk()
    app = TimedMathGame(root)
    root.mainloop()
