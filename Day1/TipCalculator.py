import tkinter as tk 

import tkinter as tk

class TipCalculator:
    def __init__(self, bill_amount, tip_percentage):
        self.bill_amount = bill_amount
        self.tip_percentage = tip_percentage

    def calculate_tip(self):
        return self.bill_amount * (self.tip_percentage / 100)

    def calculate_total(self):
        return self.bill_amount + self.calculate_tip()



class TipCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tip Calculator")

        # Bill Amount
        self.bill_amount_label = tk.Label(root, text="Bill Amount:")
        self.bill_amount_label.pack()
        self.bill_amount_entry = tk.Entry(root)
        self.bill_amount_entry.pack()

        # Tip Percentage
        self.tip_percentage_label = tk.Label(root, text="Tip Percentage:")
        self.tip_percentage_label.pack()
        self.tip_percentage_entry = tk.Entry(root)
        self.tip_percentage_entry.pack()

        # Calculate Button
        self.calculate_button = tk.Button(root, text="Calculate", command=lambda: self.calculate())
        self.calculate_button.pack()

        # Result
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def calculate(self):
        try:
            bill_amount = float(self.bill_amount_entry.get())
            tip_percentage = float(self.tip_percentage_entry.get())
            calculator = TipCalculator(bill_amount, tip_percentage)
            tip = calculator.calculate_tip()
            total = calculator.calculate_total()
            self.result_label.config(text=f"Tip: ${tip:.2f}\nTotal: ${total:.2f}")
        except ValueError:
            self.result_label.config(text="Please enter valid numbers")

if __name__ == "__main__":
    root = tk.Tk()
    app = TipCalculatorApp(root)
    root.mainloop()
