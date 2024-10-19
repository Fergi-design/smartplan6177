import pandas as pd
from models.graduate_plan_model import GraduateStudyPlan

class GraduatePlanController:
    def __init__(self, studyPlanPath):
        self.studyPlanPath = studyPlanPath
    
    # Load the graduate study plan from an Excel file
    def loadGraduateStudyPlan(self):
        # Load the Excel file into a DataFrame
        df = pd.read_excel(self.studyPlanPath)

        # Ensure correct column names: "Course number", "Course name", "Required in #1", "Required in #2"
        courses = []
        for index, row in df.iterrows():
            course = GraduateStudyPlan(
                courseNumber=row['Course number'],      # Corrected column name
                courseName=row['Course name'],          # Corrected column name
                requiredIn1=row['Required in #1'],      # First required concentration
                requiredIn2=row['Required in #2']       # Second required concentration
            )
            courses.append(course)
        
        return courses

    # Get all courses required in a specific concentration
    def getCoursesForConcentration(self, concentration):
        study_plan_courses = self.loadGraduateStudyPlan()
        
        # Filter by concentration in either "Required in #1" or "Required in #2"
        filtered_courses = [
            course for course in study_plan_courses 
            if concentration in (course.getRequiredIn1(), course.getRequiredIn2())
        ]
        
        return filtered_courses

    # Match courses already taken with the ones in the study plan
    def matchCoursesWithTaken(self, takenCourses):
        study_plan_courses = self.loadGraduateStudyPlan()
        
        # Filter out courses already taken
        remaining_courses = [
            course for course in study_plan_courses
            if not any(taken.getCourseNumber() == course.getCourseNumber() for taken in takenCourses)
        ]
        
        return remaining_courses
