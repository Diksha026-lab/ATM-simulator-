import tkinter as tk
from tkinter import simpledialog, messagebox
from ttkthemes import ThemedTk
import tkinter.ttk as ttk

class ATM_GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("ATM Simulator")
        self.master.geometry("500x400")

        self.balance = 0

        # Create a style
        self.style = ttk.Style()
        self.style.configure('TButton', background='lightblue', foreground='black', font=('Helvetica', 12))
        self.style.configure('TLabel', background='lightblue', foreground='black', font=('Helvetica', 12))
        self.style.configure('TFrame', background='lightgray')

        # Title Label
        self.title_label = ttk.Label(self.master, text="ATM Simulator", font=("Helvetica", 20, "bold"), style='TLabel')
        self.title_label.pack(pady=20, fill=tk.X)

        # Frame for Buttons
        self.button_frame = ttk.Frame(self.master, style='TFrame')
        self.button_frame.pack(pady=10, fill=tk.X)

        # Buttons
        self.check_balance_button = ttk.Button(self.button_frame, text="Check Balance", command=self.check_balance, style='TButton')
        self.check_balance_button.grid(row=0, column=0, padx=10, pady=10)

        self.deposit_button = ttk.Button(self.button_frame, text="Deposit", command=self.deposit, style='TButton')
        self.deposit_button.grid(row=0, column=1, padx=10, pady=10)

        self.withdraw_button = ttk.Button(self.button_frame, text="Withdraw", command=self.withdraw, style='TButton')
        self.withdraw_button.grid(row=0, column=2, padx=10, pady=10)

        self.transfer_button = ttk.Button(self.button_frame, text="Transfer", command=self.transfer, style='TButton')
        self.transfer_button.grid(row=0, column=3, padx=10, pady=10)

        # Status Label
        self.status_label = ttk.Label(self.master, text="", style='TLabel')
        self.status_label.pack(pady=10, fill=tk.X)

        # History Text Area
        self.history_text = tk.Text(self.master, height=10, width=60, bg='white', fg='black')
        self.history_text.pack(pady=10)
        self.history_text.config(state=tk.DISABLED)

        self.transactions = []

    def log_transaction(self, action, amount):
        self.transactions.append(f"{action}: ₹{amount:.2f}")
        self.update_history()

    def update_history(self):
        self.history_text.config(state=tk.NORMAL)
        self.history_text.delete(1.0, tk.END)
        for transaction in self.transactions:
            self.history_text.insert(tk.END, transaction + "\n")
        self.history_text.config(state=tk.DISABLED)

    def check_balance(self):
        messagebox.showinfo("Balance", f"Your balance is: ₹{self.balance:.2f}")

    def deposit(self):
        amount = simpledialog.askfloat("Deposit", "Enter amount to deposit:")
        if amount is not None and amount > 0:
            self.balance += amount
            self.log_transaction("Deposited", amount)
            messagebox.showinfo("Success", f"Deposited ₹{amount:.2f}")
        else:
            messagebox.showerror("Error", "Invalid amount")

    def withdraw(self):
        amount = simpledialog.askfloat("Withdraw", "Enter amount to withdraw:")
        if amount is not None and amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                self.log_transaction("Withdrew", amount)
                messagebox.showinfo("Success", f"Withdrew ₹{amount:.2f}")
            else:
                messagebox.showerror("Error", "Insufficient funds")
        else:
            messagebox.showerror("Error", "Invalid amount")

    def transfer(self):
        amount = simpledialog.askfloat("Transfer", "Enter amount to transfer:")
        if amount is not None and amount > 0:
            if amount <= self.balance:
                recipient = simpledialog.askstring("Transfer", "Enter recipient's name:")
                if recipient:
                    self.balance -= amount
                    self.log_transaction("Transferred", amount)
                    messagebox.showinfo("Success", f"Transferred ₹{amount:.2f} to {recipient}")
                else:
                    messagebox.showerror("Error", "Recipient's name is required")
            else:
                messagebox.showerror("Error", "Insufficient funds")
        else:
            messagebox.showerror("Error", "Invalid amount")



def main():
    root = ThemedTk(theme="arc")  # You can choose other themes if you prefer
    atm_app = ATM_GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()