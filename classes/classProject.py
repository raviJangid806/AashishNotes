class Student:
    def __init__(self, name: str, roll_no: int, marks: list[int]):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def total_marks(self) -> int:
        return sum(self.marks)

    def average(self) -> float:
        if not self.marks:
            return 0.0
        return self.total_marks() / len(self.marks)

    def grade(self) -> str:
        avg = self.average()
        if avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        else:
            return "F"

    def print_report(self) -> None:
        print(f"Student: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print("Marks:")
        for index, mark in enumerate(self.marks, start=1):
            print(f"  Subject {index}: {mark}")
        print(f"Total: {self.total_marks()}")
        print(f"Average: {self.average():.2f}")
        print(f"Grade: {self.grade()}")
        print("---------------------------")


class Classroom:
    def __init__(self) -> None:
        self.students: list[Student] = []

    def add_student(self, student: Student) -> None:
        self.students.append(student)

    def get_top_student(self) -> Student | None:
        if not self.students:
            return None
        top = self.students[0]
        for student in self.students[1:]:
            if student.total_marks() > top.total_marks():
                top = student
        return top

    def class_summary(self) -> None:
        if not self.students:
            print("No students in the class yet.")
            return
        print("Class Summary")
        print(f"Total students: {len(self.students)}")
        print("Student averages:")
        for student in self.students:
            print(f"  {student.name}: {student.average():.2f}")
        top_student = self.get_top_student()
        if top_student:
            print(f"Top student: {top_student.name} ({top_student.total_marks()} marks)")


def create_sample_classroom() -> Classroom:
    classroom = Classroom()
    classroom.add_student(Student("Aashish", 1, [88, 92, 79]))
    classroom.add_student(Student("Priya", 2, [95, 91, 93]))
    classroom.add_student(Student("Rohit", 3, [67, 73, 70]))
    classroom.add_student(Student("Neha", 4, [82, 78, 85]))
    return classroom



classroom = create_sample_classroom()
for student in classroom.students:
    student.print_report()
classroom.class_summary()
