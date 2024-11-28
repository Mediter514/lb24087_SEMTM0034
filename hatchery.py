# Import Technician class from technician module
from technician import Technician

class Hatchery:
    def __init__(self, initial_cash):
        self.cash = initial_cash  # Current cash balance
        self.technicians = []  # List of technicians
        self.species = []  # List of fish species
        self.supplies = []  # List of supplies
        self.vendors = []  # List of vendors
        self.total_revenue = 0  # Total revenue
        self.total_expense = 0  # Total expense
        self.total_expenses = 0  # Fixed expenses
        self.total_warehouse_cost = 0  # Warehouse costs
        self.cash = initial_cash  # Initialize cash

    def set_cash(self, amount):
        self.cash = amount  # Set the cash balance

    def add_supply(self, supply):
        self.supplies.append(supply)  # Add a new supply

    def update_supplies(self):
        for supply in self.supplies:
            supply.update_capacity()  # Update supply capacity considering depreciation

    # New method to add a technician
    def add_technician(self, name, weekly_rate, specialty=None):
        technician = Technician(name, weekly_rate, specialty)  # Create a technician
        self.technicians.append(technician)  # Add technician to the list

    def sell_fish(self):
        # Calculate total labor available
        total_labour_available = len(self.technicians) * 9  # Assume each technician works 9 weeks per quarter

        # Calculate total supply available
        total_supply_available = {
            supply.name: supply.main_capacity + supply.aux_capacity for supply in self.supplies
        }

        self.total_revenue = 0  # Reset total revenue
        insufficient_reported = False  # Flag for insufficient resources

        print("\n=== Sales situation ===")
        for fish in self.species:
            if not insufficient_reported:
                # Calculate labor needed
                labour_needed = (fish.demand * fish.maintenance_time) / 5

                # Find specialized technicians
                specialized_technicians = [tech for tech in self.technicians if tech.specialty == fish.name]

                # If there are specialized technicians, adjust labor need
                if specialized_technicians:
                    labour_needed /= 3  # Reduce labor needed by a factor of 3 for specialized technicians

                # Check if there is enough labor
                if total_labour_available < labour_needed:
                    print(f"Insufficient labour: required {labour_needed:.2f}, available {total_labour_available:.2f}")
                    actual_sold = 0
                    insufficient_reported = True
                else:
                    # Calculate material needs
                    total_material_needed = {
                        name: fish.demand * amount for name, amount in fish.supply_needs.items()
                    }

                    # Prepare material needs and storage information
                    materials_info = []
                    for name, needed in total_material_needed.items():
                        storage = total_supply_available.get(name, 0)
                        materials_info.append(f" {name} need {needed:.1f} storage {storage:.2f}")

                    # Check for material shortages
                    if any(total_supply_available.get(name, 0) < needed for name, needed in
                           total_material_needed.items()):
                        print("Insufficient ingredients:" + "\n" + "\n".join(materials_info))
                        actual_sold = 0
                        insufficient_reported = True
                    else:
                        # If labor and materials are sufficient, proceed with sales
                        actual_sold = fish.demand
                        for name, needed in total_material_needed.items():
                            total_supply_available[name] -= needed  # Update material inventory
                        total_labour_available -= labour_needed  # Update labor available

                        # Calculate revenue from fish sales
                        revenue = fish.demand * fish.price
                        self.total_revenue += revenue  # Add to total revenue

            else:
                # If there was a shortage before, subsequent fish sales are 0
                actual_sold = 0

            # Print the sales information for the current fish
            print(f"Fish {fish.name}, demand {fish.demand}, sell {fish.demand}: {actual_sold}")

        # Print total revenue and current cash balance after sales
        print(f"\n=== Sales Summary ===")
        print(f"Total revenue from fish sales: {self.total_revenue:.2f}")

        # Print updated material inventory
        print("\n=== Updated Materials Inventory ===")

        # Calculate warehouse costs
        self.total_warehouse_cost = 0
        total_warehouse_remaining = 0

        for supply in self.supplies:
            remaining = total_supply_available.get(supply.name, 0)
            supply_cost = remaining * supply.cost_per_unit
            self.total_warehouse_cost += supply_cost  # Add to warehouse cost

            # Calculate remaining stock after depreciation
            remaining_after_depreciation = round(remaining * (1 - supply.depreciation), 0)
            total_warehouse_remaining += remaining_after_depreciation

            # Print individual supply's warehouse cost
            print(f"Material {supply.name} warehouse cost: {supply_cost:.2f}")

        # Check if there are any vendors available
        if not self.vendors:
            print("No vendors available. Please add vendors before selling fish.")
            return

        # Vendor selection logic
        print("\n=== List of Vendors ===")
        for i, vendor in enumerate(self.vendors, start=1):
            print(f"{i}. {vendor.name}")
            print(f"Fertiliser: £{vendor.fertilisers_price}/litre")
            print(f"Feed: £{vendor.feed_price}/g")
            print(f"Salt: £{vendor.salt_price}/g")

        choice = -1
        while choice not in range(1, len(self.vendors) + 1):
            try:
                choice = int(input(">>> Enter number of vendor to purchase from: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        selected_vendor = self.vendors[choice - 1]  # Select the vendor
        print(f"\nSelected Vendor: {selected_vendor.name}")

        # Calculate total expense for materials
        self.total_expense = 0

        for supply in self.supplies:
            # Calculate amount to purchase: inventory capacity minus remaining stock after depreciation
            remaining_after_depreciation = round(
                (total_supply_available.get(supply.name, 0) * (1 - supply.depreciation)), 0
            )
            purchase_amount = max(0, supply.main_capacity + supply.aux_capacity - remaining_after_depreciation)

            # Default expense value
            expense = 0  # Ensure expense is initialized even if nothing needs to be purchased

            # If purchase is needed, calculate the expense
            if purchase_amount > 0:
                if supply.name == "Fertiliser":
                    expense = purchase_amount * selected_vendor.fertilisers_price
                elif supply.name == "Feed":
                    expense = purchase_amount * selected_vendor.feed_price
                elif supply.name == "Salt":
                    expense = purchase_amount * selected_vendor.salt_price

                self.total_expense += expense  # Add to total expense
                print(f"Expense for {supply.name}: £{expense:.2f} (Purchase amount: {purchase_amount})")

        # Print total material expense
        print(f"\nTotal expenses for materials: £{self.total_expense:.2f}")

    def calculate_and_print_expenses(self):
        # Calculate and print technician wages and fixed expenses
        print("\n=== Quarterly Expenses ===")
        total_wages = 0
        for technician in self.technicians:
            quarterly_wage = technician.weekly_rate * 12  # Assuming 12 weeks per quarter
            total_wages += quarterly_wage
            print(f"Paid {technician.name}, weekly rate={technician.weekly_rate} amount {quarterly_wage:.2f}")

        # Fixed rent and utilities cost
        rent_utilities = 1500
        print(f"Paid rent/utilities {rent_utilities:.2f}")
        self.total_expenses = total_wages + rent_utilities  # Calculate total expenses
        print(f"Total quarterly expenses: {self.total_expenses:.2f}")

    def calculate_cash_after_expenses(self):
        # Calculate the remaining cash after all expenses
        return self.cash + self.total_revenue - self.total_expense - self.total_expenses - self.total_warehouse_cost
