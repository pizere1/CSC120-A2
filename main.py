from Computer import Computer
from ResaleShop import ResaleShop
def main():
    resaleshop: ResaleShop = ResaleShop()
    comp1:Computer=Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2013, 1500)
    resaleshop.buy(comp1)
    resaleshop.print_inventory()
    comp2:Computer=Computer("2019 MacBook Pro",  "Intel", 289, 16, "High Sierra", 2019, 3000)
    resaleshop.buy(comp2)
    resaleshop.print_inventory()
    resaleshop.refurbish(1, "Mac23")
    resaleshop.print_inventory()
    comp1.updateos(None)
if __name__ == "__main__":
    main()
