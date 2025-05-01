import unittest
from finance_tools import *

class TestFinanceTools(unittest.TestCase):

    def test_calculate_emi(self):
        self.assertAlmostEqual(calculate_emi(100000, 10, 5), 2124.70, places=2)
        with self.assertRaises(ValueError):
            calculate_emi(-100000, 10, 5)

    def test_calculate_sip(self):
        self.assertAlmostEqual(calculate_sip(1000, 12, 10), 232339.08, places=2)
        with self.assertRaises(ValueError):
            calculate_sip(-1000, 12, 10)

    def test_calculate_fd(self):
        self.assertAlmostEqual(calculate_fd(100000, 7, 5), 140255.17, places=2)
        with self.assertRaises(ValueError):
            calculate_fd(-100000, 7, 5)

    def test_calculate_rd(self):
        self.assertAlmostEqual(calculate_rd(1000, 6, 5), 70118.88, places=2)
        with self.assertRaises(ValueError):
            calculate_rd(-1000, 6, 5)

    def test_estimate_retirement_corpus(self):
        self.assertAlmostEqual(estimate_retirement_corpus(50000, 1000, 8, 20), 839287.36, places=2)
        with self.assertRaises(ValueError):
            estimate_retirement_corpus(-50000, 1000, 8, 20)

    def test_estimate_home_loan_eligibility(self):
        self.assertAlmostEqual(estimate_home_loan_eligibility(50000, 20000, 8, 20), 3586628.75, places=2)
        with self.assertRaises(ValueError):
            estimate_home_loan_eligibility(-50000, 20000, 8, 20)

    def test_calculate_credit_card_balance(self):
        self.assertAlmostEqual(calculate_credit_card_balance(10000, 18, 500, 12), 5435.58, places=2)
        with self.assertRaises(ValueError):
            calculate_credit_card_balance(-10000, 18, 500, 12)

    def test_calculate_taxable_income(self):
        self.assertEqual(calculate_taxable_income(100000, 20000), 80000)
        with self.assertRaises(ValueError):
            calculate_taxable_income(-100000, 20000)

    def test_plan_budget(self):
        self.assertEqual(plan_budget(50000, 30000), {
            "savings": 20000,
            "investment": 10000,
            "emergency_fund": 6000,
            "discretionary_spending": 4000
        })
        with self.assertRaises(ValueError):
            plan_budget(-50000, 30000)

    def test_calculate_net_worth(self):
        self.assertEqual(calculate_net_worth(500000, 200000), 300000)
        with self.assertRaises(ValueError):
            calculate_net_worth(-500000, 200000)

if __name__ == '__main__':
    unittest.main()
