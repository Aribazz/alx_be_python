import sys
from bank_account import BankAccount

def main():
    # Initialize the account with a default balance of $100
    account = BankAccount(100)

    # Check if the user provided sufficient command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Parse the command and any parameters
    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    # Process the command
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

def mainone():
    # Ensure the user provides exactly two arguments
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    # Retrieve numerator and denominator from command-line arguments
    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Perform the division using safe_divide
    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
    mainone()