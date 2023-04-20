import tkinter as tk

class TicTacToeGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.buttons = [[0 for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text='', font=('Arial', 20), width=5, height=2, command=lambda row=i, col=j: self.click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def click(self, row, col):
        # Handle user input when a button is clicked
        pass

    def run(self):
        self.root.mainloop()

gui = TicTacToeGUI()
gui.run()
