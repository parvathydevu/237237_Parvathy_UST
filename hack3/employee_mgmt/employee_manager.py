from employee import employees
 
class employeeManager(object):
   
    def __init__(self):
        self.stds =[]  #self.stds-->
       
    #add a new employee
    def add_std(self,name,department,designation,gross_salary,tax,bonus):
        employee = employees(name,department,designation,gross_salary,tax,bonus)
        self.stds.append(employee)
        return employee
   
    #View all employees
    def get_all_std(self):
        return self.stds
   
   
    #search employee by ID
    def search_ID(self,id):
        for employees in self.stds:
            if employees.id == id:
                return employees
            return  None
   
   
    #Delete an employee
    def delete_std(self,id):
        for employees in self.stds:
            if employees.id == id:
                self.stds.remove(employees)
                return True
            return False
   
    #load data 
    def load_std(self,std_dicts):
        self.stds = [employees.from_dict(td) for td in std_dicts]
       
    #list of tasks in dictionary format
    def to_dict_list(self):
        return [employees.to_dict() for employees in self.stds]