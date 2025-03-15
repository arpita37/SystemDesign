from datetime import datetime
from Utils.Costing.CostingStrategy import Costingstrategy
from Utils.Costing.costCalculator import CostCalculator


class w4Calculator(CostCalculator):
    def __init__(self):
        super().__init__(Costingstrategy.perDay)

    def calculate(self,price,entryTime):
        startTime = entryTime
        endtime = datetime.now()
        duration = endtime-startTime
        duration_in_s = duration.total_seconds()
        hours = divmod(duration_in_s, 86400)[0]
        return hours*price