## Question C(Visualization)
# the proportion of number of bedrooms of Airbnb listing using pie chart
import matplotlib.pyplot as plt

from Data_loading_and_user_code import load_pd_file

def plot_bedroom_distribution(loaded_data):
    bedrooms_counts = loaded_data['bedrooms'].value_counts()

    plt.figure(figsize=(8, 8))
    plt.pie(bedrooms_counts.values, labels=bedrooms_counts.index)
    plt.axis('equal')
    plt.tight_layout()
    plt.title('Distribution of Bedrooms for AirBnB')

    legend_labels = []
    for label, count in zip(bedrooms_counts.index, bedrooms_counts.values):
        legend_labels.append(f'{label}: {count}')

    plt.legend(legend_labels, loc='best')

    legend_title = 'Bedrooms'
    plt.text(0.8, 1.1, legend_title, fontsize=12)

    plt.show()




# Display the number of listings for each room type using bar chart
def plot_room_type_counts(loaded_data):
    # Calculate the counts of each room type
    room_type_counts = loaded_data['room_type'].value_counts()

    # Create the bar chart
    plt.figure(figsize=(8, 6))
    bars = plt.bar(room_type_counts.index, room_type_counts.values)

    # Set labels and title
    plt.xlabel('Room Type')
    plt.ylabel('Count')
    plt.title('Number of listings for each room type')
    
    # Add labels to the bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height,
                 height, ha='center', va='bottom')


    # Show the plot
    plt.show()
    



# Display the relationship between accommodates and price using scatter plot
def plot_scatter(loaded_data):
    x = loaded_data['accommodates']
    y = loaded_data['price']

    # Create a scatter plot
    plt.scatter(x, y)

    # Add labels and title
    plt.xlabel('Accommodates')
    plt.ylabel('Price')
    plt.title('Relationship between Accommodates and Price')

    # Show the plot
    plt.show()





# Display Airbnb prices from 2019 - 2022 with line chart using subplots (one year per plot)
def subplot_airbnb_prices(loaded_data):
    import pandas as pd
    # Extract the relevant columns
    new_data = loaded_data[['host_since', 'price']]
    new_data = new_data.rename(columns={'host_since': 'Year'})
    
    # Convert 'Year' column to datetime
    new_data['Year'] = pd.to_datetime(new_data['Year'])
    
    # Extract the year from the 'Year' column
    new_data['Year'] = new_data['Year'].dt.year
    
    # Perform multiple slicings based on yearly periods
    year_2019 = new_data[new_data['Year'] == 2019]
    year_2020 = new_data[new_data['Year'] == 2020]
    year_2021 = new_data[new_data['Year'] == 2021]
    year_2022 = new_data[new_data['Year'] == 2022]
    
    # Create subplots
    fig, axs = plt.subplots(2, 2, figsize=(12, 8), sharey=True)

    # Plot line graph for Year 2019
    axs[0, 0].plot(year_2019['price'])
    axs[0, 0].set_title('Year 2019')

    # Plot line graph for Year 2020
    axs[0, 1].plot(year_2020['price'])
    axs[0, 1].set_title('Year 2020')

    # Plot line graph for Year 2021
    axs[1, 0].plot(year_2021['price'])
    axs[1, 0].set_title('Year 2021')

    # Plot line graph for Year 2022
    axs[1, 1].plot(year_2022['price'])
    axs[1, 1].set_title('Year 2022')

    # Adjust spacing between subplots
    fig.tight_layout()
    fig.suptitle('Subplots of price for years 2019 to 2022')
    plt.subplots_adjust(top=0.9)
    # Show the plot
    plt.show()


