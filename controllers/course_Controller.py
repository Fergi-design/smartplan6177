import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.course_model import Course
from pypdf import PdfReader
from controllers.student_Controller import StudentController

#controller for course
FYS_courses = []
sc = StudentController([])

class CourseController:
    #student data from student controller
    
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
        output = []   # array to be returned by method
        studentData = []   # array to store student data
        while True:
            filename = self.DWRCS  
            # check if PdfReader works; check if file exists
            try:   
                reader = PdfReader(filename)
                break   # break while loop

            # file not found; restart loop
            except:   
                print("\nInvalid input or file not found. Try again.")
                break

        # creating a pdf reader object
        reader = PdfReader(filename)

        for i in range(len(reader.pages)):
            # creating a page object
            page = reader.pages[i]

            # extracting text from page
            text = page.extract_text()
            if i == 0:
                storeFile = open("convertedText.txt", "w") #creates file if doesn't exist, overwrites if it does
                storeFile.write(text)
                storeFile.close()
            else:
                storeFile = open("convertedText.txt", "a") #additional pages of PDF as appended to file
                storeFile.write('\n' + text)
                storeFile.close()
        #storeFile (AKA convertedText.txt) is used to easily parse data to be added to output array

        # adds necessary data to array to be processed by other modules in software
        with open("convertedText.txt", "r") as file:
            for line in file:
                # finds lines from list of taken courses and adds them to array; strips \n for better reading
                if " Fall " in line: 
                    str = line.strip()
                    output.append(str)
                elif " Spring " in line:
                    str = line.strip()
                    output.append(str)
                elif " Summer " in line:
                    str = line.strip()
                    output.append(str)
                elif " Level " in line:
                    str = line.strip()
                    studentData.append(str)
                elif " Concentration " in line:
                    str = line.strip()
                    studentData.append(str)
                elif " Major " in line:
                    str = line.strip()
                    studentData.append(str)

        file.close()
        return output,  sc.setupStudentData(studentData)  # return array and student data

    def formatDWData(courseData):
        DW_courses = []
        courseData.pop()   # remove unwanted student data from array
        # format data from DWRCS to be used in other contollers
        for course in courseData:
            courseNumber = course[0:9]
            courseName = course[10: course.find("(")].replace("CURR", "").strip()
            courseSemester = course[course.find(")")+1: ].strip()
            DW_courses.append(Course(courseNumber, courseName, courseSemester))
        
        
        return DW_courses


#Testing the getDataFromFYS
# c = CourseController("path to four year schedule excel", "path to DWRCS pdf")
#courses = CourseController.checkDataFromFYS(CourseController.getDataFromFYS(c))
# print(courses[0].getCourseName())
# print(courses[0].getCourseTitle())
# print(courses[0].getTimesAvailable())
#print(c.getDataFromDWRCS())
#print(c.formatDWData(c.getDataFromDWRCS()))