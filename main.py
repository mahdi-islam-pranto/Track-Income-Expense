import pandas as pd
import csv
from datetime import datetime


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



# create csv file
CSV.initialize_csv()

# add data to csv file
CSV.add_data_to_csv("8-1-2024", 100, "income", "bonus")
