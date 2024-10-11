import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.course_model import Course
#controller for course

FYS_courses = []

class CourseController:
    def __init__(self, FYS, DWRCS):
        self.FYS = FYS
        self.DWRCS = DWRCS

    #Check Data from FYS and create new array with the semesters that have 'F' or 'O' values
    def checkDataFromFYS(filtered_array):
        for i in range(len(filtered_array)):
            semesters = []
            for j in range(2, len(filtered_array[i])):
                if str(filtered_array[i][j]).__contains__('F') or str(filtered_array[i][j]).__contains__('O'):
                    if(j == 2):
                        semesters.append('FA24') 
                    elif (j == 3):
                        semesters.append('SP25')
                    elif (j == 4):
                        semesters.append('SU25') 
                    elif (j == 5):
                        semesters.append('FA25')
                    elif (j == 6):
                        semesters.append('SP26')
                    elif (j == 7):
                        semesters.append('SU26')
                    elif (j == 8):
                        semesters.append('FA26')
                    elif (j == 9):
                        semesters.append('SP27')
                    elif (j == 10):
                        semesters.append('SU27')
                    elif (j == 11):
                        semesters.append('FA27')
                    elif (j == 12):
                        semesters.append('SP28')
                    elif (j == 13):
                        semesters.append('SU28')
                    elif (j == 14):
                        semesters.append('FA28')
                    elif (j == 15):
                        semesters.append('SP29')
                    
            FYS_courses.append(Course(filtered_array[i][0], filtered_array[i][1], semesters))

        return FYS_courses

    #Github Copilot was used to help write this function
    def getDataFromFYS(self):
        df = pd.read_excel(self.FYS, skiprows=[0,1])
        #drop previous semester columns and skip the first column
        new_df = df.drop(columns=['SP20', 'SU20',  'FA20',   'SP21',  'SU21',  'FA21',  'SP22', 'SU22', 'FA23', 'SP24', 'SU24'])

        # Drop the 'Unnamed: 27' column if it exists
        if 'Unnamed: 27' in new_df.columns:
            new_df = new_df.drop(columns=['Unnamed: 27'])
            
        # Filter the DataFrame for rows where 'F' or 'O' values are present in columns with index greater than 2
        filter_mask = new_df.iloc[:, 3:].map(lambda x: 'F' in str(x) or 'O' in str(x)).any(axis=1)
        filtered_df = new_df[filter_mask]
        # Convert the filtered DataFrame to a NumPy array
        filtered_array = filtered_df.to_numpy()
        return filtered_array

    def getDataFromDWRCS(self):
        return self.DWRCS 
        

#Testing the getDataFromFYS
'''
c = CourseController("path to four year schedule excel", '')
courses = CourseController.checkDataFromFYS(CourseController.getDataFromFYS(c))
print(courses[0].getCourseName())
print(courses[0].getCourseTitle())
print(courses[0].getTimesAvailable())
'''
