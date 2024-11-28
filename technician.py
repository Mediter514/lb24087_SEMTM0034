class Technician:
    def __init__(self, name, weekly_rate, specialty=None):
        self.name = name  # Technician's name
        self.weekly_rate = weekly_rate  # Technician's weekly wage
        self.specialty = specialty  # Technician's specialty (optional)

    def get_salary(self):
        # Calculate salary for a quarter (12 weeks of work)
        return self.weekly_rate * 12

    def __str__(self):
        return self.name  # Return the name of the technician when printed
