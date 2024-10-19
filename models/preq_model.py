# Model file for courses

class Preq:
    def __init__(self, courseName, preqName):
        self.courseName = courseName
        self.preqName = preqName

    def getCourseName(self):
        return self.courseName

    def getPreqName(self):
        return self.preqName

    def setCourseName(self, courseName):
        self.courseName = courseName

    def setPreqName(self, preqName):
        self.preqName = preqName
