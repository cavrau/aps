class Rating:
    def __init__(self, comment, grade):
        self.__comment = comment
        self.__grade = grade

    def get_comment(self):
        return self.__comment
    
    def get_grade(self):
        return self.__grade
