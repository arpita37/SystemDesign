from DesignPatterns.ObserverPattern.Observables.productStockInterface import ProductStockInterface
from DesignPatterns.ObserverPattern.Observers.observerInterface import ObserverInterface


class IPhoneStockObservable(ProductStockInterface):
    def __init__(self):
        super().__init__()
        self.observersList = set()
        self.stockCount = 0

    def addOberserves(self, observer: ObserverInterface):
        if observer not in self.observersList:
            self.observersList.add(observer)
        else:
            print(f"Observer {observer.username} is already present in the notifyees list")

    def removeObservers(self, observer):
        if observer in self.observersList:
            self.observersList.remove(observer)
        else:
            print(f"Observer {observer.username} is not present in the notifyees list")

    def notifyObservers(self):
        for observer in self.observersList:
            observer.update()

    def setData(self, newStock : int) -> None:
        self.notifyObservers()
        self.stockCount += newStock
        print(f"New stock addition completed")
