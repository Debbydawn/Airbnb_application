# import csv

# def load_csv_file(file_location):
#     try:
#         airbnb_data = []
#         with open(file_location, 'r', encoding='utf-8') as file:
#             # Construct the csv reader object from the file object
#             reader = csv.reader(file)
#             # Skip the header row
#             next(reader)
#             for line in reader:
#                 airbnb_data.append(line)
#             print(f"\nFetching data...\nSucessfully loaded the {file_location} dataset. ")
#             # Return the reader object
#             return airbnb_data
#     except csv.Error:
#         print(f"Invalid CSV file: {file_path}")
#     except FileNotFoundError:
#         print(f"File not found: {file_location}")
#     except IOError:
#         print(f"Couldn't read {file_location}. ")
    
       
    
# file_location = input("Enter file location: ")
# data = load_csv_file(file_location)

def get_host_details():
    # Create an empty list to store the rows that match the criteria
    result_rows = []
    while True:
        try:
            h_id = int(input("Enter the host id: "))
            # Loop through each row in the CSV file
            for row in data:
                # Convert row[0] to integer for comparison
                if int(row[0]) == h_id:
                    value1 = row[1]
                    value2 = row[2]
                    value3 = row[3]
                    value4 = row[4]
                    value5 = row[5]
                    # If it is, add the entire row to the list of matching rows
                    result_rows.append(row)
            # Print the matching rows
            if result_rows:
                print("The Host Id number {} details are :\n".format(h_id))
                print("The name of listing is :", value1)
                print("The description is:", value2)
                print("The host name is :", value3)
                print("The date created by host: ", value4)
                print("The host location is: ", value5)
            else:
                print("No matching host details found.")
            return
        except ValueError:
            print("Invalid input. Please enter an integer.")

# Call the function
# get_host_details()


def get_location_details():

    # Assuming you have loaded the data into a list called 'data'
    try:
        result_rows = []
        location = input("Enter the host location: ").capitalize()

        # Loop through each row in the list 'data'
        for row in data:
            # Check if the value in the 'host_id' column is 'location'
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

        # Create a DataFrame from the list of dictionaries
        df = pd.DataFrame(result_rows)

        if not df.empty:
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
    try:
        # Create an empty list to store the rows that match the criteria
        result_rows = []
        p_type = input("Enter the property type: ")

        if not p_type.isdigit():
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
                    row_dict = {
                        "The room type": value1,
                        "It accommodates": value2,
                        "The bathroom is/are": value3,
                        "The bedrooms is/are": value4,
                        "The bed is/are": value5
                    }
                    # Append the row dictionary to the result list
                    result_rows.append(row_dict)

            if len(result_rows) > 0:
                location_data = result_rows
            else:
                raise ValueError("Property type not found.")
        else:
            raise ValueError("Invalid input. Please enter a string.")

    except ValueError as ve:
        print(ve)
    except Exception as e:
        print("An error occurred:", str(e))

    if location_data is not None:
        num_rows = 20
        start_pos = 0
        end_pos = min(start_pos + num_rows, len(location_data))

        while True:
            # Display the current set of rows
            for row in location_data[start_pos:end_pos]:
                print("The room type:", row["The room type"])
                print("It accommodates:", row["It accommodates"])
                print("The bathroom is/are:", row["The bathroom is/are"])
                print("The bedrooms is/are:", row["The bedrooms is/are"])
                print("The bed is/are:", row["The bed is/are"])
                print()

            if end_pos >= len(location_data):
                print("No more rows available.")
                break

            user_input = input("Enter 'next' to retrieve the next 20 rows, or 'quit' to exit: ")
            if user_input == 'next':
                start_pos += num_rows
                end_pos = min(start_pos + num_rows, len(location_data))
            elif user_input == 'quit':
                break

# find_properties_by_location()

## Question B(PANDAS)
# question B1

# import pandas as pd

# def load_pd_file():
#     try:
#         file_location = input('What is the location of the file you want to import from: ')
#         r_file = pd.read_csv(file_location)
#         print(f"\nFetching data...\nSuccessfully loaded the {file_location} dataset.")
#         return r_file

#     except pd.errors.EmptyDataError:
#         print("The file is empty.")
#     except pd.errors.ParserError:
#         print("An error occurred while parsing the file.")
#     except pd.errors.DtypeWarning:
#         print("Warning: Data type mismatch.")
#     except OSError:
#         print(f"Couldn't read {file_location}.")

# loaded_data = load_pd_file()


# question B2
def get_most_popular_amenity(loaded_data):

    # Assuming you have loaded the data into a DataFrame called 'loaded_data'
    amenities = loaded_data['amenities'].tolist()  # Convert amenities column to a list
    amenities_list = [amenity.strip() for sublist in [amenity.split(',') for amenity in amenities] for amenity in sublist]  # Split each string by commas, flatten the list, and remove leading/trailing whitespace
    v_counts = pd.Series(amenities_list).value_counts().to_frame()  # Count the occurrence of each amenity
    most_popular_amenity = v_counts.index[0]  # Get the most popular amenity (first index of the value counts)
    most_popular_count = v_counts.iloc[0, 0]  # Get the count of the most popular amenity

    print(f"The most popular amenity is '{most_popular_amenity}' with a count of {most_popular_count}.")
    
# get_most_popular_amenity(loaded_data)


# question B3
def average_price_location():

    # Assuming you have loaded the data into a DataFrame called 'loaded_data'
    try:
        # Average price based on location
        av_price = loaded_data.groupby('host_location')['price'].mean().round(2)
        # Create a dataframe from the average prices
        average_price = pd.DataFrame(av_price)

        if not average_price.empty:
            num_rows = 20
            start_pos = 0
            end_pos = min(start_pos + num_rows, len(average_price))

            while True:
                # Display the current set of rows
                print(average_price.iloc[start_pos:end_pos])

                if end_pos >= len(average_price):
                    print("No more rows available.")
                    break

                user_input = input("Enter 'next' to retrieve the next 20 rows, or 'quit' to exit: ")
                if user_input == 'next':
                    start_pos += num_rows
                    end_pos = min(start_pos + num_rows, len(average_price))
                elif user_input == 'quit':
                    break

    except Exception as e:
        print("An error occurred:", str(e))
        
        
# average_price_location()


# question B4        
def average_review_location():

    # Assuming you have loaded the data into a DataFrame called 'loaded_data'
    try:
        # Average review scores rating by location
        avg_review = loaded_data.groupby('host_location')['review_scores_rating'].mean().round(2)
        # Create a dataframe from the average review scores
        df = pd.DataFrame(avg_review)

        if not df.empty:
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

    except Exception as e:
        print("An error occurred:", str(e))
        
        
# average_review_location()

    
