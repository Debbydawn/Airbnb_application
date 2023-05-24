print("Welcome to Dawn Airbnb\nWhat is your name?")
username = input("Please enter your desired name: ")
username = username.upper()
print(f"\nYes, {username} lets get to work.")
while True:
    print("\nPlease select an operation:")
    print("1. Load the data from a CSV file")
    print("2. Get some details on an individual host by host_id")
    print("3. Get some deatils of all Airbnb listing for a specified location")
    print("4. Get some details of all Airbnb listing for a specified property type")
    print("5. Load your data from a CSV file into a pandas Dataframe")
    print("6. Get the most popular amenities or features in Airbnb")
    print("7. Get the average price of stay in each location")
    print("8. Get the average review scores rating for each location")
    print("9. Get the proportion of number of bedrooms of Airbnb listing using pie chart")
    print("10. Get the number of listings for each room type using bar chart")
    print("11. Get the relationship between accommodates and price using scatter plot")    
    print("12. Get Airbnb prices from 2019 - 2022 with line chart using subplots")
    print("0. Exit")

    try:
        choice = int(input("Enter your choice (0-12): "))
        
        if choice == 1:
            # Perform option 1
            print("Option 1 selected.")
            loaded_data = load_pd_file()
            
        elif choice == 2:
            # Perform option 2
            print("Option 2 selected.")
            host_details = get_host_details()
            print(host_details) 
            
        elif choice == 3:
            # Perform option 3
            print("Option 3 selected.")
            location_details = get_location_details()
            print(location_details)
            
        elif choice == 4:
            # Perform option 4
            print("Option 4 selected.")
            properties = find_properties_by_location()
            print(properties)
            
        elif choice == 5:
            # Perform option 5
            print("Option 5 selected.")
            load_pd_file()
            
        elif choice == 6:
            # Perform option 6
            print("Option 6 selected.")
            popular_amenity = get_most_popular_amenity(loaded_data)
            print(popular_amenity)
            
        elif choice == 7:
            # Perform option 7
            print("Option 7 selected.")
            average_price= average_price_location()
            print(average_price)
            
        elif choice == 8:
            # Perform option 8
            print("Option 8 selected.")
            average_review = average_review_location()
            print(average_review)
            
        elif choice == 9:
            # Perform option 9
            print("Option 9 selected.")
            plot_bedroom_distribution(loaded_data)
            
        elif choice == 10:
            # Perform option 10
            print("Option 10 selected.")
            plot_room_type_counts(loaded_data)
            
        elif choice == 11:
            # Perform option 11
            print("Option 11 selected.")
            plot_scatter(loaded_data)
            
        elif choice == 12:
            # Perform option 12
            print("Option 12 selected.")
            subplot_airbnb_prices(loaded_data)
            
        elif choice == 0:
            # Exit the program
            print("Exiting...")
            break
            
        else:
            print("Invalid choice. Please enter a valid option.")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    
    # Ask the user if they want to continue or exit
    continue_choice = input("Do you want to perform another operation? (yes/no): ")
    if continue_choice.lower() != 'yes':
        print("Exiting...\nExited")
        break
