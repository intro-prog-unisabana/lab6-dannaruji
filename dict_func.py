# Write your code here!
def employee_print(employee_info):
    Name = employee_info.get("Name", "N/A")
    Salary = employee_info.get("Salary", "N/A")
    Role = employee_info.get("Role", "N/A")

    print(f"Name: {Name}")
    print(f"Salary: {Salary}")
    print(f"Role: {Role}")
    