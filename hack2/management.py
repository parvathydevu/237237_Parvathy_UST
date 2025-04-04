import json

class Person:
    #Constructor
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
    
class Employee(Person):  #inherits from Person
    def __init__(self, name, age, gender, emp_id, department, salary):
        super().__init__(name, age, gender)
        self.emp_id=emp_id
        self.department=department
        self.salary=salary
    def get_details(self):
        return f"{super().get_details()}, Emp ID: {self.emp_id}, Department: {self.department}, Salary: {self.salary}"
    def is_eligible_for_bonus(self):
        if self.salary<5000:
            return True
        else:
            return False
        
    #class method
    def from_string(cls, data_string):
        sample= data_string.split(',')
        name = sample[0]
        age = int(sample[1])
        gender = sample[2]
        emp_id = sample[3]
        department = sample[4]
        salary = int(sample[5])
        return cls(name, age, gender, emp_id, department, salary)
    from_string=classmethod(from_string)

    #static method
    def bonus_policy():
        print("<-----Bonus policy----->")
        print("Employees earning less than ₹50,000 are eligible for bonuses")
    bonus_policy=staticmethod(bonus_policy)
class Department:
    def __init__(self,name):
        self.name=name
        self.employees=[]  #assign an empty list..append employee details->all
    def add_employee(self,employee):
        return self.employees.append(employee)  #.append employee details->all
    def get_average_salary(self):
        if not self.employees:
            return 0
        total = sum(emp.salary for emp in self.employees)
        return total/ len(self.employees)
    def get_all_employees(self):
        return self.employees

# save to json file
def save_to_json(employees, filename="employees.json"):
    data = []
    for x in employees:
        data.append({
            "name": x.name,
            "age": x.age,
            "gender": x.gender,
            "emp_id": x.emp_id,
            "department": x.department,
            "salary": x.salary
        })
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
#
#Read JSON data from a saved file (employees.json) and load it into a Python dict
#save it
def load_from_json(filename="employees.json"):
    with open(filename, 'r') as f:
        data = json.load(f)
    employees = []
    for emp_data in data:
        emp = Employee(
            name=emp_data['name'],
            age=emp_data['age'],
            gender=emp_data['gender'],
            emp_id=emp_data['emp_id'],
            department=emp_data['department'],
            salary=emp_data['salary']
        )
        employees.append(emp)
    return employees
 

