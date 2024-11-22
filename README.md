Smart Planning Tool - Graduate Study Plan Module

Purpose

The Graduate Study Plan Module is part of the Smart Planning Tool for the Master of Applied Computer Science program. This module helps students and advisors identify required courses for graduation based on a specific concentration, using the graduate study plan as a reference. It enables users to:

- Load course details from an Excel file.
- Filter courses by concentrations.
- Generate a list of courses still required for degree completion.

------------------------------------------------------

Prerequisites

To run this project, ensure you have the following installed:

- Python (version 3.8 or higher)
- pip (Python package manager)
- Required Python libraries:
  - pandas (for data manipulation)
  - openpyxl (for reading Excel files)
  -requests (for making HTTP requests)
  -bs4 (BeautifulSoup for web scraping)
  -re (regular expressions)
  -PyPDF2 (for working with PDF files)


Install the dependencies using the following command:

pip install pandas openpyxl requests beautifulsoup4 pypdf2

------------------------------------------------------

Download 
Clone the repository or download the source code files directly:

git clone https://github.com/Fergi-design/smartplan6177.git

Alternatively, download the ZIP file from the repository and extract it.

------------------------------------------------------

Build/Configuration/Installation/Deployment 

File Structure: Ensure the files are organized as follows:
   
SmartPlanningTool/
├── controllers/
│   ├── course_controller.py
│   ├── graduate_plan_controller.py
│   ├── prereq_controller.py
│   └── student_controller.py
├── models/
│   ├── course_model.py
│   ├── graduate_plan_model.py
│   ├── prereq_model.py
│   └── student_model.py
├── views/ 
│ └── course_planning_view.py 
├── input/ 
│ └── graduate_study_plan.xlsx
├── README.md

PDF File: Place your Degreeworks PDF file in the `input/` directory. Ensure the file has the following column names:
   - Course number
   - Course name
   - Required in #1
   - Required in #2

------------------------------------------------------
Usage

Controllers Folder
The controllers handle the interaction between models and views. Each controller file is responsible for different parts of the application:
1.	course_controller.py: Handles course data, loading, and filtering.
2.	graduate_plan_controller.py: Handles the graduate study plan logic, including identifying required courses for concentrations.
3.	prereq_controller.py: Handles course prerequisite management.
4.	student_controller.py: Manages student-related data, course progress, and concentration tracking.

Models Folder
The models define the core data structures and their logic:
1.	course_model.py: Defines the Course class with details about each course.
2.	graduate_plan_model.py: Defines the GraduatePlan class, representing the overall study plan and its associated courses.
3.	prereq_model.py: Defines prerequisites for courses and their relationships.
4.	student_model.py: Defines student data and the courses they’ve taken or need to take.

Views Folder
The views provide the user interface or interaction layer for the project:
•	course_planning_view.py: Displays information to the user about courses, the graduate study plan, and concentration requirements.

The project also includes functionality for extracting and processing data from the Degreeworks PDF. This is made possible by the PyPDF2 library.
