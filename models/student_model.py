#Student Model

class Student:
    def __init__(self, studentYear, studentMajor, studentConcentration):
        self.studentYear = studentYear
        self.studentMajor = studentMajor
        self.studentConcentration = studentConcentration
    
    def getStudentYear(self):
        return self.studentYear
    
    def getStudentMajor(self):
        return self.studentMajor
    
    def setStudentYear(self, studentYear):
        self.studentYear = studentYear

    def setStudentMajor(self, studentMajor):
        self.studentMajor = studentMajor

    def setStudentConcentration(self, studentConcentration):
        self.studentConcentration = studentConcentration
    
    def getStudentConcentration(self):
        return self.studentConcentration
