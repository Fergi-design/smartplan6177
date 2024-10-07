#Model file for courses

class Course:
    def __init__(self, courseName,courseTitle, timesAvailabe):
        self.courseName = courseName
        self.courseTitle = courseTitle
        self.timesAvailabe = timesAvailabe
    
    def getCourseName(self):
        return self.courseName
    
    def getCourseTitle(self):
        return self.courseTitle
    
    def getTimesAvailable(self):
        return self.timesAvailabe
    
    def setCourseName(self, courseName):
        self.courseName = courseName

    def setCourseTitle(self, courseTitle):
        self.courseTitle = courseTitle
    
    def setTimesAvailable(self, timesAvailable):
        self.timesAvailable = timesAvailable