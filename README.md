## PART 1

# Software Development

This program simulates the operation of a fish hatchery, managing various aspects such as fish species, technician wages, inventory (supplies), and purchasing materials from vendors. It handles quarterly operations, fish sales, material consumption, and updates the hatchery's cash balance based on various expenses.

## Table of Contents
- [Overview](#overview)
- [Class Definitions](#class-definitions)
  - [Technician](#technician)
  - [Vendor](#vendor)
  - [Supply](#supply)
  - [FishSpecies](#fishspecies)
  - [Hatchery](#hatchery)
- [Usage](#usage)
- [Requirements](#requirements)
- [License](#license)

## Overview

This program simulates the financial and operational tasks of a fish hatchery over multiple quarters. Users can add technicians, specialties, fish species, supplies, and vendors. Users can manage inventory, sell fish, purchase materials from vendors, and calculate wages, supply costs, and other expenses. The program ensures smooth operation of the hatchery by updating the cash balance and tracking material usage.

### Features:
- Simulate quarterly fish sales based on fish species demand.
- Technician management, including wage calculation.
- Supply management, including depreciation of fertilizer, feed, and salt.
- Vendor management for material purchases.
- Check material and labor requirements to ensure sufficient resources for operations.
- Calculate various expenses, including wages, rent/utilities, material costs, and storage costs.

## Class Definitions

### Technician
The `Technician` class represents a technician at the hatchery. Each technician has a name, a weekly wage, and a specialty, with their quarterly wage calculated based on their weekly rate.

**Attributes:**
- `name`: The technician's name.
- `weekly_rate`: The technician's weekly wage.
- `specialty`: The technician's area of expertise.

**Methods:**
- `get_salary()`: Returns the technician's quarterly wage (calculated as `weekly_rate * 12`).
- `__str__()`: Returns the technician's name.

### Vendor
The `Vendor` class represents a vendor that provides various materials required by the hatchery, such as fertilizer, feed, and salt.

**Attributes:**
- `name`: The vendor's name.
- `fertilizers_price`: Price per unit of fertilizer (per liter).
- `feed_price`: Price per unit of feed (per gram).
- `salt_price`: Price per unit of salt (per gram).

### Supply
The `Supply` class represents supplies in the hatchery, such as fertilizer, feed, and salt. Each supply has a capacity, depreciation, and unit cost.

**Attributes:**
- `name`: The name of the supply.
- `main_capacity`: Main inventory capacity.
- `aux_capacity`: Auxiliary inventory capacity.
- `depreciation`: Depreciation per quarter.
- `cost_per_unit`: The cost per unit of supply.

**Methods:**
- `calculate_cost()`: Calculates the total cost of supplies based on the main inventory capacity.
- `update_capacity()`: Updates the inventory capacity considering depreciation.

### FishSpecies
The `FishSpecies` class represents the fish species in the hatchery. It includes information about the species' costs, maintenance time, sales price, and supply requirements.

**Attributes:**
- `name`: The name of the fish species.
- `fertilizer_cost`: The cost of fertilizer for the species.
- `feed_cost`: The cost of feed for the species.
- `salt_cost`: The cost of salt for the species.
- `maintenance_time`: Time required to maintain the species.
- `price`: Sales price of the species.
- `demand`: The quantity of fish species to be sold each quarter.

**Methods:**
- `get_cost()`: Returns the total cost of maintaining the species (sum of fertilizer, feed, and salt costs).
- `get_price()`: Returns the sales price of the species.
- `__str__()`: Returns the name of the fish species.

### Hatchery
The `Hatchery` class is the main class that manages the operations of the hatchery. It tracks cash, technicians, fish species, supplies, and vendors. It simulates the fish sales process, inventory management, and financial calculations.

**Attributes:**
- `cash`: The hatchery's current cash balance.
- `technicians`: List of technicians at the hatchery.
- `species`: List of fish species available for sale.
- `supplies`: List of supplies such as fertilizer, feed, and salt.
- `vendors`: List of vendors providing materials for the hatchery.
- `total_revenue`: Total revenue from fish sales.
- `total_expense`: Total cost of purchased materials.
- `total_expenses`: Total expenses including technician wages, rent/utilities, supply costs, etc.
- `total_warehouse_cost`: Cost of warehouse maintenance.

**Methods:**
- `set_cash(amount)`: Sets the hatchery's cash balance.
- `add_supply(supply)`: Adds a supply to the hatchery's inventory.
- `update_supplies()`: Updates the supply inventory, considering depreciation.
- `add_technician(name, weekly_rate, specialty=None)`: Adds a technician to the hatchery.
- `sell_fish()`: Simulates fish sales and updates finances based on available labor and materials.
- `calculate_and_print_expenses()`: Calculates and prints the quarterly expenses.
- `calculate_cash_after_expenses()`: Calculates remaining cash after all expenses are deducted.

## Usage

To run the simulation program, follow these steps:

1. **Set up the hatchery**: Create a new `Hatchery` instance and set an initial cash balance.
2. **Add technicians**: Use the `add_technician()` method to hire technicians.
3. **Add fish species**: Create `FishSpecies` instances and add them to the hatchery's fish species list.
4. **Add supplies**: Create `Supply` instances (e.g., fertilizer, feed, salt) and add them to the hatchery's inventory.
5. **Add vendors**: Create `Vendor` instances and add them to the hatchery's vendor list.
6. **Run the simulation**: Use methods such as `sell_fish()` and `calculate_and_print_expenses()` to simulate a quarter's operations.

## Example Run

Please enter number of quarters: 8

=== Quarter 1 ===
Enter number of technicians: 2
Enter the name of Technician 1 for quarter 1: James
Does James have a specialty? (yes=1/no=0): 1
Enter the fish type James specializes in: Clef Fins
Hired James, weekly rate=500, specialty=Clef Fins in quarter 1
Enter the name of Technician 2 for quarter 1: Richard
Does Richard have a specialty? (yes=1/no=0): 0
Hired Richard, weekly rate=500, specialty=None in quarter 1

=== Sales situation ===
Fish Clef Fins, demand 25, sell 25: 25
Fish Timpani Snapper, demand 10, sell 10: 10
Fish Andalusian Brim, demand 15, sell 15: 15
Insufficient ingredients:
 Fertiliser need 2.0 storage 25.65
 Feed need 200000.0 storage 120000.00
 Salt need 40000.0 storage 200000.00
Fish Plagal Cod, demand 20, sell 20: 0
Fish Fugue Flounder, demand 30, sell 30: 0
Fish Modal Bass, demand 50, sell 50: 0

=== Sales Summary ===
Total revenue from fish sales: 13500.00

=== Updated Materials Inventory ===
Material Fertiliser warehouse cost: 2.56
Material Feed warehouse cost: 120.00
Material Salt warehouse cost: 200.00

=== List of Vendors ===
1. Slippery Lakes
Fertiliser: £0.3/litre
Feed: £0.0001/g
Salt: £5e-05/g
2. Scaly Wholesaler
Fertiliser: £0.2/litre
Feed: £0.0004/g
Salt: £0.00025/g
>>> Enter number of vendor to purchase from: 1

Selected Vendor: Slippery Lakes
Expense for Fertiliser: £4.50 (Purchase amount: 15.0)
Expense for Feed: £49.20 (Purchase amount: 492000.0)
Expense for Salt: £5.00 (Purchase amount: 100000.0)

Total expenses for materials: £58.70

=== Quarterly Expenses ===
Paid James, weekly rate=500 amount 6000.00
Paid Richard, weekly rate=500 amount 6000.00
Paid rent/utilities 1500.00
Total quarterly expenses: 13500.00
Remaining cash after quarter 1: 9618.73

=== Quarter 2 ===
Enter number of technicians: -1
Removed technician Richard in quarter 2

=== Sales situation ===
Fish Clef Fins, demand 25, sell 25: 25
Fish Timpani Snapper, demand 10, sell 10: 10
Fish Andalusian Brim, demand 15, sell 15: 15
Insufficient labour: required 8.00, available 2.17
Fish Plagal Cod, demand 20, sell 20: 0
Fish Fugue Flounder, demand 30, sell 30: 0
Fish Modal Bass, demand 50, sell 50: 0

=== Sales Summary ===
Total revenue from fish sales: 13500.00

=== Updated Materials Inventory ===
Material Fertiliser warehouse cost: 2.56
Material Feed warehouse cost: 120.00
Material Salt warehouse cost: 200.00

=== List of Vendors ===
1. Slippery Lakes
Fertiliser: £0.3/litre
Feed: £0.0001/g
Salt: £5e-05/g
2. Scaly Wholesaler
Fertiliser: £0.2/litre
Feed: £0.0004/g
Salt: £0.00025/g
>>> Enter number of vendor to purchase from: 1

Selected Vendor: Slippery Lakes
Expense for Fertiliser: £4.50 (Purchase amount: 15.0)
Expense for Feed: £49.20 (Purchase amount: 492000.0)
Expense for Salt: £5.00 (Purchase amount: 100000.0)

Total expenses for materials: £58.70

=== Quarterly Expenses ===
Paid James, weekly rate=500 amount 6000.00
Paid rent/utilities 1500.00
Total quarterly expenses: 7500.00
Remaining cash after quarter 2: 15237.47

=== Quarter 3 ===
Enter number of technicians: 0
No change in technician count for quarter 3.

=== Sales situation ===
Fish Clef Fins, demand 25, sell 25: 25
Fish Timpani Snapper, demand 10, sell 10: 10
Fish Andalusian Brim, demand 15, sell 15: 15
Insufficient labour: required 8.00, available 2.17
Fish Plagal Cod, demand 20, sell 20: 0
Fish Fugue Flounder, demand 30, sell 30: 0
Fish Modal Bass, demand 50, sell 50: 0

=== Sales Summary ===
Total revenue from fish sales: 13500.00

=== Updated Materials Inventory ===
Material Fertiliser warehouse cost: 2.56
Material Feed warehouse cost: 120.00
Material Salt warehouse cost: 200.00

=== List of Vendors ===
1. Slippery Lakes
Fertiliser: £0.3/litre
Feed: £0.0001/g
Salt: £5e-05/g
2. Scaly Wholesaler
Fertiliser: £0.2/litre
Feed: £0.0004/g
Salt: £0.00025/g
>>> Enter number of vendor to purchase from: 1

Selected Vendor: Slippery Lakes
Expense for Fertiliser: £4.50 (Purchase amount: 15.0)
Expense for Feed: £49.20 (Purchase amount: 492000.0)
Expense for Salt: £5.00 (Purchase amount: 100000.0)

Total expenses for materials: £58.70

=== Quarterly Expenses ===
Paid James, weekly rate=500 amount 6000.00
Paid rent/utilities 1500.00
Total quarterly expenses: 7500.00
Remaining cash after quarter 3: 20856.21

=== Quarter 4 ===
Enter number of technicians: 2
Enter the name of Technician 1 for quarter 4: Richard
Does Richard have a specialty? (yes=1/no=0): 0
Hired Richard, weekly rate=500, specialty=None in quarter 4
Enter the name of Technician 2 for quarter 4: Lee
Does Lee have a specialty? (yes=1/no=0): 0
Hired Lee, weekly rate=500, specialty=None in quarter 4

=== Sales situation ===
Fish Clef Fins, demand 25, sell 25: 25
Fish Timpani Snapper, demand 10, sell 10: 10
Fish Andalusian Brim, demand 15, sell 15: 15
Insufficient ingredients:
 Fertiliser need 2.0 storage 25.65
 Feed need 200000.0 storage 120000.00
 Salt need 40000.0 storage 200000.00
Fish Plagal Cod, demand 20, sell 20: 0
Fish Fugue Flounder, demand 30, sell 30: 0
Fish Modal Bass, demand 50, sell 50: 0

=== Sales Summary ===
Total revenue from fish sales: 13500.00

=== Updated Materials Inventory ===
Material Fertiliser warehouse cost: 2.56
Material Feed warehouse cost: 120.00
Material Salt warehouse cost: 200.00

=== List of Vendors ===
1. Slippery Lakes
Fertiliser: £0.3/litre
Feed: £0.0001/g
Salt: £5e-05/g
2. Scaly Wholesaler
Fertiliser: £0.2/litre
Feed: £0.0004/g
Salt: £0.00025/g
>>> Enter number of vendor to purchase from: 1

Selected Vendor: Slippery Lakes
Expense for Fertiliser: £4.50 (Purchase amount: 15.0)
Expense for Feed: £49.20 (Purchase amount: 492000.0)
Expense for Salt: £5.00 (Purchase amount: 100000.0)

Total expenses for materials: £58.70

=== Quarterly Expenses ===
Paid James, weekly rate=500 amount 6000.00
Paid Richard, weekly rate=500 amount 6000.00
Paid Lee, weekly rate=500 amount 6000.00
Paid rent/utilities 1500.00
Total quarterly expenses: 19500.00
Remaining cash after quarter 4: 14474.94

=== Quarter 5 ===
Enter number of technicians: 0
No change in technician count for quarter 5.

=== Sales situation ===
Fish Clef Fins, demand 25, sell 25: 25
Fish Timpani Snapper, demand 10, sell 10: 10
Fish Andalusian Brim, demand 15, sell 15: 15
Insufficient ingredients:
 Fertiliser need 2.0 storage 25.65
 Feed need 200000.0 storage 120000.00
 Salt need 40000.0 storage 200000.00
Fish Plagal Cod, demand 20, sell 20: 0
Fish Fugue Flounder, demand 30, sell 30: 0
Fish Modal Bass, demand 50, sell 50: 0

=== Sales Summary ===
Total revenue from fish sales: 13500.00

=== Updated Materials Inventory ===
Material Fertiliser warehouse cost: 2.56
Material Feed warehouse cost: 120.00
Material Salt warehouse cost: 200.00

=== List of Vendors ===
1. Slippery Lakes
Fertiliser: £0.3/litre
Feed: £0.0001/g
Salt: £5e-05/g
2. Scaly Wholesaler
Fertiliser: £0.2/litre
Feed: £0.0004/g
Salt: £0.00025/g
>>> Enter number of vendor to purchase from: 1

Selected Vendor: Slippery Lakes
Expense for Fertiliser: £4.50 (Purchase amount: 15.0)
Expense for Feed: £49.20 (Purchase amount: 492000.0)
Expense for Salt: £5.00 (Purchase amount: 100000.0)

Total expenses for materials: £58.70

=== Quarterly Expenses ===
Paid James, weekly rate=500 amount 6000.00
Paid Richard, weekly rate=500 amount 6000.00
Paid Lee, weekly rate=500 amount 6000.00
Paid rent/utilities 1500.00
Total quarterly expenses: 19500.00
Remaining cash after quarter 5: 8093.68

=== Quarter 6 ===
Enter number of technicians: 0
No change in technician count for quarter 6.

=== Sales situation ===
Fish Clef Fins, demand 25, sell 25: 25
Fish Timpani Snapper, demand 10, sell 10: 10
Fish Andalusian Brim, demand 15, sell 15: 15
Insufficient ingredients:
 Fertiliser need 2.0 storage 25.65
 Feed need 200000.0 storage 120000.00
 Salt need 40000.0 storage 200000.00
Fish Plagal Cod, demand 20, sell 20: 0
Fish Fugue Flounder, demand 30, sell 30: 0
Fish Modal Bass, demand 50, sell 50: 0

=== Sales Summary ===
Total revenue from fish sales: 13500.00

=== Updated Materials Inventory ===
Material Fertiliser warehouse cost: 2.56
Material Feed warehouse cost: 120.00
Material Salt warehouse cost: 200.00

=== List of Vendors ===
1. Slippery Lakes
Fertiliser: £0.3/litre
Feed: £0.0001/g
Salt: £5e-05/g
2. Scaly Wholesaler
Fertiliser: £0.2/litre
Feed: £0.0004/g
Salt: £0.00025/g
>>> Enter number of vendor to purchase from: 1

Selected Vendor: Slippery Lakes
Expense for Fertiliser: £4.50 (Purchase amount: 15.0)
Expense for Feed: £49.20 (Purchase amount: 492000.0)
Expense for Salt: £5.00 (Purchase amount: 100000.0)

Total expenses for materials: £58.70

=== Quarterly Expenses ===
Paid James, weekly rate=500 amount 6000.00
Paid Richard, weekly rate=500 amount 6000.00
Paid Lee, weekly rate=500 amount 6000.00
Paid rent/utilities 1500.00
Total quarterly expenses: 19500.00
Remaining cash after quarter 6: 1712.41

=== Quarter 7 ===
Enter number of technicians: 0
No change in technician count for quarter 7.

=== Sales situation ===
Fish Clef Fins, demand 25, sell 25: 25
Fish Timpani Snapper, demand 10, sell 10: 10
Fish Andalusian Brim, demand 15, sell 15: 15
Insufficient ingredients:
 Fertiliser need 2.0 storage 25.65
 Feed need 200000.0 storage 120000.00
 Salt need 40000.0 storage 200000.00
Fish Plagal Cod, demand 20, sell 20: 0
Fish Fugue Flounder, demand 30, sell 30: 0
Fish Modal Bass, demand 50, sell 50: 0

=== Sales Summary ===
Total revenue from fish sales: 13500.00

=== Updated Materials Inventory ===
Material Fertiliser warehouse cost: 2.56
Material Feed warehouse cost: 120.00
Material Salt warehouse cost: 200.00

=== List of Vendors ===
1. Slippery Lakes
Fertiliser: £0.3/litre
Feed: £0.0001/g
Salt: £5e-05/g
2. Scaly Wholesaler
Fertiliser: £0.2/litre
Feed: £0.0004/g
Salt: £0.00025/g
>>> Enter number of vendor to purchase from: 1

Selected Vendor: Slippery Lakes
Expense for Fertiliser: £4.50 (Purchase amount: 15.0)
Expense for Feed: £49.20 (Purchase amount: 492000.0)
Expense for Salt: £5.00 (Purchase amount: 100000.0)

Total expenses for materials: £58.70

=== Quarterly Expenses ===
Paid James, weekly rate=500 amount 6000.00
Paid Richard, weekly rate=500 amount 6000.00
Paid Lee, weekly rate=500 amount 6000.00
Paid rent/utilities 1500.00
Total quarterly expenses: 19500.00
Remaining cash after quarter 7: -4668.85

Hatchery has gone bankrupt in quarter 7 due to insufficient funds!

Simulation complete!

## Requirements
- Python 3.x
- No external libraries required

## License
This project is licensed under the MIT License.




## PART 2

# Data Analytics

This project provides an analysis of datasets fetched from Kaggle, including their views, upvotes, and other attributes. The data is processed, visualized, and analyzed for correlations and linear relationships.

## Project Structure

1. **Kaggle API Integration**: 
   - The code fetches datasets from Kaggle using the Kaggle API, retrieves details such as views, upvotes, and other metadata, and stores this information into a DataFrame.

2. **Data Collection**:
   - The project retrieves a list of datasets using the Kaggle API and stores information like dataset name, ID, description, tags, views, upvotes, file size, upload time, author, license, and file types.

3. **Data Preprocessing**:
   - The data is cleaned by removing irrelevant or empty fields. Datasets are limited to the top 200 based on the number of upvotes.

4. **Popularity Score**:
   - A new column, `popularity_score`, is created using a weighted combination of views (60%) and upvotes (40%). This score is then used for further analysis.

5. **Data Exploration**:
   - **Statistical Summary**: The summary statistics of the datasets are displayed.
   - **Visualization**: 
     - A histogram showing the distribution of views.
     - A scatter plot of views vs upvotes.
     - A linear regression analysis between dataset age (ID) and views/upvotes.
     - Correlation between views and upvotes.
     - A visualization showing the relationship between dataset age and views/upvotes.

6. **Linear Regression Analysis**:
   - Linear regression is used to model the relationship between dataset age (represented by ID) and both views and upvotes.

7. **Output**:
   - The results are saved into a CSV file (`top_200_datasets_info_with_scores.csv`) containing the dataset information and popularity scores.
   - The results of the linear regression models, including coefficients and intercepts, are printed.

---

## Requirements

- Python 3.x
- Required libraries:
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `scikit-learn`
  - `kaggle` (for Kaggle API access)

To install the necessary dependencies, run the following:

```bash
pip install pandas matplotlib seaborn scikit-learn kaggle
```

## Setup

1. **Kaggle API Setup**:
   - You must have a Kaggle account and generate your API credentials.
   - Set the environment variables for your Kaggle username and key:

   ```python
   os.environ['KAGGLE_USERNAME'] = 'your_kaggle_username'
   os.environ['KAGGLE_KEY'] = 'your_kaggle_key'
   ```

2. **Running the Script**:
   - Once you've set up the Kaggle API credentials, you can run the script to fetch and analyze the datasets.
   - The script will retrieve datasets, process the data, perform analysis, and generate visualizations.

---

## Steps in the Code

### 1. Kaggle API Authentication

The script starts by authenticating with Kaggle using your API credentials.

### 2. Fetching Dataset Information

The script uses Kaggle’s API to fetch datasets, starting from the most upvoted ones, and stores various metadata for each dataset.

### 3. Data Preprocessing and Filtering

The datasets are cleaned, removing irrelevant fields. The top 200 datasets are selected based on the upvote count.

### 4. Popularity Score Calculation

A weighted popularity score is calculated based on the views and upvotes of each dataset.

### 5. Data Exploration

- Statistical summaries and visualizations are provided, such as distributions of views and upvotes.
- Scatter plots and linear regression are used to analyze the relationship between views, upvotes, and dataset age (represented by ID).

### 6. Output

The script saves the dataset information, including the popularity score, to a CSV file and prints the results of the regression models.

---

## Example Output

- **CSV File**: The resulting dataset information, including popularity scores, is saved to `top_200_datasets_info_with_scores.csv`.
- **Printed Results**: The regression model coefficients and intercepts, as well as the correlation between views and upvotes, are printed in the console.

---

## License

This project is licensed under the MIT License.



