import csv
file_location = input("Enter file location: ")

def get_host_details():
    with open(file_location, 'r', encoding='utf-8') as file:
        # Construct the csv reader object from the file object
        reader = csv.reader(file)
        # Skip the header row
        next(reader)
    # Rest of the code
        # Create an empty list to store the rows that match the criteria
        result_rows = []
        h_id = input("Enter the host id: ")
        # Loop through each row in the CSV file
        for row in reader:
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
    with open('C:/Users/adedi_tpk1ys1/OneDrive/Documents/Nw/Airbnb_UK_2022.csv.xls', 'r', encoding='utf-8') as file:
        # Construct the csv reader object from the file object
        reader = csv.reader(file)
        # Skip the header row
        next(reader)
        # Create an empty list to store the rows that match the criteria
        result_rows = []
        p_type = input("Enter the host location: ") #.capitalize()
        # Loop through each row in the CSV file
        for row in reader:

            # Check if the value in the 'host_id' column is 'h_id'
            if row[13] == p_type:
                value1 = row[14]
                value2 = row[15]
                value3 = row[16]
                value4 = row[17]
                value5 = row[18]
    #             #if it is, add the entire row to the list of matching rows
    #             result_rows.append([value1,value2,value3,value4,value5])

    #     # Print the matching rows
    #     print(result_rows)
                for row in reader:
                    print("\nFor properties with host id {} details are :\n".format(row[0]))
                    print("The room type is :",value1)
                    print("It accommodates :",value2)
                    print("The bathroom is :", value3)
                    print("The bedrooms is : ", value4)
                    print("The bed is: ", value5)
                
# get_location_details()