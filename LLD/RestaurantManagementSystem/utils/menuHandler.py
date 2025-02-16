from models.menuItem import Menuitem

class MenuHandler:
    def __init__(self):
        self.menuItems = dict()

    def addMenu(self, menu : Menuitem, log):
        id = menu.getId()
        if id in self.menuItems:
            raise ValueError("Id lready exists!!!!")
        self.menuItems[menu.getId()] = menu
        log.info(f"Menu item added!!!")

    def updatePrice(self,menu : Menuitem, val, log):
        id = menu.getId()
        if id not in self.menuItems:
            log.info("Menu item does'nt exist")
            return
        self.menuItems[id].updatePrice(val)
        log.info(f"Menu price updated!!!")

    def updateStatus(self,menu : Menuitem, val, log):
        id = menu.getId()
        if id not in self.menuItems:
            log.info("Menu item does'nt exist")
            return
        self.menuItems[id].updateStatus(val)
        log.info(f"Menu status updated!!!")

    def showMenu(self):
        print("MENUID\tITEM_NAME\tAMOUNT")
        for key, val in self.menuItems.items():
            print(f"{val.getId()}\t{val.getName()}\t{val.getPrice()}")