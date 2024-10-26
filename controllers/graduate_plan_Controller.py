import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
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
                courseNumber=row['Course Number'],      # Corrected column name
                courseName=row['Course name'],          # Corrected column name
                requiredIn1=row['Required in #1'],      # First required concentration
                requiredIn2=row['Required in #2']       # Second required concentration
            )
            courses.append(course)
        
        return courses

    # Get all courses required in a specific concentration
    def getCoursesForConcentration(self, concentration, courses):
        study_plan_courses = courses
            
        # Filter by concentration in either "Required in #1" or "Required in #2"
        filtered_courses = [
            course for course in study_plan_courses 
            if concentration in (str(course.getRequiredIn1()).replace("-", ""), str(course.getRequiredIn2()).replace("-", ""))
        ]
        # Handle case where a course is a core course
        for course in study_plan_courses:
            if "ACS" in concentration:
                if ("ACS Core" in (str(course.getRequiredIn1()).replace("-", ""), str(course.getRequiredIn2()).replace("-", ""))):
                    filtered_courses.append(course)
            elif "CYBR" in concentration:
                if ("CYBR Core" in (str(course.getRequiredIn1()).replace("-", ""), str(course.getRequiredIn2()).replace("-", ""))):
                    filtered_courses.append(course)
        
        return filtered_courses

    # Match courses already taken with the ones in the study plan
    def matchCoursesWithTaken(self, takenCourses, courses):
        study_plan_courses = courses
        
        # Filter out courses already taken
        remaining_courses = [
            course for course in study_plan_courses
            if not any(taken.getCourseNumber() == course.getCourseNumber() for taken in takenCourses)
        ]
        
        return remaining_courses


# Test the GraduatePlanController
# gc = GraduatePlanController("Graduate Study Plans -revised.xlsx")
# study_plan = gc.loadGraduateStudyPlan()
# for course in study_plan:
#   print(course.getCourseNumber(), course.getCourseName(), course.getRequiredIn1(), course.getRequiredIn2())

# # Test the getCoursesForConcentration method
# concentration = "ACS General"
# acs_courses = gc.getCoursesForConcentration(concentration, study_plan)
# for course in acs_courses:
#     print(course.getCourseNumber(), course.getCourseName(), course.getRequiredIn1(), course.getRequiredIn2())