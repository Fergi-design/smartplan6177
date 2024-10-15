# importing required classes
from pypdf import PdfReader

filename = ""   # instantiate variable for DegreeWorks file
while True:
    filename = input("\nPlease enter the name of the PDF file from DegreeWorks: ")
    # check if PdfReader works; check if file exists
    try:
        reader = PdfReader(filename)
        break   # break while loop
    
    # file not found; restart loop
    except:   
        print("\nInvalid input or file not found. Try again.")

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
        
print("Success!")   # output file was created successfully


# adds necessary data to output file to be processed by other modules in software
with open("convertedText.txt", "r") as file:
    with open("coursesOutput.txt", "w") as output:
        for line in file:
            # finds lines that say you have already taken a course; may contain duplicate lines (CURR) and includes undergrad courses
            if " Fall " in line: 
                output.write(line + '\n')
            elif " Spring " in line:
                output.write(line + '\n')
            elif " Summer " in line:
                output.write(line + '\n')
            elif "CURR" in line:
                output.write(line + '\n')
    output.close()
file.close()
