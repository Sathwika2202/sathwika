
def parse_student_info(student_dict):
    
    full_name = student_dict.get('name')
    details = student_dict.get('details', {})
    branch = details.get('branch')
    sgpa = details.get('sgpa')
    return (full_name, branch, sgpa)

# Example usage:
student1 = {'name': 'radha', 'details': {'branch': 'cse', 'sgpa': 9}}
student2 = {'name': 'krishna', 'details': {'branch': 'ece', 'sgpa': 9.5}}
student3 = {'name': 'ravi', 'details': {'branch': 'eee', 'sgpa': 8}}

print(parse_student_info(student1))  # Output: ('radha', 'cse', 9)
print(parse_student_info(student2))  # Output: ('krishna', 'ece', 9.5)
print(parse_student_info(student3))  # Output: ('ravi', 'eee', 8)