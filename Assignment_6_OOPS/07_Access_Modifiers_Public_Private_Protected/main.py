# Create a class Employee with: public variable name,protected variable _salary, and
# private variable __ssn.
# Try accessing all three variables from an object of the class and document what happens.


class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name #public
        self._salary = salary # protected
        self.__ssn = ssn #private

if __name__ == "__main__":
    emp = Employee("Ali", 10000, "011-234-56789")

    # access public variable
    print("Private Variable:", emp.name)

    # access protected variable
    print("Protected Variable:", emp._salary)

    # access private variable
    try:
        print("Private Variable:", emp.__ssn)
    except AttributeError:
        print("Cannot access in Private Variable.__ssn")


# class Employee:
#     def __init__(self, name, salary, ssn):
#         self.name = name    # public
#         self._salary = salary   # protected
#         self.__ssn = ssn    # private

#     def get_ssn(self):
#         return self.__ssn
    
#     def set_salary(self, new_salary):
#         if new_salary > 0:
#             self._salary = new_salary
#         else:
#             print("Salary must be positive in number")

#     def display(self):
#         print(f"Name: {self.name}") # public
#         print(f"Salary: {self._salary}") # protected
#         print(f"SSN: {self.__ssn}") # private

# class Manager(Employee):
#     def __init__(self, name, salary, ssn, department):
#         super().__init__(name, salary, ssn)
#         self.department = department

#     def show_manager_info(self):
#         print(f"Manager: {self.name}")
#         print(f"Department: {self.department}")
#         print(f"Protected: {self._salary}")
#         print(f"Acessing SSN via getter comand: {self.get_ssn}") # private variable

# m = Manager("Ali", "12000", "444-852-2025", "Information Technology")
# m.show_manager_info()
# m.set_salary(32000)

# print("Update Salary: ", m._salary)
# #print(m.__ssn)
# print("Private SSN via managed:", m._Employee__ssn)
