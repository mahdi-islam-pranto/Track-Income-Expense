from datetime import datetime


date_format = "%d-%m-%Y"
categories = {
    "I": "income",
    "E": "expense"
}

# function to get the date from user
def get_date(user_date, allow_date = False):
    # get date from user
    date_str = input(user_date)
    # if user does not enter date 
    if allow_date and not date_str:
        # return today's date
        return datetime.today().strftime(
            "%d-%m-%Y"
        )
    
    # if user enters date
    try:
        # valid date format
        valid_date = datetime.strptime(date_str, "%d-%m-%Y")
        return valid_date.strftime("%d-%m-%Y")
    
    except ValueError:
        # if user enters invalid date
        print("Invalid date format. Please enter date in DD-MM-YYYY format.")
        return get_date(user_date, allow_date)
    

# function to get the amount from user
def get_amount():
    try:
        ammount = float(input("Enter amount: "))
        if ammount <= 0:
            raise ValueError("Amount should be non zero positive number")
        return ammount
    except ValueError as e:
        print(e)
        return get_amount()

# function to get the category from user
def get_category():
    category = input("Enter category (I for income, E for expense): ").upper()
    if category in categories:
        return categories[category]
    
    print("Invalid category. Please enter I for income and E for expense.")
    return get_category()

# function to get the description from user
def get_description():
    description = input("Enter description: ")
    
    if not description:
        print("Description cannot be empty.")
        return get_description()
    return description
    

# get transactions data by date
def get_transaction_data():
    start_date = input("Enter start date (DD-MM-YYYY): ")

    try:
        # valid date format
        start_date = datetime.strptime(start_date, "%d-%m-%Y")
        # return valid_date.strftime("%d-%m-%Y")
    
    except ValueError:
        # if user enters invalid date
        print("Invalid date format. Please enter date in DD-MM-YYYY format.")
        return get_transaction_data()
        
    end_date = input("Enter end date (DD-MM-YYYY): ")

    try:
        # valid date format
        end_date = datetime.strptime(end_date, "%d-%m-%Y")
        # return valid_date.strftime("%d-%m-%Y")
    
    except ValueError:
        # if user enters invalid date
        print("Invalid date format. Please enter date in DD-MM-YYYY format.")
        return get_transaction_data()
    
    return start_date.strftime("%d-%m-%Y"), end_date.strftime("%d-%m-%Y")

# get_description()
# get_transaction_data()

