import unittest
import uuid
 
from employee_manager import Employeemanagement
 
 
class TestEmployeeManagement(unittest.TestCase):
    def setUp(self):
        self.emp = Employeemanagement()
       
    def test_add_and_view(self):
        self.emp.add_employee("Adithi", "IT", "Developer", 3600000, 5, 10000)
        self.emp.add_employee("Deva", "HR", "Manager", 170000, 15, 23000)
        self.emp.add_employee("Hema", "Operations", "Supervisor", 160000, 10, 15000)
        emp = self.emp.view_details()
        self.assertEqual(len(emp), 3)
       
    def test_search(self):
        emp = self.emp.add_employee("Adithi", "IT", "Developer", 3600000, 5, 10000)
        result = self.emp.search_by_id(emp.emp_id)
        self.assertIsNotNone(result)
        self.assertEqual(result.name, "Adithi")
        self.assertEqual(result.department, "IT")
        self.assertEqual(result.designation, "Developer")
        self.assertEqual(result.gross_salary, 3600000)
        self.assertEqual(result.tax, 5)
        self.assertEqual(result.bonus, 10000)
       
    def test_delete(self):
        emp = self.emp.add_employee("Deva", "HR", "Manager", 170000, 15, 23000)
        self.emp.add_employee("Hema", "Operations", "Supervisor", 160000, 10, 15000)
        result = self.emp.delete_by_name(emp.name)
        self.assertTrue(result)
        self.assertEqual(len(self.emp.view_details()), 1)
       
    def test_delete_nonexistent_data(self):
        result = self.emp.delete_by_name("invalid-name")
        self.assertFalse(result)
       
    def test_to_dict_list_and_load(self):
        self.emp.add_employee("Arya", "Design", "Artist", 1200000, 8, 5000)
        dict_list = self.emp.to_dict_list()
        self.assertEqual(len(dict_list), 1)
        self.assertEqual(dict_list[0]["Name"], "Arya")
 
        new_emp = Employeemanagement()
        new_emp.load_emp_details(dict_list)
        self.assertEqual(len(new_emp.employee_list), 1)
        self.assertEqual(new_emp.employee_list[0].name, "Arya")
 
    def tearDown(self):
        return None