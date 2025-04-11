import uuid
 
class employees:
    def __init__(self, name, department, designation, gross_salary, tax, bonus, id=None):
        self.id = id if id else str(uuid.uuid4())
        self.name = name
        self.department = department
        self.designation = designation
        self.gross_salary = gross_salary
        self.tax = tax
        self.bonus = bonus
        #Employee.net_sal(self,self.tax,self.bonus, self.gross_salary)
        self.net_salary = employees.net_sal(self,self.tax,self.bonus, self.gross_salary)
 
    def net_sal(self,tax,bonus,gross_salary):
        self.net_salary = self.gross_salary - (self.gross_salary * self.tax / 100) + self.bonus
        return self.net_salary
       
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'department': self.department,
            'designation': self.designation,
            'gross_salary': self.gross_salary,
            'tax': self.tax,
            'bonus': self.bonus,
            #'netsalary': self.netsalary
        }
       
    @staticmethod
    def from_dict(data):
        return employees(
            name=data['name'],
            department=data['department'],
            designation=data['designation'],
            gross_salary=data['gross_salary'],
            tax=data['tax'],
            bonus=data['bonus'],
            id=data['id']
        )
       
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Department: {self.department}, Designation: {self.designation}, Gross Salary: {self.gross_salary}, Tax: {self.tax}, Bonus: {self.bonus}"

