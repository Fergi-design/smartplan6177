#Model file for courses

class Course:
    def __init__(self, courseNumber,courseName, timesAvailabe):
        self.courseNumber = courseNumber
        self.courseName = courseName
        self.timesAvailabe = timesAvailabe
    
    def getCourseNumber(self):
        return self.courseNumber
    
    def getCourseName(self):
        return self.courseName
    
    def getTimesAvailable(self):
        return self.timesAvailabe
    
    def setCourseNumber(self, courseNumber):
        self.courseNumber = courseNumber

    def setCourseName(self, courseName):
        self.courseName = courseName
    
    def setTimesAvailable(self, timesAvailable):
        self.timesAvailable = timesAvailable