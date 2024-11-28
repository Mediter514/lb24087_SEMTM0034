from hatchery import Hatchery  # Import the Hatchery class
from fish_species import FishSpecies  # Import the FishSpecies class
from utils import prompt_integer_range  # Import prompt_integer_range function
from utils import prompt_integer  # Import prompt_integer function
from supply import Supply  # Import the Supply class
from vendor import Vendors  # Import the Vendors class

def main():
    # Initialize the hatchery with an initial cash balance of 10,000
    hatchery = Hatchery(initial_cash=10000)

    # Add fish species information to the hatchery with fixed quarterly sales volume (adjustable based on demand)
    hatchery.species.extend([
        FishSpecies("Clef Fins", 0.1, 12000, 2000, 2.0, 250, demand=25),  # Fish species 1
        FishSpecies("Timpani Snapper", 0.05, 9000, 2000, 1.0, 350, demand=10),  # Fish species 2
        FishSpecies("Andalusian Brim", 0.09, 6000, 2000, 0.5, 250, demand=15),  # Fish species 3
        FishSpecies("Plagal Cod", 0.1, 10000, 2000, 2.0, 400, demand=20),  # Fish species 4
        FishSpecies("Fugue Flounder", 0.2, 12000, 2000, 2.5, 550, demand=30),  # Fish species 5
        FishSpecies("Modal Bass", 0.3, 12000, 6000, 3.0, 500, demand=50),  # Fish species 6
    ])

    # Add supplies to the hatchery
    hatchery.supplies.extend([
        Supply("Fertiliser", 20, 10, 0.4, 0.10),  # Supply 1
        Supply("Feed", 400000, 200000, 0.1, 0.001),  # Supply 2
        Supply("Salt", 200000, 100000, 0.0, 0.001)  # Supply 3
    ])

    # Initialize vendor information
    hatchery.vendors.extend([
        Vendors("Slippery Lakes", 0.30, 0.0001, 0.00005),
        Vendors("Scaly Wholesaler", 0.20, 0.0004, 0.00025)
    ])

    # Simulate multiple quarters
    quarters = prompt_integer("Please enter number of quarters: ")  # Prompt user to enter the number of quarters for simulation

    # Initialize remaining cash with the starting balance of 10,000
    remaining_cash = hatchery.cash

    for q in range(1, quarters + 1):  # Loop through each quarter
        print(f"\n=== Quarter {q} ===")  # Print the current quarter

        if q > 1:  # From the second quarter onwards, update the remaining cash to the previous quarter's balance
            hatchery.set_cash(remaining_cash)

        # Add technicians
        tech_change = prompt_integer_range("Enter number of technicians: ", min_value=-5, max_value=5)
        if tech_change > 0:
            for _ in range(tech_change):
                name = input(f"Enter the name of Technician {_ + 1} for quarter {q}: ")
                specialty = input(f"Does {name} have a specialty? (yes=1/no=0): ").lower()
                specialty_fish = None
                if specialty == "1":
                    specialty_fish = input(f"Enter the fish type {name} specializes in: ")
                weekly_rate = 500
                hatchery.add_technician(name, weekly_rate, specialty_fish)
                print(f"Hired {name}, weekly rate={weekly_rate}, specialty={specialty_fish} in quarter {q}")
        elif tech_change < 0:
            for _ in range(abs(tech_change)):
                if hatchery.technicians:
                    removed_technician = hatchery.technicians.pop()
                    print(f"Removed technician {removed_technician.name} in quarter {q}")
                else:
                    print(f"No technicians left to remove in quarter {q}.")
        else:
            print(f"No change in technician count for quarter {q}.")

        # Sales section
        hatchery.sell_fish()  # Execute fish sales
        hatchery.calculate_and_print_expenses()  # Calculate and print the expenses

        # Calculate remaining cash after expenses
        remaining_cash = hatchery.calculate_cash_after_expenses()
        print(f"Remaining cash after quarter {q}: {remaining_cash:.2f}")

        if remaining_cash < 0:  # Check for bankruptcy
            print(f"\nHatchery has gone bankrupt in quarter {q} due to insufficient funds!")
            break

    print("\nSimulation complete!")  # End of simulation

if __name__ == "__main__":
    # Program entry point, calls the main function
    main()


