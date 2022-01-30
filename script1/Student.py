class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
    
    def report_gpa(self):
        sentence = f'{self.name} has a GPA of {self.gpa}'
        return sentence