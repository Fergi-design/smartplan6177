# graduate_plan_model.py
class GraduateStudyPlan:
    def __init__(self, courseNumber, courseName, concentration):
        # Initializes the study plan with course details and concentration
        self.courseNumber = courseNumber  # Unique identifier for the course
        self.courseName = courseName      # Name of the course
        self.concentration = concentration # Concentration associated with the course

    def getCourseNumber(self):
        return self.courseNumber
    
    def getCourseName(self):
        return self.courseName
    
    def getConcentration(self):
        return self.concentration
    
    def setCourseNumber(self, courseNumber):
        self.courseNumber = courseNumber

    def setCourseName(self, courseName):
        self.courseName = courseName
    
    def setConcentration(self, concentration):
        self.concentration = concentration
