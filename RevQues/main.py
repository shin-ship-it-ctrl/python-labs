class Student:
    def __init__(self,stud_id, stud_name):
        self.stud_id = stud_id
        self.stud_name = stud_name
        self.modules = {}

    def set_stud_id(self, stud_id):
        self.stud_id = stud_id

    def set_stud_name(self,stud_name):
        self.stud_name=stud_name

    def get_stud_id(self):
        return self.stud_id

    def get_stud_name(self):
        return self.stud_name

    def enrol_modules(self):
        mark=0
        modulename = input("Enter Module Name : ")
        modulecode = input("Enter Module Code : ")
        mark=input("Enter Mark : ")
        self.modules[modulename] = modulename
        self.modules[modulecode] = modulecode
        self.modules[mark] = mark

    def addmark(self, modulecode):
        newmark=input("Enter Mark : ")
        mark= modulecode.update(newmark)
        self.modules.update({modulecode:mark})

    def get_mark(self, modulecode,mark=None):
        return modulecode.get(mark)

    def average(self):
        mark = self.get_mark(self.get_stud_id(),self.get_stud_name())










