class FishSpecies:

    def __init__(self, name, fertiliser_cost, feed_cost, salt_cost, maintenance_time, price, demand=0):
        self.name = name  # The name of the fish species
        self.fertiliser_cost = fertiliser_cost  # Cost of fertiliser
        self.feed_cost = feed_cost  # Cost of feed
        self.salt_cost = salt_cost  # Cost of salt
        self.maintenance_time = maintenance_time  # Maintenance time for the fish
        self.price = price  # Selling price of the fish
        self.demand = demand  # Fixed sales volume per quarter

        self.supply_needs = {
            "Fertiliser": fertiliser_cost,  # Assuming the fertiliser cost as the fertiliser need
            "Feed": feed_cost,  # Feed cost as the feed need
            "Salt": salt_cost  # Salt cost as the salt need
        }

    def get_cost(self):
        # Assuming the total cost of the fish is the sum of fertiliser, feed, and salt costs
        return self.fertiliser_cost + self.feed_cost + self.salt_cost

    def get_price(self):
        return self.price

    def __str__(self):
        return self.name  # String representation of the fish species (name)
