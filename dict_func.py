# Write your code here!
def employee_print(employee_info):
    Name = employee_info.get("Name", "N/A")
    Salary = employee_info.get("Salary", "N/A")
    Role = employee_info.get("Role", "N/A")

    print(f"Name: {Name}")
    print(f"Salary: {Salary}")
    print(f"Role: {Role}")

    temp_dict = employee_info.copy()
    temp_dict.pop("Name", None)
    temp_dict.pop("Salary", None)
    temp_dict.pop("Role", None)

    if len(temp_dict) == 0:
        print("No other info!")
    else:
        for key, value in temp_dict.items():
            print(f"{key}: {value}")