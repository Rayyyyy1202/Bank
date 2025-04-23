from bank import Bank

def main():
    bank = Bank()

    # Clean start: reset existing accounts
    bank.accounts.clear()
    bank.save()

    print("=== Creating accounts ===")
    try:
        bank.create_account("Alice", 1000)
        bank.create_account("Bob", 500)
        bank.create_account("Charlie", 0)
    except ValueError as e:
        print("Account creation error:", e)

    print_balances(bank)

    print("\n=== Depositing Money ===")
    bank.deposit("Alice", 200)
    bank.deposit("Charlie", 50)
    print_balances(bank)

    print("\n=== Withdrawing Money ===")
    try:
        bank.withdraw("Bob", 100)
        bank.withdraw("Charlie", 100)  # Should raise ValueError
    except ValueError as e:
        print("Withdraw error:", e)
    print_balances(bank)

    print("\n=== Transferring Money ===")
    try:
        bank.transfer("Alice", "Bob", 300)
        bank.transfer("Bob", "Charlie", 200)
        bank.transfer("Alice", "Alice", 100)  # Should raise error
    except ValueError as e:
        print("Transfer error:", e)
    print_balances(bank)

    print("\n=== Invalid Operations ===")
    try:
        bank.deposit("Ghost", 50)
    except ValueError as e:
        print("Expected error (deposit to non-existent):", e)

    try:
        bank.withdraw("Ghost", 10)
    except ValueError as e:
        print("Expected error (withdraw from non-existent):", e)

    try:
        bank.create_account("Alice", 100)
    except ValueError as e:
        print("Expected error (duplicate account):", e)

    print("\n=== Final Balances ===")
    print_balances(bank)

def print_balances(bank):
    for name, acc in bank.accounts.items():
        print("%s: $%.2f" % (name, acc.balance))

if __name__ == "__main__":
    main()
