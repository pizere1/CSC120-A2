class Computer:
 #attributes
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
    
    def __init__(self, description: str, processor_type: str, hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, price: int)->None:
        self.description=description
        self.processor_type=processor_type
        self.hard_drive_capacity=hard_drive_capacity
        self.memory=memory
        self.operating_system=operating_system
        self.year_made=year_made
        self.price=price
    # The class constructor
    def display(self):
        print (self.description, self.processor_type, self.hard_drive_capacity, self.memory, self.operating_system, self.year_made, self.price)
        
    #Method for updating the price of a computer after resale_shop class checks whether the item is in inventory
    def update_price(self):
            new_price=int(input("Enter a new price"))
            self.price=new_price
            
    #updates the os once called by resale_shop class which checks whether the item is inventory
    def update_os(self):
            new_operating_system=str(input("Enter the new os"))
            self.operating_system=new_operating_system
def main():
    Mac:Computer = Computer("Mac Pro (Late 2013)","3.5 GHc 6-Core Intel Xeon E5",1024, 64,"macOS Big Sur", 2013, 1500)
    Mac.display()
    Mac.update_price()
    Mac.update_os()
    Mac.display()
main()
