class Student:
  """
  This class represents a student with attributes and a method to calculate GPA.
  """
  def __init__(self, name, student_id, grades):
    self.name = name
    self.student_id = student_id
    self.grades = grades  # List of grades

  def calculate_gpa(self):
    """
    Calculates the GPA of the student based on their grades.
    Returns the GPA as a float or 0.0 if no grades are available.
    """
    if not self.grades:
      return 0.0
    return sum(self.grades) / len(self.grades)


class Course:
  """
  This class represents a course with attributes and methods to manage students.
  """
  def __init__(self, course_name):
    self.course_name = course_name
    self.enrolled_students = []  # List of Student objects

  def add_student(self, student):
    """
    Adds a student to the course.
    """
    self.enrolled_students.append(student)

  def remove_student(self, student_id):
    """
    Removes a student from the course based on their ID.
    Returns True if successful, False otherwise.
    """
    for student in self.enrolled_students:
      if student.student_id == student_id:
        self.enrolled_students.remove(student)
        return True
    return False  # Student not found

  def calculate_average_gpa(self):
    """
    Calculates the average GPA of all students enrolled in the course.
    Returns the average GPA as a float or 0.0 if no students are enrolled.
    """
    if not self.enrolled_students:
      return 0.0
    total_gpa = 0
    for student in self.enrolled_students:
      total_gpa += student.calculate_gpa()
    return total_gpa / len(self.enrolled_students)


# Example usage
student1 = Student("Ubaid", 12365, [95, 99, 100])
student2 = Student("Sanyam", 64721, [95, 88, 92])

course1 = Course("Machine Learning")
course1.add_student(student1)
course1.add_student(student2)

average_gpa = course1.calculate_average_gpa()
print(f"Average GPA for {course1.course_name}: {average_gpa:.2f}")

# Remove student with ID 64721
if course1.remove_student(64721):
    print(f"Student with ID 64721 and Name {student2.name} has been removed from {course1.course_name}")
else:
    print(f"Student with ID 64721 not found in {course1.course_name}")
