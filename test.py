import csv
import os

def create_file_if_not_exists(file_name):
    if not os.path.exists(file_name):
        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Description', 'Amount'])

def add_expense(file_name):
    date = input("Enter the date (YYYY-MM-DD): ")
    description = input("Enter the description: ")
    amount = input("Enter the amount: ")
    
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, description, amount])
    print("Expense added successfully!")

def main():
    file_name = 'expenses.csv'
    create_file_if_not_exists(file_name)
    
    while True:
        print("\nExpense Tracker")
        print("1. Add an expense")
        print("2. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_expense(file_name)
        elif choice == '2':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
