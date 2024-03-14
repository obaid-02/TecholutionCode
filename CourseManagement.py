class Student:
    """
    Represents a student with a name, ID, and grades.
    """
    def __init__(self, name, student_id, grades=None):
        """
        Initializes a new Student object.
        
        Parameters:
            name (str): The name of the student.
            student_id (str): The unique ID of the student.
            grades (list, optional): A list of grades for the student. Defaults to an empty list.
        """
        self.name = name
        self.student_id = student_id
        self.grades = grades or []

    def add_grade(self, grade):
        """
        Adds a grade to the student's list of grades. Can handle single grade or a list of grades.

        Parameters:
            grade (float or list): A single grade (float) or a list of grades to be added.
        """
        if isinstance(grade, list):
            self.grades.extend(grade)
        else:
            self.grades.append(grade)

    def calculate_gpa(self):
        """
        Calculates and returns the GPA of the student.

        Returns:
            float: The GPA of the student.
        """
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        """
        Returns a string representation of the Student object.
        
        Returns:
            str: A string that includes the student's name, ID, and GPA.
        """
        return f"Student: {self.name}, ID: {self.student_id}, Average GPA: {self.calculate_gpa():.2f}"

class Course:
    """
    Represents a course with a name and enrolled students.
    """
    def __init__(self, course_name):
        """
        Initializes a new Course object.

        Parameters:
            course_name (str): The name of the course.
        """
        self.course_name = course_name
        self.enrolled_students = []

    def add_student(self, student):
        """
        Adds a Student object to the course.

        Parameters:
            student (Student): The student to add to the course.
        """
        self.enrolled_students.append(student)

    def remove_student(self, student_id):
        """
        Removes a student from the course by their ID.

        Parameters:
            student_id (str): The ID of the student to remove.
        """
        self.enrolled_students = [student for student in self.enrolled_students if student.student_id != student_id]

    def find_student(self, student_id):
        """
        Searches for and returns a student by their ID.

        Parameters:
            student_id (str): The ID of the student to find.

        Returns:
            Student or None: The found student object or None if not found.
        """
        for student in self.enrolled_students:
            if student.student_id == student_id:
                return student
        return None

    def __str__(self):
        """
        Returns a string representation of the Course object.

        Returns:
            str: A string that includes the course name and details of enrolled students.
        """
        course_info = f"Course: {self.course_name}\n"
        students_info = "\n".join(str(student) for student in self.enrolled_students)
        return course_info + "Enrolled students:\n" + students_info if students_info else course_info + "No students enrolled."

def main_menu(course):
    """
    Displays the main menu and handles user interaction for managing a course.

    Parameters:
        course (Course): The course to manage.
    """
    while True:
        print("\nCourse Management System")
        print("1. Add a student")
        print("2. Remove a student")
        print("3. Search for a student")
        print("4. Display all students")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            # Adding a student along with grades
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            grades_input = input("Enter grades separated by space (hit enter if none): ")
            grades = [float(grade) for grade in grades_input.split()] if grades_input else []
            student = Student(name, student_id, grades)
            course.add_student(student)
            print("Student added successfully.")
        elif choice == '2':
            # Removing a student by ID
            student_id = input("Enter student ID to remove: ")
            course.remove_student(student_id)
            print("Student removed successfully.")
        elif choice == '3':
            # Searching for a student by ID
            student_id = input("Enter student ID to search for: ")
            student = course.find_student(student_id)
            if student:
                print(f"Student found: {student}")
            else:
                print("Student not found.")
        elif choice == '4':
            # Displaying all students in the course
            print("\nCurrent Course Enrollment:")
            print(course)
        elif choice == '5':
            # Exiting the program
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Example usage
if __name__ == "__main__":
    course_name = input("Enter the course name to manage: ")
    course = Course(course_name)
    main_menu(course)
