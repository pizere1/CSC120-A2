from Computer import Computer
from typing import Dict, Optional
class ResaleShop:
    #Attributes
    inventory: Dict[int, Dict] = {}
    global itemID

    def __init__(self) -> None:
        self.itemID = 0
        print("You created a new Resale Shop")
    #Function for adding a new item to the inventory with buy
    def buy(self, computer: Dict):
        self.itemID += 1  # increment itemID
        self.inventory[self.itemID] = computer
        print("Buying "+self.inventory[self.itemID].description)
        return self.itemID
    #Function for updating the price of a computer
    def update_price(self, item_id: int, new_price: int):
        if item_id in self.inventory:
            self.inventory[item_id].update_price(new_price)
        else:
            print("Item", item_id, "not found. Cannot update price.")
    #Function for selling an item and removing it from inventory
    def sell(self, item_id: int):
        if item_id in self.inventory:
            del self.inventory[item_id]
            print("Item", item_id, "sold!")
        else:
            print("Item", item_id, "not found. Please select another item to sell.")
    #Function for refurbishing a computer by updating price based on age, and optionally the Os
    #Function checks the year and calls the function update from Computer class to update
    # the price and OS if it is not None
    def refurbish(self, item_id: int, new_os: Optional[str]=None):
        if item_id in self.inventory:
            computer = self.inventory[item_id]  # locate the computer
            if int(computer.year_made) < 2000:
                computer.update_price(0)  # too old to sell, donation only
            elif int(computer.year_made) < 2012:
                computer.update_price(250)  # heavily-discounted price on machines 10+ years old
            elif int(computer.year_made) < 2018:
                computer.update_price(550)  # discounted price on machines 4-to-10 year old machines
            else:
                computer.update_price(1000)  # recent stuff
            if new_os is not None:
                computer.updateos(new_os)
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")
    #Function for printing the inventory which call display from computer class
    def print_inventory(self):
        # If the inventory is not empty
        if self.inventory:
            # For each item
            print(print(f"-" * 21, "New display starts for inventory","-" * 21))
            for item_id in self.inventory:
                #print its details
                print(item_id)
                self.inventory[item_id].display()
        else:
            print("No inventory to display.")
