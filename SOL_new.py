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

## Question B(PANDAS)
# question B1

import pandas as pd

def load_pd_file():
    try:
        file_location = input('What is the location of the file you want to import from: ')
        r_file = pd.read_csv(file_location)
        print(f"\nFetching data...\nSucessfully loaded the {file_location} dataset. ")
        return r_file

    except IOError:
            print(f"Couldn't read {file_location}. ")
            
# loaded_data = load_pd_file()



# question B2
def get_most_popular_amenity(data):
    amenities = data['amenities'].tolist()  # Convert amenities column to a list
    amenities_list = [amenity.split(',') for amenity in amenities]  # Split each string by commas to create lists of individual amenities
    flattened_amenities = [item.strip() for sublist in amenities_list for item in sublist]  # Flatten the list of lists and remove leading/trailing whitespace
    v_counts = pd.Series(flattened_amenities).value_counts().to_frame()  # Count the occurrence of each amenity
    most_popular_amenity = v_counts.index[0]  # Get the most popular amenity (first index of the value counts)
    most_popular_count= v_counts.iloc[0, 0]  # Get the count of the most popular amenity
    return most_popular_amenity, most_popular_count

# Assuming you have loaded the data into a DataFrame called 'loaded_data'
most_popular_amenity, count = get_most_popular_amenity(loaded_data)
print(f"The most popular amenity is {most_popular_amenity} with count of :",count )



# question B3
def averge_price_location():
    # average price based on location
    av_price = loaded_data.groupby('host_location')['price'].mean()
    av_price = round(av_price,2)
    # Create a dataframe from the list of dictionaries
    df = pd.DataFrame(av_price)
    return df

df = averge_price_location()
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
        

# question B4        
def average_review_location():
    # average review scores rating by location
    avg_review = loaded_data.groupby('host_location')['review_scores_rating'].mean()
    avg_review = round(avg_review,2)
    # Create a dataframe from the list of dictionaries
    df = pd.DataFrame(avg_review)
    return df

df = average_review_location()
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
    
    
## Question C(Visualization)

