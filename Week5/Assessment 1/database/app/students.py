from app.orm import ORM

class Students(ORM):
    tablename = 'students'
    fields = ["fname", "lname", "school", "id", "gpa"]

    def __init__(self, *args, **kwargs):
        self.pk = kwargs.get('pk')
        self.fname = kwargs.get('fname')
        self.lname = kwargs.get('lname')
        self.school = kwargs.get('school')
        self.id = kwargs.get('id')
        self.gpa = kwargs.get('gpa')

    @classmethod
    def all_students(cls):
        return cls.get_all()
    
    @classmethod
    def one_student(cls, pk):
        return cls.get_one("WHERE pk = ?", (pk,))

    #UPDATE ANY STUDENTS SCHOOL
    @classmethod
    def update_schools(cls):
        students = cls.all_students()
        for row in students:
            print(f"NAME: {row.fname} {row.lname} | SCHOOL: {row.school} | ID:{row.id} |  GPA:{row.gpa}")
        sanity_check = [row.id[-1] for row in students]
        
        while True:
            student_pk = input("Select Student ID to update - last digit only or Q to quit ")
            
            if student_pk.lower() == "q":
                print("bye!")
                break
            elif student_pk not in sanity_check:
                print("enter only a valid digit")
                continue
            else:
                student = cls.one_student(student_pk)
                print(f"{student.fname} {student.lname} is enrolled in {student.school} ")
                switch = input("To switch schools - type \"Y\" or \"N\" to return ")
                if switch.lower() not in ["y", "n"]:
                    print("please type only Y or N")
                    continue 
                elif switch.lower() == "n":
                    print("bye!")
                    break
                else: 
                    if student.school == "NYC":
                        student.school = "Houston"
                        student.save()
                        print("student updated")
                        return 
                    elif student.school == "Houston":
                        student.school = "NYC"
                        student.save()
                        print("student updated")
                        return 
    
    #GET GPA'S
    @classmethod
    def get_students_by(cls):
        school = input("Type the school NYC or Houston ")
        gpa = input("type the student GPAs to return ")
        # not making validations here to save time
        results = cls.get_all_by(
            "WHERE school = ? AND gpa >= ?",(school, gpa)
        )
        for row in results:
            print("here are your results")
            print(f"NAME: {row.fname} {row.lname} | SCHOOL: {row.school} | ID:{row.id} |  GPA:{row.gpa}")


if __name__ == "__main__":
    student = Students()
    student.update_schools()
    student.get_students_by()