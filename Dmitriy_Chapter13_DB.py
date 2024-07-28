import sqlite3
import matplotlib.pyplot as plt

def create_database(db_name):
    """
    Create a SQLite database and a table named 'population'.
    """
    conn = sqlite3.connect(db_name)  # Connect to the SQLite database (or create it if it doesn't exist)
    cursor = conn.cursor()
    
    # Create the table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS population (
            city TEXT,
            year INTEGER,
            population INTEGER
        )
    ''')
    
    conn.commit()  # Commit the changes
    conn.close()   # Close the connection

def insert_initial_data(db_name):
    """
    Insert initial population data for 10 Florida cities for the year 2023.
    """
    # List of cities and their populations
    cities = [
        'Miami', 'Orlando', 'Tampa', 'Jacksonville', 'St. Petersburg',
        'Hialeah', 'Fort Lauderdale', 'Cape Coral', 'Palm Bay', 'Gainesville'
    ]
    populations = [
        470914, 307573, 416522, 949611, 267700,
        237069, 182595, 205599, 119760, 135417
    ]
    
    conn = sqlite3.connect(db_name)  # Connect to the SQLite database
    cursor = conn.cursor()
    
    # Insert data into the table
    for city, population in zip(cities, populations):
        cursor.execute('''
            INSERT INTO population (city, year, population) VALUES (?, ?, ?)
        ''', (city, 2023, population))
    
    conn.commit()  # Commit the changes
    conn.close()   # Close the connection

def simulate_growth(db_name):
    """
    Simulate population growth for the next 20 years at a 2% growth rate.
    """
    conn = sqlite3.connect(db_name)  # Connect to the SQLite database
    cursor = conn.cursor()
    
    # Retrieve distinct cities from the database
    cursor.execute('SELECT DISTINCT city FROM population')
    cities = cursor.fetchall()
    
    for city_tuple in cities:
        city = city_tuple[0]
        
        # Get the population for the city in 2023
        cursor.execute('SELECT population FROM population WHERE city = ? AND year = 2023', (city,))
        population = cursor.fetchone()[0]
        
        # Simulate growth for the next 20 years
        for year in range(2024, 2024 + 20):
            population *= 1.02  # Increase population by 2%
            cursor.execute('''
                INSERT INTO population (city, year, population) VALUES (?, ?, ?)
            ''', (city, year, int(population)))
    
    conn.commit()  # Commit the changes
    conn.close()   # Close the connection

def plot_population_growth(db_name, city_name):
    """
    Plot the population growth of a specified city over time.
    """
    conn = sqlite3.connect(db_name)  # Connect to the SQLite database
    cursor = conn.cursor()
    
    # Retrieve population data for the specified city
    cursor.execute('''
        SELECT year, population FROM population WHERE city = ?
    ''', (city_name,))
    
    data = cursor.fetchall()  # Fetch all the data
    conn.close()   # Close the connection
    
    # Extract years and populations
    years, populations = zip(*data)
    
    # Plot the data
    plt.figure(figsize=(10, 5))
    plt.plot(years, populations, marker='o')
    plt.title(f'Population Growth for {city_name}')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.grid(True)
    plt.show()

def main():
    """
    Main function to create the database, insert initial data, simulate growth, and plot results.
    """
    db_name = 'population_YOUR_INITIALS.db'  # Replace YOUR_INITIALS with your initials
    create_database(db_name)  # Create the database and table
    insert_initial_data(db_name)  # Insert initial data
    simulate_growth(db_name)  # Simulate population growth
    
    # List of cities for the user to choose from
    cities = [
        'Miami', 'Orlando', 'Tampa', 'Jacksonville', 'St. Petersburg',
        'Hialeah', 'Fort Lauderdale', 'Cape Coral', 'Palm Bay', 'Gainesville'
    ]
    
    # Display available cities
    print("Available cities:")
    for i, city in enumerate(cities, 1):
        print(f"{i}. {city}")
    
    # Get user choice
    choice = int(input("Enter the number corresponding to the city you want to see: "))
    selected_city = cities[choice - 1]
    
    # Plot the population growth for the selected city
    plot_population_growth(db_name, selected_city)

if __name__ == '__main__':
    main()
