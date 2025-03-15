import datetime

from Models.ticket import Ticket
from Utils.Costing.CostingStrategy import Costingstrategy


class CostCalculator:
    def __init__(self,st=Costingstrategy.PerHour):
        self.st = st

    def calculate(self,price,entryTime):
        startTime = entryTime
        endtime = datetime.datetime.now()+datetime.timedelta(days=1)
        duration = endtime-startTime
        duration_in_s = duration.total_seconds()
        hours = divmod(duration_in_s, 3600)[0]
        return hours*price

