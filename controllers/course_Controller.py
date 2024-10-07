#controller for course

class CourseController:
    def __init__(self, FYS, DWRCS):
        self.FYS = FYS
        self.DWRCS = DWRCS

    def getDataFromFYS(self):
        return self.FYS   

    def getDataFromDWRCS(self):
        return self.DWRCS 
        