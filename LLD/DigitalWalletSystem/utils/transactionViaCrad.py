from models.paymentStatus import Paymentstatus
from utils.processTransaction import ProcessTransaction


class TransactionViaCard(ProcessTransaction):
    def __init__(self,tx,src,dest,amount):
        super().__init__(tx,src,dest,amount)

    def execute(self):
        st1 = st2 = True
        self.authenticate()
        print("\nPayment in progress!!!")
        self.tx.setStatus(Paymentstatus.PROGRESS)
        try:
            self.src.debit(self.amount)
            try:
                self.dest.credit(self.amount)
                print("\nPayment successful using card")
                return True
            except Exception as e:
                print(f"\nSome error occured {e}, rolling back transaction")
                st1 = False
                st2 = False
        except Exception as e:
            print(f"\nSome error occured {e}, rolling back transaction")
            st1 = False

        if not st1:
            self.src.credit(self.amount)
        if not st2:
            self.dest.debit(self.amount)
        return False

    def authenticate(self):
        #Implement the logic
        print(f"Authenticated user {self.src.getName()} and {self.dest.getName()} for transaction via card")