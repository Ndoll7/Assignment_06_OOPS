class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display(self):
        print(f"Employee Name: {self.name}, ID: {self.emp_id}")

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation: uses an existing Employee object

    def show_details(self):
        print(f"Department: {self.dept_name}")
        self.employee.display()  # Accessing method of aggregated object

# Create an independent Employee object
emp = Employee("John ", 1001)

# Pass the employee to a Department (aggregation)
dept = Department("HR", emp)

# Show details
dept.show_details()
