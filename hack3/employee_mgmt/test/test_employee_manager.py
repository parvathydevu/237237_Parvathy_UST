import unittest
from employee_manager import EmployeeManagement

class TestEmployeeManager(unittest.TestCase):
    def setUp(self):
        self.sm = EmployeeManagement()
       
    def test_add_and_view(self):
        self.sm.add_employee("Anu", "MM","ABCD",10000,10,100)
        self.sm.add_employee("Deva", "MR","ABC",10000,20,100)
        self.sm.add_employee("Naveen","IR","ABD",10000,15,100)
        employees = self.sm.view_details()
        self.assertEqual(len(employees), 6)
       
    def test_search(self):
        student = self.sm.add_employee("Anu", "MM","ABCD",10000,10,100)
        result = self.sm.search_data(student.student_id)
        self.assertIsNotNone(result)
        self.assertEqual(result.name, "Anu")
        self.assertEqual(result.department, "MM")
        self.assertEqual(result.designation, "ABCD")
        self.assertEqual(result.gross_salary, 10000)
        self.assertEqual(result.gross_salary, 10000)
       
    def test_delete(self):
        student = self.sm.add_student("Deva", "MR","ABC",10000,20,100)
        self.sm.add_student("Deva", 9, "B")
        result = self.sm.delete_data(student.student_id)
        self.assertTrue(result)
        self.assertEqual(len(self.sm.view_details()), 1)
       
    def test_delete_nonexistent_data(self):
        result = self.sm.delete_data("non-existent-id")
        self.assertFalse(result)
       
    def tearDown(self):
        return None
