import hashlib

class ATM:
    def __init__(self):
        self.balance = 0.0
        self.is_authenticated = False
        self.pin_hash = self._hash_pin("1234")  

    def _hash_pin(self, pin):
        return hashlib.sha256(pin.encode()).hexdigest()

    def authenticate_user(self):
        entered_pin = input("\nEnter your PIN: ")
        if self._hash_pin(entered_pin) == self.pin_hash:
            self.is_authenticated = True
            print("\nAuthentication successful.")
        else:
            print("\nAuthentication failed. Incorrect PIN.")

    def _check_authentication(self):
        if not self.is_authenticated:
            print("\nPlease authenticate first.")
            return False
        return True

    def check_balance(self):
        if not self._check_authentication():
            return
        print(f"\nYour current balance is: Rs. {self.balance:.2f}")

    def deposit(self):
        if not self._check_authentication():
            return
        amount = self._get_positive_float("\nEnter the amount to deposit: ")
        if amount is not None:
            self.balance += amount
            print(f"\nDeposited Rs. {amount:.2f}")

    def withdraw(self):
        if not self._check_authentication():
            return
        amount = self._get_positive_float("\nEnter the amount to withdraw: ")
        if amount is not None:
            if amount <= self.balance:
                self.balance -= amount
                print(f"\nWithdrew Rs. {amount:.2f}")
            else:
                print("\nInsufficient funds.")

    def _get_positive_float(self, prompt):
        try:
            amount = float(input(prompt))
            if amount > 0:
                return amount
            else:
                print("\nAmount must be greater than zero.")
        except ValueError:
            print("\nInvalid amount. Please enter a numeric value.")
        return None

    def change_pin(self):
        if not self._check_authentication():
            return
        new_pin = input("\nEnter new PIN: ")
        self.pin_hash = self._hash_pin(new_pin)
        print("\nPIN changed successfully.")

    def display_menu(self):
        while True:
            print("\nATM Menu:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Change PIN")
            print("5. Exit\n")
            choice = input("\nChoose an option: ")
            
            if choice == '1':
                self.check_balance()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                self.change_pin()
            elif choice == '5':
                print("\nExiting. Thank you for using the ATM.")
                break
            else:
                print("\nInvalid choice. Please enter a number between 1 and 5.")

def main():
    atm = ATM()
    atm.authenticate_user()
    if atm.is_authenticated:
        atm.display_menu()

if __name__ == "__main__":
    main()
