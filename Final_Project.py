import pandas as pd
import matplotlib.pyplot as plt
import sys

# Load the data
df = pd.read_csv("/Users/diyamehta/Desktop/Vir/VITYARTHI/final.csv")

#Clean the data extracted from CSV file
df.columns = df.columns.str.strip()
print("Columns after cleaning:", df.columns.tolist())

# Check for 'Users Millions' column and handle duplicates
if 'Users Millions' not in df.columns:
    print("Looking for Users Millions column...")
    for col in df.columns:
        if 'users' in col.lower() and 'millions' in col.lower():
            df = df.rename(columns={col: 'Users Millions'})
            break
    print("Available columns:", df.columns.tolist())

def select_from_list(options, prompt):

    sorted_options = sorted(options)
    while True:
        print("\n" + prompt)
        for i, opt in enumerate(sorted_options, 1):
            print(f"{i}. {opt}")
        try:
            choice = int(input("Enter number (or 0 to search): ")) - 1
            if choice == -1:
                search_term = input("Search term: ").strip().lower()
                matches = [opt for opt in sorted_options if search_term in opt.lower()]
                if matches:
                    print("Matches:")
                    for i, match in enumerate(matches, 1):
                        print(f"{i}. {match}")
                    sub_choice = int(input("Select (number): ")) - 1
                    return matches[sub_choice]
                else:
                    print("No matches found.")
                    continue
            if 0 <= choice < len(sorted_options):
                return sorted_options[choice]
            else:
                print("Invalid choice.")
        except (ValueError, IndexError):
            print("Invalid input. Try again.")
            
#Structuring the Main Menu
def main_menu():
    while True:
        print("\n" + "="*24)
        print("Mobile Phones Over the Years")
        print("="*24)
        print("1. Data Visualization")
        print("2. Data Analysis")
        print("3. Data Manipulation")
        print("4. Exit")
        opt = input("Your choice: ").strip()
        if opt == '1':
            visualization_menu()
        elif opt == '2':
            analysis_menu()
        elif opt == '3':
            manipulation_menu()
        elif opt == '4':
            print("Thank you. Closing now...")
            sys.exit()
        else:
            print("Invalid option. Try again.")

#Structuring the Visualization Menu
def visualization_menu():
    while True:
        print("\n" + "-"*20)
        print("Visualization Menu")
        print("-"*20)
        print("1. Line Chart for a City")
        print("2. Bar Chart for a City")
        print("3. Compare Cities (Line Chart)")
        print("4. Back")
        opt = input("Your choice: ").strip()
        if opt == '1':
            plot_city_line_chart()
        elif opt == '2':
            plot_city_bar_chart()
        elif opt == '3':
            compare_cities_line_chart()
        elif opt == '4':
            break
        else:
            print("Invalid input. Try again.")

           
#Structuring the Analysis Menu
def analysis_menu():
    while True:
        print("\n" + "-"*15)
        print("Analysis Menu")
        print("-"*15)
        print("1. Display Data")
        print("2. Top Records")
        print("3. Statistics")
        print("4. Back")
        opt = input("Your choice: ").strip()
        if opt == '1':
            print(df.head(10))
        elif opt == '2':
            try:
                n = int(input("Enter number of top records: "))
                print(df.nlargest(n, 'Users Millions'))
            except ValueError:
                print("Please enter a valid number.")
        elif opt == '3':
            print(df.describe())
        elif opt == '4':
            break
        else:
            print("Invalid input. Try again.")
            
#Structuring the Manipulation Menu
def manipulation_menu():
    while True:
        print("\n" + "-"*25)
        print("Data Manipulation Menu")
        print("-"*25)
        print("1. Filter by Country")
        print("2. Filter by Year Range")
        print("3. Add Growth Rate Column")
        print("4. Remove Duplicates")
        print("5. Sort Data")
        print("6. Save Modified Data")
        print("7. Back")
        opt = input("Your choice: ").strip()
        if opt == '1':
            country = select_from_list(sorted(df['Country'].unique()), "Search country")
            filtered_df = df[df['Country'] == country]
            print(f"\nData for {country}:")
            print(filtered_df.head())
            globals()['current_df'] = filtered_df
        elif opt == '2':
            try:
                start_year = int(input("Start year: "))
                end_year = int(input("End year: "))
                filtered_df = df[(df['Year'] >= start_year) & (df['Year'] <= end_year)]
                print(f"\nData from {start_year}-{end_year}:")
                print(filtered_df.head())
                globals()['current_df'] = filtered_df
            except ValueError:
                print("Please enter valid years.")
        elif opt == '3':
            if 'current_df' in globals():
                df_work = globals()['current_df'].sort_values(['City', 'Country', 'Year'])
                df_work['Growth_Rate'] = df_work.groupby(['City', 'Country'])['Users Millions'].pct_change() * 100
                print("\nGrowth rate added:")
                print(df_work[['Country', 'City', 'Year', 'Users Millions', 'Growth_Rate']].head(10))
                globals()['current_df'] = df_work
            else:
                print("Please filter data first (options 1 or 2).")
        elif opt == '4':
            initial_len = len(df)
            df_clean = df.drop_duplicates()
            print(f"Removed {initial_len - len(df_clean)} duplicates.")
            globals()['current_df'] = df_clean
        elif opt == '5':
            col = input("Sort by column (Country/City/Year/Users Millions): ").strip().lower()
            #Defining the shortcuts or possible errors for the code to understand 
            col_mapping = {
                'country': 'Country',
                'count':'Country',
                'ci':'City',
                'city': 'City',
                'cit':'City',
                'ciy':'City',
                'year': 'Year',
                'yr':'Year',
                'users': 'Users Millions',
                'users millions': 'Users Millions',
                'user': 'Users Millions',
                'user million':'Users Millions',
                'million':'Users Millions',
            }
            if col in col_mapping:
                col = col_mapping[col]
            elif col.title() in df.columns:
                col = col.title()
            if col in df.columns:
                sorted_df = df.sort_values(col, ascending=False)
                print("\nTop 10 sorted records:")
                print(sorted_df.head(10))
                globals()['current_df'] = sorted_df
            else:
                print("Column not found.")
        elif opt == '6':
            if 'current_df' in globals():
                filename = input("Enter filename to save (e.g., modified_data.csv): ").strip()
                globals()['current_df'].to_csv(filename, index=False)
                print(f"Data saved to {filename}")
            else:
                print("No modified data to save. Filter first.")
        elif opt == '7':
            break
        else:
            print("Invalid input.")

#Plotting the Line graph
def plot_city_line_chart():
    country = select_from_list(sorted(df['Country'].unique()), "Search country")
    city_df = df[df['Country'] == country]
    city = select_from_list(sorted(city_df['City'].unique()), "Search city")
    data = city_df[city_df['City'] == city]
    plt.figure(figsize=(10, 6))
    plt.plot(data['Year'], data['Users Millions'], marker='o')
    plt.title(f"Mobile Phone Users in {city}, {country} (2010-2025)")
    plt.xlabel("Year")
    plt.ylabel("Users (Millions)")
    plt.grid(True)
    plt.xticks(data['Year'], rotation=45)
    plt.tight_layout()
    plt.show()

#Plotting the bar graph
def plot_city_bar_chart():
    country = select_from_list(sorted(df['Country'].unique()), "Search country")
    city_df = df[df['Country'] == country]
    city = select_from_list(sorted(city_df['City'].unique()), "Search city")
    data = city_df[city_df['City'] == city]
    plt.figure(figsize=(10, 6))
    plt.bar(data['Year'], data['Users Millions'])
    plt.title(f"Mobile Phone Users in {city}, {country} (2010-2025)")
    plt.xlabel("Year")
    plt.ylabel("Users (Millions)")
    plt.xticks(data['Year'], rotation=45)
    plt.tight_layout()
    plt.show()

#Plotting the graph to compare multiple cities
def compare_cities_line_chart():
    print("You can compare up to 5 cities.")
    n = 0
    max_cities = 5
    plt.figure(figsize=(12, 8))
    while n < max_cities:
        country = select_from_list(sorted(df['Country'].unique()), f"Search country for city {n+1}")
        city_df = df[df['Country'] == country]
        city = select_from_list(sorted(city_df['City'].unique()), f"Search city {n+1}")
        data = city_df[city_df['City'] == city]
        plt.plot(data['Year'], data['Users Millions'], marker='o', label=f"{city}, {country}")
        n += 1
        if n < max_cities:
            more = input("Add another city? (y/n): ").strip().lower()
            if more != 'y':
                break
    plt.title("Mobile Phone Users Comparison (2010-2025)")
    plt.xlabel("Year")
    plt.ylabel("Users (Millions)")
    plt.legend()
    plt.grid(True)
    plt.xticks(df['Year'].unique(), rotation=45)
    plt.tight_layout()
    plt.show()

#Running the code
if __name__ == "__main__":
    main_menu()
