from models.staff import Staff


class StaffHandler:
    def __init__(self):
        self.staffs = dict()

    def addStaff(self, staff : Staff, log):
        id = staff.getId()
        if id in self.staffs:
            raise ValueError("Id lready exists!!!!")
        self.staffs[staff.getId()] = staff
        log.info(f"Staff {staff.getName()} added!!!")

    def updateRating(self,staff : Staff, val, log):
        id = staff.getId()
        if id not in self.staffs:
            raise ValueError("Id doesn't exist!!!!")
        obj = self.staffs[id]
        obj.updateRating(val)
        log.info("Rating updated!!!")
