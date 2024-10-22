import requests
from bs4 import BeautifulSoup
import re
# URL of the course catalog page
url = "https://catalog.columbusstate.edu/course-descriptions/cpsc/"

def fetch_page(url):
    """Fetch the webpage content."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
        return None

  def parse_courses(html_content):
    """Parse course information from HTML."""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all course blocks (assuming they are inside <p> tags or similar structure)
    courses = []
    course_divs = soup.find_all('div') 
    for div in course_divs:
        course_text = div.get_text(strip=True)
      
       
        
        
        
        # Extract course code and name (e.g., CPSC 6109. Advanced Algorithms)
        match = re.match(r"^(CPSC \d{4})+(.*)", course_text)
        print(match)
        
        if match:
            course_code = match.group(1)
            course_name = match.group(2).split('.')[0].strip()

            prereq_match = re.search(
                 r"Prerequisite\(s\):\s*(.*?)\s*(?:Re|$)", course_text
                )
            
            if prereq_match:
                
                prerequisites = prereq_match.group(1).strip()
                
            else:
                prerequisites = "None"


            courses.append({
                "Course Code": course_code,
                "Course Name": course_name,
                "Prerequisites": prerequisites
            })


    return courses

html_content = fetch_page(url)

#Gather List of Courses from the CPSC course descriptions
courses = parse_courses(html_content)

def extract_course_codesCPCS(text):
    """Extract all CPSC course codes from the given text."""
    # Use re.findall to get all occurrences of "CPSC ####"
    clean_text = text.replace('\xa0', ' ')
    course_codes = re.findall(r"CPSC\s\d{4}(?=\D|$)", clean_text)

    return course_codes

def find_CPSCpreReq(courseNum, courses):
    """Find the prerequisites for a given course number."""
    for course in courses:
        if courseNum == course['Course Code']:
            fullText = course['Prerequisites'].replace('with', ' ')
            courseList = extract_course_codes(fullText)
            return courseList
    return "Course not found."


