import math

def calculate_emi(principal: float, annual_rate: float, tenure_years: int) -> float:
    """
    Calculates the monthly EMI for a loan.
    
    :param principal: The loan amount.
    :param annual_rate: The annual interest rate (in percentage).
    :param tenure_years: The tenure of the loan (in years).
    :return: The monthly EMI.
    """
    if principal <= 0 or annual_rate <= 0 or tenure_years <= 0:
        raise ValueError("Principal, annual rate, and tenure must be positive values.")
    
    monthly_rate = annual_rate / (12 * 100)
    tenure_months = tenure_years * 12
    emi = principal * monthly_rate * (math.pow(1 + monthly_rate, tenure_months)) / (math.pow(1 + monthly_rate, tenure_months) - 1)
    return emi

def calculate_sip(monthly_investment: float, annual_rate: float, tenure_years: int) -> float:
    """
    Calculates the maturity amount for a Systematic Investment Plan (SIP).
    
    :param monthly_investment: The monthly investment amount.
    :param annual_rate: The annual interest rate (in percentage).
    :param tenure_years: The tenure of the investment (in years).
    :return: The maturity amount.
    """
    if monthly_investment <= 0 or annual_rate <= 0 or tenure_years <= 0:
        raise ValueError("Monthly investment, annual rate, and tenure must be positive values.")
    
    monthly_rate = annual_rate / (12 * 100)
    tenure_months = tenure_years * 12
    maturity_amount = monthly_investment * ((math.pow(1 + monthly_rate, tenure_months) - 1) / monthly_rate) * (1 + monthly_rate)
    return maturity_amount

def calculate_fd(principal: float, annual_rate: float, tenure_years: int) -> float:
    """
    Calculates the maturity amount for a Fixed Deposit (FD).
    
    :param principal: The deposit amount.
    :param annual_rate: The annual interest rate (in percentage).
    :param tenure_years: The tenure of the deposit (in years).
    :return: The maturity amount.
    """
    if principal <= 0 or annual_rate <= 0 or tenure_years <= 0:
        raise ValueError("Principal, annual rate, and tenure must be positive values.")
    
    maturity_amount = principal * math.pow(1 + annual_rate / 100, tenure_years)
    return maturity_amount

def calculate_rd(monthly_deposit: float, annual_rate: float, tenure_years: int) -> float:
    """
    Calculates the maturity amount for a Recurring Deposit (RD).
    
    :param monthly_deposit: The monthly deposit amount.
    :param annual_rate: The annual interest rate (in percentage).
    :param tenure_years: The tenure of the deposit (in years).
    :return: The maturity amount.
    """
    if monthly_deposit <= 0 or annual_rate <= 0 or tenure_years <= 0:
        raise ValueError("Monthly deposit, annual rate, and tenure must be positive values.")
    
    monthly_rate = annual_rate / (12 * 100)
    tenure_months = tenure_years * 12
    maturity_amount = monthly_deposit * ((math.pow(1 + monthly_rate, tenure_months) - 1) / monthly_rate) * (1 + monthly_rate)
    return maturity_amount

def estimate_retirement_corpus(current_savings: float, monthly_addition: float, annual_rate: float, tenure_years: int) -> float:
    """
    Estimates the future retirement corpus based on current savings, monthly addition, and expected returns.
    
    :param current_savings: The current savings amount.
    :param monthly_addition: The monthly addition to savings.
    :param annual_rate: The annual interest rate (in percentage).
    :param tenure_years: The tenure of the savings (in years).
    :return: The estimated retirement corpus.
    """
    if current_savings < 0 or monthly_addition < 0 or annual_rate <= 0 or tenure_years <= 0:
        raise ValueError("Current savings, monthly addition, annual rate, and tenure must be positive values.")
    
    monthly_rate = annual_rate / (12 * 100)
    tenure_months = tenure_years * 12
    future_value = current_savings * math.pow(1 + monthly_rate, tenure_months)
    future_value += monthly_addition * ((math.pow(1 + monthly_rate, tenure_months) - 1) / monthly_rate) * (1 + monthly_rate)
    return future_value

def estimate_home_loan_eligibility(monthly_income: float, monthly_expenses: float, annual_rate: float, tenure_years: int) -> float:
    """
    Estimates the maximum home loan eligibility based on income and expenses.
    
    :param monthly_income: The monthly income.
    :param monthly_expenses: The monthly expenses.
    :param annual_rate: The annual interest rate (in percentage).
    :param tenure_years: The tenure of the loan (in years).
    :return: The maximum loan eligibility.
    """
    if monthly_income <= 0 or monthly_expenses < 0 or annual_rate <= 0 or tenure_years <= 0:
        raise ValueError("Monthly income, monthly expenses, annual rate, and tenure must be positive values.")
    
    disposable_income = monthly_income - monthly_expenses
    monthly_rate = annual_rate / (12 * 100)
    tenure_months = tenure_years * 12
    max_loan = disposable_income * (math.pow(1 + monthly_rate, tenure_months) - 1) / (monthly_rate * math.pow(1 + monthly_rate, tenure_months))
    return max_loan

def calculate_credit_card_balance(principal: float, annual_rate: float, minimum_payment: float, tenure_months: int) -> float:
    """
    Calculates the outstanding balance if minimum payment is made each month.
    
    :param principal: The initial balance.
    :param annual_rate: The annual interest rate (in percentage).
    :param minimum_payment: The minimum payment made each month.
    :param tenure_months: The tenure of the calculation (in months).
    :return: The outstanding balance.
    """
    if principal <= 0 or annual_rate <= 0 or minimum_payment <= 0 or tenure_months <= 0:
        raise ValueError("Principal, annual rate, minimum payment, and tenure must be positive values.")
    
    monthly_rate = annual_rate / (12 * 100)
    balance = principal
    for _ in range(tenure_months):
        balance = balance * (1 + monthly_rate) - minimum_payment
    return balance

def calculate_taxable_income(gross_income: float, deductions: float) -> float:
    """
    Computes the taxable income after considering deductions.
    
    :param gross_income: The gross income.
    :param deductions: The total deductions.
    :return: The taxable income.
    """
    if gross_income < 0 or deductions < 0:
        raise ValueError("Gross income and deductions must be non-negative values.")
    
    taxable_income = gross_income - deductions
    return max(taxable_income, 0)

def plan_budget(monthly_income: float, monthly_expenses: float) -> dict:
    """
    Suggests saving/investing plans based on income vs expenses.
    
    :param monthly_income: The monthly income.
    :param monthly_expenses: The monthly expenses.
    :return: A dictionary with savings and investment suggestions.
    """
    if monthly_income <= 0 or monthly_expenses < 0:
        raise ValueError("Monthly income must be positive and monthly expenses must be non-negative values.")
    
    savings = monthly_income - monthly_expenses
    if savings <= 0:
        return {"message": "No savings possible with current income and expenses."}
    
    investment = savings * 0.5
    emergency_fund = savings * 0.3
    discretionary_spending = savings * 0.2
    return {
        "savings": savings,
        "investment": investment,
        "emergency_fund": emergency_fund,
        "discretionary_spending": discretionary_spending
    }

def calculate_net_worth(assets: float, liabilities: float) -> float:
    """
    Calculates net worth based on assets and liabilities.
    
    :param assets: The total assets.
    :param liabilities: The total liabilities.
    :return: The net worth.
    """
    if assets < 0 or liabilities < 0:
        raise ValueError("Assets and liabilities must be non-negative values.")
    
    net_worth = assets - liabilities
    return net_worth
