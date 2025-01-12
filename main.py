import pandas as pd
import csv
from datetime import datetime
from data_input import get_date, get_amount, get_category, get_description , get_transaction_data

class CSV:
    #csv file name
    csv_file = "finance_data.csv"
    # function to read csv file and create csv file if not exists 
    @classmethod
    def initialize_csv(cls):
        try:
            # read csv file
            pd.read_csv(cls.csv_file)
        except FileNotFoundError:
            # create csv file
            df = pd.DataFrame(columns=["date", "amount", "category", "description"])
            df.to_csv(cls.csv_file, index=False)
            print("CSV file created successfully")

    # function to add data to csv file
    @classmethod
    def add_data_to_csv(cls, date, amount, category, description):
        # read csv file
        df = pd.read_csv(cls.csv_file)
        # new data to be added as dictionary
        new_data = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }

        # open csv file in append mode and write new data to the end of the file
        with open(cls.csv_file, 'a',newline='') as file:
            # create csv writer object
            writer = csv.DictWriter(file, fieldnames=["date", "amount", "category", "description"])
            # write new data to csv file
            writer.writerow(new_data)
            print("New Data added successfully")


# function to add all user data to csv file
    def add():
        CSV.initialize_csv()
        date = get_date("Enter date (DD-MM-YYYY) or leave blank to use today's date: ", allow_date=True)
        amount = get_amount()
        category = get_category()
        description = get_description()
        CSV.add_data_to_csv(date,amount,category,description)


# function to get all the transactions data by date from the csv file
    @classmethod
    def get_transactions_by_date(cls, start_date, end_date):
        # read csv file
        df = pd.read_csv(CSV.csv_file)
        # filter data by date
        df['date'] = pd.to_datetime(df['date'], format="%d-%m-%Y")
        mask = (df['date'] >= start_date) & (df['date'] <= end_date)
        filtered_data = df.loc[mask]

        if filtered_data.empty:
            print("No data found for the given date range")
        else:
            print(f'All Transactions Data from {start_date} to {end_date}')
            print(filtered_data.to_string(index=False)+"\n")
            # get total income, expense and net savings
            print("Summary:")
            total_income = filtered_data[filtered_data["category"] == "income"]["amount"].sum()
            total_expense = filtered_data[filtered_data["category"] == "expense"]["amount"].sum()
            print(f"Total Income: {total_income}")
            print(f"Total Expense: {total_expense}")
            net_savings = total_income - total_expense
            print(f"Net Savings: {net_savings:.2f}")

# function to start the code where user will be asked to enter data or get data by date range
    def main():
        while True:
            print("\n1. Welcome to Your Finance Tracker App")
            print("2. Enter 1 to add new transaction data")
            print("3. Enter 2 to get transaction data and summary by date range")
            print("Enter 3 to exit")
            user_choice = input("Enter your choice: (1 or 2 or 3): ")
            if user_choice == '1':
                CSV.add()
            elif user_choice == '2':
                start_date = get_date("Enter start date (DD-MM-YYYY): ")
                end_date = get_date("Enter end date (DD-MM-YYYY): ")
                CSV.get_transactions_by_date(start_date, end_date)
            elif user_choice == '3':
                print("Thank you for using the app. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1, 2 or 3.")
            
        

# # create csv file
# CSV.initialize_csv()

# add data to csv file
# CSV.add()

# get transactions data by date
# CSV.get_transactions_by_date("01-01-2025", "01-02-2026")

# start the code
if __name__ == "__main__":
    CSV.main()