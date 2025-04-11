import unittest
import os
from storage import Storage
from employee import Employee
 
 
class TestStorageWithPickle(unittest.TestCase):
 
    def setUp(self):
        self.filename = "test_employee.pkl"
        self.storage = Storage(self.filename)
 
    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
 
    def test_save_and_load_employee_objects(self):
        emp1 = Employee("Deva", "IT", "Manager", 150000, 15, 15000)
        emp2 = Employee("Hima", "HR", "Junior HR", 360000, 5, 10000)
        emp_list = [emp1, emp2]
 
        self.storage.save(emp_list)
        loaded_emp_list = self.storage.load()
 
        self.assertEqual(len(loaded_emp_list), 2)
        self.assertEqual(loaded_emp_list[0].name, "Deva")
        self.assertEqual(loaded_emp_list[1].designation, "Junior HR")
 
    def test_load_when_file_missing(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
        result = self.storage.load()
        self.assertEqual(result, [])