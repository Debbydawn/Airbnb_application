def run_airbnb_program():
    print("Welcome to Airbnb Application")
    username = input("What is your name? ")
    username = username.upper()
    print(f"\nYes, {username}, let's get to work.")
    import Data_processing_and_analysis
    import Data_visualization
    


    while True:
        print("\nPlease select a section:")
        print("A. Work with a CSV file")
        print("B. Work with a Pandas file")
        print("C. Visualize using the pandas data")

        try:
            choice1 = input("Enter the section (A-C): ").upper()
            
            if choice1 == "A":
                print("\nPlease select an operation:")
                print("1. Load the data from a CSV file")
                print("2. Get some details on an individual host by host_id")
                print("3. Get details of all Airbnb listings for a specified location")
                print("4. Get details of all Airbnb listings for a specified property type")
                choice_A = int(input("Enter your choice (1-4): "))

                if choice_A == 1:
                    # Perform option 1
                    print("Option 1 selected.")
                    data = load_csv_file()

                elif choice_A == 2:
                    # Perform option 2
                    print("Option 2 selected.")
                    from Data_processing_and_analysis import get_host_details
                    # host_details = get_host_details()
                    host_details = Data_processing_and_analysis.get_host_details(data)
                    print(host_details)

                elif choice_A == 3:
                    # Perform option 3
                    print("Option 3 selected.")
                    from Data_processing_and_analysis import get_location_details
                    location_details = Data_processing_and_analysis.get_location_details(data)
                    print(location_details)

                elif choice_A == 4:
                    # Perform option 4
                    print("Option 4 selected.")
                    from Data_processing_and_analysis import find_properties_by_location
                    properties = Data_processing_and_analysis.find_properties_by_location(data)
                    print(properties)

                else:
                    print("Invalid choice. Please enter a valid option.")

            elif choice1 == "B":
                print("\nPlease select an operation:")
                print("5. Load your data from a CSV file into a pandas DataFrame")
                print("6. Get the most popular amenities or features in Airbnb")
                print("7. Get the average price of stay in each location")
                print("8. Get the average review scores rating for each location")
                choice_B = int(input("Enter your choice (5-8): "))

                if choice_B == 5:
                    # Perform option 5
                    print("Option 5 selected.")
                    loaded_data = load_pd_file()

                elif choice_B == 6:
                    # Perform option 6
                    print("Option 6 selected.")
                    from Data_processing_and_analysis import get_most_popular_amenity
                    popular_amenity = Data_processing_and_analysis.get_most_popular_amenity(loaded_data)
                    print(popular_amenity)

                elif choice_B == 7:
                    # Perform option 7
                    print("Option 7 selected.")
                    from Data_processing_and_analysis import average_price_location
                    average_price = Data_processing_and_analysis.average_price_location(loaded_data)
                    print(average_price)

                elif choice_B == 8:
                    # Perform option 8
                    print("Option 8 selected.")
                    from Data_processing_and_analysis import average_review_location
                    average_review = Data_processing_and_analysis.average_review_location(loaded_data)
                    print(average_review)

                else:
                    print("Invalid choice. Please enter a valid option.")

            elif choice1 == "C":
                print("\nPlease select an operation:")
                print("9. Get the proportion of the number of bedrooms of Airbnb listings using a pie chart")
                print("10. Get the number of listings for each room type using a bar chart")
                print("11. Get the relationship between accommodates and price using a scatter plot")
                print("12. Get Airbnb prices from 2019-2022 with a line chart using subplots")
                choice_C = int(input("Enter your choice (9-12): "))

                if choice_C == 9:
                    # Perform option 9
                    print("Option 9 selected.")
                    from Data_visualization import plot_bedroom_distribution
                    plot_bedroom = Data_visualization.plot_bedroom_distribution(loaded_data)

                elif choice_C == 10:
                    # Perform option 10
                    print("Option 10 selected.")
                    from Data_visualization import plot_room_type_counts
                    plot_room = Data_visualization.plot_room_type_counts(loaded_data)

                elif choice_C == 11:
                    # Perform option 11
                    print("Option 11 selected.")
                    from Data_visualization import plot_scatter
                    plot_scatter = Data_visualization.plot_scatter(loaded_data)

                elif choice_C == 12:
                    # Perform option 12
                    print("Option 12 selected.")
                    from Data_visualization import subplot_airbnb_prices
                    plot_subplot = Data_visualization.subplot_airbnb_prices(loaded_data)

                else:
                    print("Invalid choice. Please enter a valid option.")

        except ValueError:
            print("Invalid input. Please enter a valid integer.")

        # Ask the user if they want to continue or exit
        continue_choice = input("Do you want to perform another operation? (yes/no): ")
        
        if continue_choice.lower() != 'yes':
            print("Exiting...\nExited")
            break

    
       

import csv

def load_csv_file():
    try:
        file_location = input("Enter file location: ")
        airbnb_data = []
        with open(file_location, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for line in reader:
                airbnb_data.append(line)
            print(f"\nFetching data...\nSuccessfully loaded the {file_location} dataset.")
            return airbnb_data
    except csv.Error:
        print(f"Invalid CSV file: {file_location}")
    except FileNotFoundError:
        print(f"File not found: {file_location}")
    except IOError:
        print(f"Couldn't read {file_location}.")




import pandas as pd

def load_pd_file():
    try:
        data_location = input('What is the location of the file you want to import from: ')
        r_file = pd.read_csv(data_location)
        print(f"\nFetching data...\nSuccessfully loaded the {data_location} dataset.")
        return r_file

    except pd.errors.EmptyDataError:
        print("The file is empty.")
    except pd.errors.ParserError:
        print("An error occurred while parsing the file.")
    except pd.errors.DtypeWarning:
        print("Warning: Data type mismatch.")
    except OSError:
        print(f"Couldn't read {data_location}.")





from Data_processing_and_analysis import get_host_details, get_location_details, find_properties_by_location
from Data_processing_and_analysis import average_price_location, average_review_location