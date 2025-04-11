import unittest
from employee import employees

class TestStudent(unittest.TestCase):

    def test_student_creation(self):
        t = employees("Devika", "MM","ABCD",10000,10,100)
        self.assertEqual(t.name, "Devika")
        self.assertEqual(t.department,"MM" )
        self.assertEqual(t.designation, "ABCD")
        self.assertEqual(t.gross_salary, 10000)
        self.assertEqual(t.tax,10)
        self.assertEqual(t.bonus,100)

    def test_to_dict_and_from_dict(self):
        t1 = employees("Devika", "MM","ABCD",10000,10,100)
        d = t1.to_dict()
        t2 = employees.from_dict(d)
        self.assertEqual(t1.name, t2.name)
        self.assertEqual(t1.department, t2.department)
        self.assertEqual(t1.designation, t2.designation)
        self.assertEqual(t1.gross_salary, t2.gross_salary)
        self.assertEqual(t1.tax, t2.tax)
        self.assertEqual(t1.bonus, t2.bonus)

if __name__ == "__main__":
    unittest.main()