from models.course import Course
from models.student import Student
from publicInterfaces.registrationSystem import RegistrationSystem


class Demo:
    @staticmethod
    def run():
        obj = RegistrationSystem()
        obj.get_instance()
        u1 = Student(1,"Arpita","abasak@gmail.com")
        u2 = Student(2, "Kingshuk", "kbose@gmail.com")
        u3 = Student(3, "Adhrit", "akar@yahoo.com")

        obj.addUser(u1)
        obj.addUser(u2)
        obj.addUser(u3)

        c1 = Course("Maths",1,"SIR",2)
        c2 = Course("English", 2, "MADAM", 3)
        c3 = Course("Physics", 3, "SIR", 2)
        c4 = Course("Maps", 4, "MADAM", 2)

        obj.addCourse(c1)
        obj.addCourse(c2)
        obj.addCourse(c3)
        obj.addCourse(c4)

        obj.registerCourse(1,1)
        obj.registerCourse(2, 1)
        obj.registerCourse(3, 1)

        obj.searchByID(1)
        obj.searchByKey("Ma")

if __name__ == "__main__":
    Demo.run()