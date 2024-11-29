import sys
import os
import re
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controllers.course_Controller import CourseController, sc
from controllers.graduate_plan_Controller import GraduatePlanController
from controllers.prereq_Controller import PrereqController
from controllers.student_Controller import StudentController
from controllers.prereq_Controller import cpsc_url, cybr_url
import xlwt 
from xlwt import Workbook 


class CoursePlanningView:
    def __init__(self, FYS, GSP, DWRCS):
        self.FYS = FYS
        self.GSP = GSP
        self.DWRCS = DWRCS

    def getUserDocumentFilePath(self):
       print("Welcome to the Course Planning Tool")
       self.FYS = input("Enter the path of the Four Year Schedule excel file: ")
       self.GSP = input("Enter the path of the Graduate Study Plans excel file: ")
       self.DWRCS = input("Enter the path of the Degreeworks pdf file: ")

    #Course Planning
    #Co-Pilot was used to help write this function
    def coursePlanning(self):
        #workbook created
        wb = Workbook()
        #add_sheet is used to create sheet
        worksheet = wb.add_sheet('Sheet 1', cell_overwrite_ok=True)
        worksheet.write(0, 0, 'Course')
        worksheet.write(0, 1, 'Semester')
        worksheet.write(0, 2, 'Credit Hours Remaining')

        cc = CourseController(self.FYS, self.DWRCS)
        pc = PrereqController()
        gc = GraduatePlanController(self.GSP)
        student_concentration = ""
        #List of cs courses
        cpsc_courses = []
        #List of cybr courses
        cybr_courses = []
        # Get the courses from the FYS
        fys_courses = CourseController.checkDataFromFYS(CourseController.getDataFromFYS(cc))
        # Get the courses from the Graduate Study Plan
        gsp_courses = gc.loadGraduateStudyPlan()
        # Get the courses from the Degreeworks PDF and student data
        datafromDWRCS, student_data = CourseController.getDataFromDWRCS(cc)
        courses_taken = cc.formatDWData(datafromDWRCS)

        courses_taken_new = []
        #Remove Undergraduate courses from the list
        for i in range(len(courses_taken)):
            if courses_taken[i].getCourseNumber()[5] == '6':
                courses_taken_new.append(courses_taken[i])
        

        #List of prerequisites
        all_preReqs = []
        #Adjust concentration string
        if "General" in student_data.getStudentConcentration():
            student_concentration = "ACS General"
        elif "Software" in student_data.getStudentConcentration():
            student_concentration = "ACS Software Dev"
        elif "Data Science" in student_data.getStudentConcentration():
            student_concentration = "ACS AI and Data Science"
        elif "Cyber Defense" in student_data.getStudentConcentration():
            student_concentration = "CYBR Cyber Defense"
        elif "Mnaagement" in student_data.getStudentConcentration():
            student_concentration = "CYBR Management"
            
        #Get courses for needed for the student's concentration
        concentration_courses = gc.getCoursesForConcentration(student_concentration, gsp_courses)
        #Get courses remaining for the student
        remaining_courses = gc.matchCoursesWithTaken(courses_taken_new, concentration_courses)
        


        
        #Get Preqs from Webcrawler
        cpsc_courses = PrereqController.parse_courses(PrereqController.fetch_page(cpsc_url))
        cybr_courses = PrereqController.parse_courses(PrereqController.fetch_page(cybr_url))
        cpsc_courses_preReq = pc.getAll_PreReq(cpsc_courses)
        cybr_courses_preReq = pc.getAll_PreReq(cybr_courses)

        
        all_preReqs = cpsc_courses_preReq + cybr_courses_preReq
        

        student_preqs = []
        #Check if Student has any preqs
        for req in all_preReqs:
            for course in remaining_courses:
                if course.getCourseNumber() == req.getCourseNumber():
                    student_preqs.append(req.getPreqcourseNumber())

        
        #Remove courses for preqs that student has already taken
        student_preqs_new = []
        if len(student_preqs) > 0:
            for preq in student_preqs:
                for course in courses_taken_new:
                    if preq.getCourseNumber() == course.getCourseNumber():
                        student_preqs_new.append(preq)

        #Use Four Year Schedule to determine roadmap

        #Start course planning after latest semster in DWRCS
        latest_semester = courses_taken_new[-1].getTimesAvailable()
        latest_semester = latest_semester.split()
        season = latest_semester[0]
        year = latest_semester[1]
        #Get the courses that are available in the after latest semester
        fys_courses_new = []
        
        for i in range(len(fys_courses)):
            course_semester = fys_courses[i].getTimesAvailable()
            semester_index = 0
            index_to_remove = []
            #Remove latest semester
            if season[:2].upper() + year[-2:] in course_semester:
                course_semester.remove(season[:2].upper() + year[-2:])
            
            for semester_index, item in enumerate(course_semester, start=0):
                #spilt the semester into a list (e.g ['SU', '26']) to compare to the latest semester
                semester_list = re.split(r'(\d+)', item)
                semester_season = semester_list[0]
                semester_year = semester_list[1]
                
                #Remove semesters that are before latest semester
                if season[:2].upper() == "SP" and semester_season == "FA" and year[-2:] > semester_year:
                    index_to_remove.append(semester_index)
                elif season[:2].upper() == "SP" and semester_season == "SU" and year[-2:] > semester_year:
                    index_to_remove.append(semester_index)
                elif season[:2].upper() == "FA" and semester_season == "SU" and year[-2:] > semester_year:
                    index_to_remove.append(semester_index)
                elif season[:2].upper() == "FA" and semester_season == "SP" and year[-2:] > semester_year:
                    index_to_remove.append(semester_index)
                elif season[:2].upper() == "FA" and semester_season == "SU" and year[-2:] == semester_year:
                    index_to_remove.append(semester_index)    
                elif season[:2].upper() == "SU" and semester_season == "SP" and year[-2:] > semester_year:
                    index_to_remove.append(semester_index)
                elif season[:2].upper() == "SU" and semester_season == "FA" and year[-2:] > semester_year:
                    index_to_remove.append(semester_index)            
                elif season[:2].upper() == "SU" and semester_season == "SP" and year[-2:] == semester_year:
                    index_to_remove.append(semester_index)
            
            
            for index in index_to_remove:
                course_semester.remove(course_semester[index])
                    
            fys_courses[i].setTimesAvailable(course_semester)

        #Check if student has taken the preqs for the courses
        prereq_needed = []
        if len(student_preqs_new) > 0:
            for preq in student_preqs_new:
                for course in courses_taken:
                    preq_list = preq.getPreqcourseNumber()
                    if len(preq_list) == 3:
                        if preq_list[0] != course.getCourseNumber() or preq_list[1] != course.getCourseNumber():
                            prereq_needed.append(preq_list[0] + "or" + preq_list[1])
                        elif preq_list[2] != course.getCourseNumber():
                            prereq_needed.append(preq_list[2])
                    elif len(preq_list) == 2:
                        if preq_list[0] != course.getCourseNumber() or preq_list[1] != course.getCourseNumber():
                            prereq_needed.append(preq_list[0] + "or" + preq_list[1])
                    elif len(preq_list) == 1:
                        if preq_list[0] != course.getCourseNumber():
                            prereq_needed.append(preq_list[0])
                        

        #Course Plan
        course_plan = []
        semester_course_count = []
        
        # Initialize a dictionary to keep track of the count of courses per semester
        semester_counts = {}
        #Add Preqs to the course plan if applicable
        if len(prereq_needed) > 0:
            for preq in prereq_needed:
                for course in fys_courses:
                    if course.getCourseNumber() == preq:

                        times_available = course.getTimesAvailable()
                
                        for semester in times_available:
                            # Initialize the count for the semester if it doesn't exist
                            if semester not in semester_counts:
                                semester_counts[semester] = 0
                    
                            # Check if the count for the semester is less than 4
                            if semester_counts[semester] < 4:
                                course_plan.append({"Semester": semester, "Course": course.getCourseNumber()})
                                semester_course_count.append({"Semester": semester, "Count": 1})
                                semester_counts[semester] += 1
                                break  # Move to the next course once added to a semester
                            

        

        # Add courses from remaining_courses to course_plan
        for course in remaining_courses:
            for fys_course in fys_courses:
                if course.getCourseNumber() == fys_course.getCourseNumber():
                    times_available = fys_course.getTimesAvailable()
    
                    for semester in times_available:
                        # Initialize the count for the semester if it doesn't exist
                        if semester not in semester_counts:
                            semester_counts[semester] = 0
        
                        # Check if the count for the semester is less than 4
                        if semester_counts[semester] < 4:
                            course_plan.append({"Semester": semester, "Course": fys_course.getCourseNumber()})
                            semester_course_count.append({"Semester": semester, "Count": 1})
                            semester_counts[semester] += 1
                            break  # Move to the next course once added to a semester                    

        #Write the courses to the excel file
        for row_num, course in enumerate(course_plan, start=1):
            worksheet.write(row_num, 0, course["Course"])
            worksheet.write(row_num, 1, course["Semester"])
        worksheet.write(1, 2, (len(remaining_courses) + len(prereq_needed)) * 3)
        try:
            wb.save('CoursePlanning.xls')
            print("Course Planning Completed")
        except:
            print("Error saving file please try again")
        
        


            


# cp = CoursePlanningView('','','')
# #4-year schedule.xlsx, audit-909502440-AB85SKL0.pdf, Graduate Study Plans -revised.xlsx
# cp.getUserDocumentFilePath() #Place files in same folder and enter the file names
# cp.coursePlanning()
if __name__=="__main__":
    cp = CoursePlanningView('','','')
    cp.getUserDocumentFilePath() #Place files in same folder and enter the file names
    cp.coursePlanning()
