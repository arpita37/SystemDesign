class Payment:
    def __init__(self,st="CASH"):
        self.method = st

    def pay(self,amt,log):
        log.info(f"Payemnt of Rs. {amt} done through {self.method}")