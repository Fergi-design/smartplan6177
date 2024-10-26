# Model file for courses

class Preq:
    def __init__(self, courseNumber, preqcourseNumber):
        self.courseNumber = courseNumber
        self.preqcourseNumber = preqcourseNumber

    def getCourseNumber(self):
        return self.courseNumber

    def getPreqcourseNumber(self):
        return self.preqcourseNumber

    def setCourseNumber(self, courseNumber):
        self.courseNumber = courseNumber

    def setPreqcourseNumber(self, preqcourseNumber):
        self.preqcourseNumber = preqcourseNumber
