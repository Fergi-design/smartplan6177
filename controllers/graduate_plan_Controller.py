import pandas as pd 
import sys 
import os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) 
from models.graduate_plan_model import GraduateStudyPlan 
from models.course_model import Course 

class GraduatePlanController: 
    def __init__(self, graduateStudyPlanPath): 
        # Initialize the controller with the path to the graduate study plan file 
        self.graduateStudyPlanPath = graduateStudyPlanPath 
        self.studyPlanCourses = []  # List to store GraduateStudyPlan objects 

    def loadGraduateStudyPlan(self): 
        # Load the graduate study plan from an Excel file and parse the required columns 
        df = pd.read_excel(self.graduateStudyPlanPath) 
        # Assuming the file has 'Course Number', 'Course Name', and 'Concentration' columns 
        for index, row in df.iterrows(): 
            courseNumber = row['Course Number'] 
            courseName = row['Course Name'] 
            concentration = row['Concentration'] 
          
            # Create a GraduateStudyPlan object and add it to the studyPlanCourses list 
            studyPlan = GraduateStudyPlan(courseNumber, courseName, concentration) 
            self.studyPlanCourses.append(studyPlan) 
          
        return self.studyPlanCourses 

    def getCoursesForConcentration(self, concentration): 
        # Retrieve a list of courses for the given concentration 
        filtered_courses = [course for course in self.studyPlanCourses if course.getConcentration() == concentration] 
        return filtered_courses 

    def matchCoursesWithTaken(self, takenCourses): 
        # This function matches the courses in the study plan with the courses the student has already taken 
        remainingCourses = [] 
        for course in self.studyPlanCourses: 
            # If the course from the study plan is not in the list of taken courses, add it to remainingCourses 
            if course.getCourseNumber() not in [taken.getCourseName() for taken in takenCourses]: 
                remainingCourses.append(course) 

        return remainingCourses
