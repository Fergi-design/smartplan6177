import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.student_model import Student

#Initialize Student Model
student = Student('','','')

class StudentController:
    def __init__(self, studentData):
        self.studentData = studentData   
   
    def setupStudentData(self, Data):
        return Student(self.trimStrings(Data[0], "Level").replace("Level", ""), self.trimStrings(Data[0], "Major").replace("Major", ""), self.trimStrings(Data[1], "Concentration").replace("Concentration", ""))
    
    

    #Trim the strings for the student data
    def trimStrings(self, input_string, type):
        start_index = 0
        end_index = 0
        if(type == "Level"):
            start_index = input_string.find("Level")
            end_index = input_string.find("Classification")
        elif(type == "Major"):
            start_index = input_string.find("Major")
            end_index = input_string.find("Program")
        elif(type == "Concentration"):
            start_index = input_string.find("Concentration")
            end_index = input_string.find(",")
        else:
            print("Invalid type")

        return input_string[start_index:end_index].strip()   