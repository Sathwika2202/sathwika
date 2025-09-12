# Define the sru_student class

class sru_student:
    # Initialize the student object with name, roll no., and hostel status
    def __init__(self, name, roll_no, hostel_status):
        self.name = name  # Student's name
        self.roll_no = roll_no  # Student's roll number
        self.hostel_status = hostel_status  # Hostel status (Yes/No)
        self.fee_paid = False  # Fee payment status, default is False

    # Method to update the fee status
    def fee_update(self, status):
        self.fee_paid = status  # Update fee payment status

    # Method to display student details
    def display_details(self):
        print("Name:", self.name)  # Print student's name
        print("Roll No.:", self.roll_no)  # Print roll number
        print("Hostel Status:", self.hostel_status)  # Print hostel status
        print("Fee Paid:", "Yes" if self.fee_paid else "No")  # Print fee status


# Example usage:
# Create a student object
student1 = sru_student("Amit Sharma", "SRU123", "Yes")

# Update fee status to paid
student1.fee_update(True)

# Display student details
student1.display_details()

"""
Module for representing SRU student information and operations.
Classes:
    sru_student:
        Represents a student at SRU with attributes for name, roll number, hostel status, and fee payment status.
        Methods:
            init(name, roll_no, hostel_status):
                Initializes a new student with the given name, roll number, and hostel status.
                Sets fee payment status to False by default.
            fee_update(status):
                Updates the fee payment status of the student.
            display_details():
                Prints the student's details including name, roll number, hostel status, and fee payment status.
"""

