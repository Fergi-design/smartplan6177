class GraduateStudyPlan:
    def __init__(self, courseNumber, courseName, requiredIn1, requiredIn2):
        # Initializes the study plan with course details and two "Required in" columns
        self.courseNumber = courseNumber            # Unique identifier for the course
        self.courseName = courseName                # Name of the course
        self.requiredIn1 = requiredIn1              # First required concentration
        self.requiredIn2 = requiredIn2              # Second required concentration
    
    # Getter methods
    def getCourseNumber(self):
        return self.courseNumber
    
    def getCourseName(self):
        return self.courseName
    
    def getRequiredIn1(self):
        return self.requiredIn1
    
    def getRequiredIn2(self):
        return self.requiredIn2
    
    # Setter methods
    def setCourseNumber(self, courseNumber):
        self.courseNumber = courseNumber

    def setCourseName(self, courseName):
        self.courseName = courseName
    
    def setRequiredIn1(self, requiredIn1):
        self.requiredIn1 = requiredIn1
    
    def setRequiredIn2(self, requiredIn2):
        self.requiredIn2 = requiredIn2
