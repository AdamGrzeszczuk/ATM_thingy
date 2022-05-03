from tkinter import *
from tkinter import ttk

pic = "2.png"

class Atm:

    def __init__(self, master):
        global lbLogo
        self.balance = 0

        master.title("ATM Machine")
        master.configure(background="#FFB72B")
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        self.style = ttk.Style()
        self.style.configure("TButton", background="#B5FE83")#, padding=20)
        self.style.configure("TFrame", background="#008E89")
        self.style.configure("TEntry", padding=5)

        logo = PhotoImage(file=pic)
        self.logo = logo.subsample(2)
        lbLogo = ttk.Label(self.frame_header, image=self.logo)
        lbLogo.grid(row=0, column=0,columnspan=2, padx=10, pady=10)
        lbThanks = ttk.Label(self.frame_header, text="Thanks for choosing our services", font=("Arial", 30, "bold"), background="#FFB72B", style="Header.TLabel")
        lbThanks.grid(row=1, column=1)

        self.frame_buttons = ttk.Frame(master)
        self.frame_buttons.pack()

        btBalance = ttk.Button(self.frame_buttons, text="Your Balance", command=self.account_balance)
        btBalance.grid(row=0, column=0, padx=20, pady=20, columnspan=2)

        ttk.Button(self.frame_buttons, text="Deposit 100 czk", command=self.deposit_100).grid(row=2, column=0, padx=5, pady=5)
        ttk.Button(self.frame_buttons, text="Deposit 200 czk", command=self.deposit_200).grid(row=2, column=1, padx=5, pady=5)
        ttk.Button(self.frame_buttons, text="Deposit 500 czk", command=self.deposit_500).grid(row=3, column=0, padx=5, pady=5)
        ttk.Button(self.frame_buttons, text="Deposit 1000 czk", command=self.deposit_1000).grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(self.frame_buttons, text="Get your money back.", width=50, font=("Arial", 11, "bold"),background="#008E89", justify="center").grid(row=4, column=0,padx=100, columnspan=2)

        self.withdraw = ttk.Entry(self.frame_buttons, width=15)
        self.withdraw.grid(row=5,column=1)
        ttk.Button(self.frame_buttons, text="Withdraw Money", command=self.get_money).grid(row=5, column=0, padx=5, pady=5)

        self.frame_summary = ttk.Frame(master)
        self.frame_summary.pack()

        self.summary = ttk.Label(self.frame_summary, background="red", text=f"Your account balance: {self.balance} CZK.", font=("default", 15,"bold"))
        self.summary.pack(padx=5, pady=5)


    def deposit_100(self):
        self.balance += 100
        self.summary.configure(text=f"Your account balance: {self.balance} CZK.",)


    def deposit_200(self):
        self.balance += 200
        self.summary.configure(text=f"Your account balance: {self.balance} CZK.",)

    def deposit_500(self):
        self.balance += 500
        self.summary.configure(text=f"Your account balance: {self.balance} CZK.",)

    def deposit_1000(self):
        self.balance += 1000
        self.summary.configure(text=f"Your account balance: {self.balance} CZK.",)

    def account_balance(self):
        print(self.balance)

    def get_money(self):
        self.withdrawal = Toplevel()
        self.withdrawal.title("Put your withdrawal details:")
        
        withdraw_lb = ttk.Label(self.withdrawal, text="Get your money back.\nEnter the amount:", background="#FFB72B")
        withdraw_lb.pack()
        self.withdraw_en= ttk.Entry(self.withdrawal, width=15)
        self.withdraw_en.pack()
        withdraw_bt = ttk.Button(self.withdrawal, text="Withdraw Money", command=self.take_money)
        withdraw_bt.pack( )        
        self.withdrawal.mainloop()

    def take_money(self):
        amount = self.withdraw_en.get()
        self.balance-= int(amount)
        self.withdraw.delete(0,"end")
        self.summary.configure(text=f"Your account balance: {self.balance} CZK.",)
        self.withdrawal.destroy()




 
def main():
    root = Tk()
    duplicates = Atm(root)
    root.mainloop()


if __name__ == '__main__':
    main()