def initialize_dict(student_name, subject_grades):
    student_name = student_name.title()
    
    new_dict = {
        student_name: {}
    }
    
    for subject, grade in subject_grades.items():
        new_dict[student_name][subject.title()] = float(grade)
    
    return new_dict


def add_student(student_grades=None):
    if student_grades is None:
        student_grades = {}
    
    student_name = input("Enter student name: ").title()
    
    subjects = {}
    
    while True:
        entry = input("Enter subject and grade (or 'exit' to finish): ")
        
        if entry.lower() == "exit":
            break
        
        subject, grade = entry.split(",")
        subjects[subject.strip().title()] = float(grade)
    
    student_grades[student_name] = subjects
    
    print(f"Student {student_name} successfully added to the grades management system.")
    
    return student_grades


def get_students(student_grades, keys):
    result = {}
    
    for name in keys:
        found = False
        
        for student in student_grades:
            if student.lower() == name.lower():
                result[student] = student_grades[student]
                found = True
                break
        
        if not found:
            print(f"{name.title()} not found!")
    
    return result

def avg_by_student(student_grades, selected_students=None):
    
    if selected_students is None:
        selected_students = list(student_grades.keys())
    
    for name in selected_students:
        found = False
        
        for student in student_grades:
            if student.lower() == name.lower():
                grades = student_grades[student].values()
                avg = (sum(grades) / len(grades), 1)
                
                print(f"{student}: {avg}")
                found = True
                break
        
        if not found:
            print(f"{name.title()} not found!")