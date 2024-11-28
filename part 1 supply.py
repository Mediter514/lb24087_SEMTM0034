class Supply:
    def __init__(self, name, main_capacity, aux_capacity, depreciation, cost_per_unit):
        self.name = name  # Name of the supply item
        self.main_capacity = main_capacity  # Main capacity of the supply
        self.aux_capacity = aux_capacity  # Auxiliary capacity of the supply
        self.depreciation = depreciation  # Depreciation per quarter
        self.cost_per_unit = cost_per_unit  # Cost per unit of the supply

    def calculate_cost(self):
        # Calculate the cost, assuming the full main_capacity is used each quarter
        return self.main_capacity * self.cost_per_unit

    def update_capacity(self):
        # Update the main capacity considering depreciation
        self.main_capacity -= self.depreciation
        if self.main_capacity < 0:  # Ensure the capacity doesn't go below zero
            self.main_capacity = 0
