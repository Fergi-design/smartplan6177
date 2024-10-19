#Student Model

class Student:
    def __init__(self, studentYear, studentMayor):
        self.studentYear = studentYear
        self.studentMayor = studentMayor
    
    def getStudentYear(self):
        return self.studentYear
    
    def getStudentMayor(self):
        return self.studentMayor
    
    def setStudentYear(self, studentYear):
        self.studentYear = studentYear

    def setStudentMayor(self, studentMayor):
        self.studentMayor = studentMayor
