class Computer:
    # attributes
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    def __init__(self, description: str,
                 processor_type: str,
                 hard_drive_capacity: int,
                 memory: int,
                 operating_system: str,
                 year_made: int,
                 price: int) -> None:
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    # What methods will you need?
    def display(self):
        print(f"-" * 2, "New display starts for computer", self.description, "_" * 2)
        print(self.description, self.processor_type, self.hard_drive_capacity,
              self.memory, self.operating_system, self.year_made, self.price)

    # Method for updating the price of a computer
    def update_price(self, new_price: int):
        # Add an option in the resale shop class to check the item id entered then call update_price option while passing new price in as a float, Else an error message is thrown in resale shop
        self.price = new_price
    def updateos(self, new_operating_system: str):
        if new_operating_system != None:
            self.operating_system = new_operating_system
        else:
            print(f"\nOperating system not specified. There was no updating")
