# Mobile Phone Usage Trends Explorer

## Overview

Mobile Phone Usage Trends Explorer is a menu-based Python application that makes a contribution to providing the general public with an opportunity to explore trends in the number of mobile phone users (per country and city) using line/bar plots, summary displays, and simple data manipulation.

The program utilizes a CSV dataset that includes information about the country, city, year, and number of mobile phone users. The designated CSV file includes a column titled `Users (Millions)`; when read, the program stores this information under the label `Users Millions`.

## Features

The program allows the users to:

- view a line plot of mobile phone users for a selected city and country;
- view a bar plot of mobile phone users for a selected city and country;
- compare up to five cities using a line plot;
- see the first ten records, the records with the highest values, and descriptive statistics for the dataset;
- filter the dataset by country or year;
- calculate a year-over-year growth-rate column for the filtered data;
- remove duplicates or sort the records;
- save the modified data as a CSV file.

## Technologies and tools

- Python 3
- Pandas
- Matplotlib
- CSV files

## Project files

- `Final_Project.py` – the application;
- `final.csv` – the dataset, stored in the same folder as the application.

The CSV file should include the columns `Country`, `City`, `Year`, and a column of mobile phone users (can be labeled `Users (Millions)` or `Users Millions`).

## Installation and running

1. Make sure that Python 3 is installed on the computer.
2. Keep `Final_Project.py` and `final.csv` together in the project folder.
3. Create a virtual environment in the folder with the application:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   On Windows, step 3 should be:

   ```powershell
   .venv\Scripts\activate
   ```

4. Install the dependencies:

   ```bash
   python -m pip install pandas matplotlib
   ```

5. Launch the application:

   ```bash
   python Final_Project.py
   ```

The application looks for `final.csv` in the same folder as `Final_Project.py`. If you move the dataset elsewhere, update the `DATA_FILE` path in the application code.

## Testing instructions

Currently, there are no tests that check the code’s quality and stability. However, several simple tests can be done manually. After launching the application and seeing the Main Menu, one should:

1. make sure that all menus and submenus appear correctly;
2. select an incorrect option in any menu to make sure that the program prompts the user to select a correct option.

Then, test each section:

1. Line plot and Bar plot options: select a country and a city and make sure that the data is displayed correctly (with correct labels and values).
2. Compare cities: choose at least two cities to make sure that the legend displays their names and that the data is presented correctly.
3. Analyze the records display: check that the first ten records, the records with the highest values, and the descriptive statistics are displayed correctly.
4. Data manipulation: test filtering by country and year, calculating the growth rate, removing duplicates, and sorting.
5. Saving the changes: try saving the modified CSV data to a new file to check that everything is exported correctly (the new file should include all the columns and the correct data). To check that the application does not crash, one can run the following command:

   ```bash
   python -m py_compile Final_Project.py
   ```
