import datetime
import uuid
from threading import Lock
from models.registration import Registration
import logging
logging.basicConfig(level=logging.INFO)

class RegistrationSystem:
    _instance = None
    _lock = None

    def __new__(cls):
        cls._instance = super().__new__(cls)
        cls._instance.registrationDetails = dict()
        cls._instance._lock = Lock()
        cls._instance.users = dict()
        cls._instance.courses = dict()
        cls._instance.log = logging.getLogger("CourseRegistration")
        return cls._instance

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            RegistrationSystem()
        return cls._instance

    def addUser(self,user):
        id = user.getId()
        if id in self.users:
            self.log.info(f"User with id {id} already exists!!!")
            return
        self.users[id] = user
        self.log.info(f"User {id} added!!")

    def addCourse(self,course):
        id = course.getId()
        if id in self.courses:
            self.log.info(f"Course with id {id} already exists!!!")
            return
        self.courses[id] = course
        self.log.info(f"Course {id} added!!")

    def registerCourse(self,uId,courseId):
        self._lock.acquire()
        try:
            courseObj = self.courses[courseId]
            if courseObj.getCapacity() < courseObj.getMaxCapacity():
                try:
                    user = self.users[uId]
                    if user.courseExists(courseId):
                        self.log.info(f"User laready registered to the course!!")
                        return
                    courseObj.increaseCapacity()
                    rId = self._generateId()
                    reg = Registration(rId,user,courseObj)
                    user.addCourseID(rId, courseObj)
                    self.log.info("Registration successful!!!")
                except Exception as e:
                    raise ValueError(f"USer {uId} doesn't exist in the system, first register!!!!")
            else:
                self.log.info(f"Course {courseId} is already full!!!")
        except Exception as e:
            raise ValueError(f"Course iwth id {id} doesn't exist!!!")
        self._lock.release()

    def display(self,courses=None):
        if not courses:
            courses = self.courses.values()
        self.log.info("\nCOURSE_ID\tNAME\tINSTRUCTOR\tSEAT_AVAILABLE")
        for c in courses:
            self.log.info(f"\n{c.getId()}\t{c.getName()}\t{c.getInstructor()}\t{c.getMaxCapacity()-c.getCapacity()}")

    def searchByID(self,id):
        if id in self.courses:
            self.log.info("Found the below course-")
            self.display([self.courses[id]])
            return
        self.log.info(f"Course with id {id} doens't exist in the system")

    def searchByKey(self,searchKey):
        matches = []
        for key,val in self.courses.items():
            if searchKey in val.getName():
                matches.append(val)
        if matches:
            self.log.info("Found the below courses-")
            self.display(matches)
            return
        self.log.info(f"No course found iwth key {searchKey}")


    def _generateId(self):
        return f"{uuid.uuid4().hex[:6]}_{datetime.datetime.today()}"