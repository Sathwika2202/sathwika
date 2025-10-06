class Student:
    """
    Represents a student with a name, age, and a list of marks.
    """

    def __init__(self, name, age, marks):
        """
        Initialize a Student instance.

        Args:
            name (str): The student's name.
            age (int): The student's age.
            marks (list of float): The student's marks in subjects.
        """
        self.name = name
        self.age = age
        self.marks = marks

    def show_details(self):
        """
        Prints the student's name and age in a readable format.
        """
        print(f"Name: {self.name}\nAge: {self.age}")

    def total_marks(self):
        """
        Returns the total of the student's marks.

        Returns:
            float: The sum of all marks.
        """
        return sum(self.marks)

if __name__ == "__main__":
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    marks = []
    for i in range(1, 4):
        mark = float(input(f"Enter mark {i}: "))
        marks.append(mark)
    student = Student(name, age, marks)
    print("\nStudent Details:")
    student.show_details()
    print(f"Total Marks: {student.total_marks()}")
