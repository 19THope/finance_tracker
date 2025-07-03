import os # Interact with the operating system, useful for file and directory operations
import csv
from datetime import datetime 

# Dictionary to store transactions
transactions = {
    "income": [],
    "expenses": []
}


# Function to add an income
def add_income():
    amount = float(input("Enter your income amount: $"))
    if amount <= 0:
        print("❌ Amount must be positive. Please try again.\n")
        return
        
    category = input("Enter your income category (e.g.: Salary, Bonus, etc): ")
    if not category:
        print("❌ Category cannot be empty. Please try again.\n")
        return
        
    description = input("Enter a description for your income: ")
    date = datetime.today().strftime('%Y-%m-%d')  # Get current date
    transactions["income"].append((amount, category, description, date))
    print(f"✅ Income of ${amount:.2f} added successfully!\n")  # Added .2f formatting

'''
    add_income() - 
        collects details about an income source with local variables amount, category, description, date.
        stores data in a dictionnary transactions under the key income.
        automatically adds the current date by using datetime module.
'''

# Function to add an expense
def add_expense():
    amount = float(input("Enter your expense amount: $"))
    if amount <= 0:
        print("❌ Amount must be positive. Please try again.\n")
        return
        
    category = input("Enter your expense category (e.g.: Rent, Food, Transport, etc): ")
    if not category:
        print("❌ Category cannot be empty. Please try again.\n")
        return
        
    description = input("Enter a description for your expense: ")
    date = datetime.today().strftime('%Y-%m-%d')
    transactions["expenses"].append((amount, category, description, date))
    print(f"❌ Expense of ${amount:.2f} recorded successfully!\n")  # Added .2f formatting

'''
    add_expense() - 
        collects details about an expense with local variables amount, category, description, date.
        stores data in a dictionnary transactions under the key expenses.
        automatically adds the current date by using datetime module.
'''

# Function for a view financial summary
def view_summary():
    total_income = sum([entry[0] for entry in transactions["income"]]) 
    total_expense = sum([entry[0] for entry in transactions["expenses"]]) 
    balance = total_income - total_expense

    # Display the view financial summary
    print("\n💰 Financial Summary 💰")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expense:.2f}")
    print(f"Current Balance: ${balance:.2f}")

'''
    view_summary() - provides financial overview by calculating and displaying
        extracts the first element amount from each tuple transactions["income"] or transactions["expenses"] and sum them.
        prints a formatted summary.
        using of .2f to display amounts as 2 decimal places (e.g.: 100.05).
'''

# Function to save transactions to a csv file
def save_to_csv():
    filename = "finance_data.csv"
    try:
        # Check if file exists to determine if we need headers
        file_exists = os.path.exists(filename)
        
        with open(filename, "a" if file_exists else "w", newline="") as file:
            writer = csv.writer(file)
            
            # Write headers only if creating new file
            if not file_exists:
                writer.writerow(["Type", "Amount", "Category", "Description", "Date"])
            
            # Get existing transaction dates to avoid duplicates
            existing_dates = set()
            if file_exists:
                with open(filename, "r") as read_file:
                    reader = csv.reader(read_file)
                    next(reader)  # Skip header
                    for row in reader:
                        existing_dates.add((row[0], row[4]))  # Store unique transaction defined by paris (Type, Date)
            
            # Append only new transactions
            for entry in transactions["income"]:
                if ("Income", entry[3]) not in existing_dates:  # Check if (Type, Date) exists
                    writer.writerow(["Income", *entry])
            
            for entry in transactions["expenses"]:
                if ("Expense", entry[3]) not in existing_dates:
                    writer.writerow(["Expense", *entry])
                    
        print(f"📂 Data {'appended to' if file_exists else 'saved to'} {filename} successfully!\n")
        
    except PermissionError:
        print(f"❌ Permission denied. Could not save to {filename}\n")
    except Exception as e:
        print(f"❌ Unexpected error saving data: {e}\n")

'''
    save_to_csv - saves financial transaction both income and expenses to a csv file named finance_data.csv
        creates and opens finance_data.csv in write mode ("w").
        uses Python's csv module to handle formatting.
        creates column labels: Type (Income/Expense), Amount, Category, Description, Date.
        prefixes each income/expenses entry with "Income"/"Expenses", unpacks the tuple (amount, category, description, date) using *entry.
'''