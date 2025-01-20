from DesignPatterns.ObserverPattern.Observables.iPhoneStockObservable import IPhoneStockObservable
from DesignPatterns.ObserverPattern.Observers.emailNotificationObserver import EmailNotificationObserver
from DesignPatterns.ObserverPattern.Observers.mobileNotificationObserver import MobileNotificationObserver


def main():
    emailObs1 = EmailNotificationObserver("abc@gmail.com", "Kingshuk")
    mobileObs1 = MobileNotificationObserver(901667283, "Arpita")

    iPhoneStockObj = IPhoneStockObservable()
    iPhoneStockObj.addOberserves(emailObs1)
    iPhoneStockObj.addOberserves(mobileObs1)
    iPhoneStockObj.setData(100)

if __name__ == "__main__":
    main()