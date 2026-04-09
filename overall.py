def student_averages(students):
    averages = {}
    
    for student, grades in students.items():
        total = sum(grades.values())
        avg = round(total / len(grades))
        averages[student] = avg
    
    return averages


def assignment_averages(students):
    totals = {}
    counts = {}
    
    for student in students:
        for task, grade in students[student].items():
            totals[task] = totals.get(task, 0) + grade
            counts[task] = counts.get(task, 0) + 1
    
    averages = {}
    
    for task in totals:
        averages[task] = round(totals[task] / counts[task])
    
    return averages
