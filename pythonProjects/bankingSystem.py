class BankingSystem:
    def __init__(self):
        self.pin_attempts = 1
        self.pin = 1010
        self.accbal = 500

    def main_menu(self):
        while self.pin_attempts <= 3:
            entered_pin = int(input("Enter 4 digit pin: "))
            if entered_pin == self.pin:
                self.show_menu()
                break
            else:
                if self.pin_attempts == 3:
                    print("Invalid pin. Contact bank.")
                    break
                print("Invalid pin")
                self.pin_attempts += 1

    def show_menu(self):
        while True:
            print("1. Deposit")
            print("2. Account balance")
            print("3. Withdraw")
            print("4. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.deposit()
            elif choice == 2:
                self.check_balance()
            elif choice == 3:
                self.withdraw()
            elif choice == 4:
                print("Thank you")
                break
            else:
                print("Invalid choice")

    def deposit(self):
        dep = int(input("Enter deposit amount: "))
        print(f"Before deposit: {self.accbal}")
        self.accbal += dep
        print(f"After deposit: {self.accbal}")

    def check_balance(self):
        print(f"Account balance: {self.accbal}")

    def withdraw(self):
        withdraw = int(input("Enter withdraw amount: "))
        if withdraw > self.accbal:
            print("Insufficient funds")
        else:
            print(f"Before withdraw: {self.accbal}")
            self.accbal -= withdraw
            print(f"After withdraw: {self.accbal}")


if __name__ == "__main__":
    banking_system = BankingSystem()
    banking_system.main_menu()
