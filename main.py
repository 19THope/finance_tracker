
# Create a menu for user interaction
def main():
    while True:
        print("\n👔 Personal Finance Tracker")
        print("1️⃣ Add Income")
        print("2️⃣ Add Expense")
        print("3️⃣ View Summary")
        print("4️⃣ Save and Exit")

        choice = input("Select an option: ")

        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            view_summary()
        elif choice == "4":
            save_to_csv()
            print("🔐 Exiting program. Data saved.") 
            break
        else:
            print("❌ Invalid choice. Please try again.")

'''
    main() - serves as the central control loop for Personal Finance Tracker
        displays a persistent menu
        runs in an infinite loop (while True) until the user chooses to exit.
        shows four options: add income, add expense, view summary, save and exit.
        uses if-elif-else to map the choice to options
        handles invalid choice (e.g., 5), prints "Invalid choice...", the loop continues prompts the user again.
        only breaks the loop when the user selects 4 (Save and Exit) and prints a confirmation message "...Data saved"
'''

# Run the program
main()