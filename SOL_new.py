import csv

def load_csv_file(file_location):
    try:
        airbnb_data = []
        with open(file_location, 'r', encoding='utf-8') as file:
            # Construct the csv reader object from the file object
            reader = csv.reader(file)
            # Skip the header row
            next(reader)
            for line in reader:
                airbnb_data.append(line)
            print(f"\nFetching data...\nSucessfully loaded the {file_location} dataset. ")
            # Return the reader object
            return airbnb_data
    except IOError:
        print(f"Couldn't read {file_location}. ")

    
file_location = input("Enter file location: ")
data = load_csv_file(file_location)

def get_host_details():
        # Create an empty list to store the rows that match the criteria
        result_rows = []
        h_id = input("Enter the host id: ")
        # Loop through each row in the CSV file
        for row in data:
            # Check if the value in the 'Gender' column is 'Female'
            if row[0] == h_id:
                value1 = row[1]
                value2 = row[2]
                value3 = row[3]
                value4 = row[4]
                value5 = row[5]
                # If it is, add the entire row to the list of matching rows
                result_rows.append(row)
        # Print the matching rows
        print("The Host Id number {} details are :\n".format(h_id))
        print("The name of listing is :", value1)
        print("The description is:", value2)
        print("The host name is :", value3)
        print("The date created by host: ", value4)
        print("The host location is: ", value5) 

# Call the function
# get_host_details()


def get_location_details():
    import pandas as pd
    try:
        result_rows =[]
    location = input("Enter the host location: ").capitalize()
    # Loop through each row in the CSV file
    for row in data:
        # Check if the value in the 'host_id' column is 'h_id'
        if row[5] == location:
            value1 = row[1]
            value2 = row[13]
            value3 = row[20]
            value4 = row[21]
            value5 = row[22]
            # Create a dictionary for the row
            row_dict = {
                "Name of Listing": value1,
                "Property Type": value2,
                "Price": value3,
                "Minimum Night": value4,
                "Maximum Night": value5
            }
            # Append the row dictionary to the result list
            result_rows.append(row_dict)
        
    # Create a dataframe from the list of dictionaries
    df = pd.DataFrame(result_rows)
    return df 
        
    # working on the display format
    df = load_csv_file(data,num_rows)
    num_rows = 20
    start_pos = 0
    end_pos = min(start_pos + num_rows, len(df))

    while True:
        # Display the current set of rows
        print(df.iloc[start_pos:end_pos])
        if end_pos >= len(df):
            print("No more rows available.")
            break
        user_input = input("Enter 'next' to retrieve the next 20 rows, or 'quit' to exit: ")
        if user_input == 'next':
            start_pos += num_rows
            end_pos = min(start_pos + num_rows, len(df))
        elif user_input == 'quit':
            break

    except NameError:
        print(f"Couldn't find {location}. ")
    
# get_location_details()


def find_properties_by_location():
        # Create an empty list to store the rows that match the criteria
        result_rows1 = []
        p_type = input("Enter the property type: ")
        # Loop through each row in the CSV file
        for row in data:
            # Check if the value in the 'host_id' column is equal to 'p_type'
            if row[13] == p_type:
                value1 = row[14]
                value2 = row[15]
                value3 = row[16]
                value4 = row[17]
                value5 = row[18]
               # Create a dictionary for the row
                row_dict1 = {
                    "The room type ": value1,
                    "It accommodates ": value2,
                    "The bathroom is/are": value3,
                    "The bedrooms is/are": value4,
                    "The bed is/are": value5
                }
                # Append the row dictionary to the result list
                result_rows1.append(row_dict1)
  
        # Create a dataframe from the list of dictionaries
        df = pd.DataFrame(result_rows1)
        return df 
    
    
df = find_properties_by_location()
num_rows = 20
start_pos = 0
end_pos = min(start_pos + num_rows, len(df))

while True:
    # Display the current set of rows
    print(df.iloc[start_pos:end_pos])
    if end_pos >= len(df):
        print("No more rows available.")
        break
    user_input = input("Enter 'next' to retrieve the next 20 rows, or 'quit' to exit: ")
    if user_input == 'next':
        start_pos += num_rows
        end_pos = min(start_pos + num_rows, len(df))
    elif user_input == 'quit':
        break

## Question 2(PANDAS)
import pandas as pd

def load_pd_file():
    r_file = pd.DataFrame(data)
    return r_file.head()
load_pd_file()