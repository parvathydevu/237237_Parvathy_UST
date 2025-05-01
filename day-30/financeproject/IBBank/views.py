from django.shortcuts import render,redirect
from finance_app.finance_tools import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import UserRegisterForm, DepositForm, WithdrawForm
from .models import Profile,Transaction

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'IBBank/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in!')
            return redirect('dashboard')  #dashboard.html
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'IBBank/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
@login_required
def dashboard(request):
    profile = request.user.profile
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    return render(request, 'IBBank/dashboard.html', {'profile': profile,'transactions': transactions})

@login_required
def deposit(request):
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data.get('amount')
            request.user.profile.balance += amount
            request.user.profile.save()
            Transaction.objects.create(user=request.user, type='Deposit', amount=amount)
            messages.success(request, f'{amount} deposited successfully!')
            return redirect('dashboard')
    else:
        form = DepositForm()
    return render(request, 'IBBank/deposit.html', {'form': form})
 
@login_required
def withdraw(request):
    if request.method == 'POST':
        form = WithdrawForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data.get('amount')
            if request.user.profile.balance >= amount:
                request.user.profile.balance -= amount
                request.user.profile.save()
                Transaction.objects.create(user=request.user, type='Withdraw', amount=amount)
                messages.success(request, f'{amount} withdrawn successfully!')
            else:
                messages.error(request, 'Insufficient balance')
            return redirect('dashboard')
    else:
        form = WithdrawForm()
    return render(request, 'IBBank/withdraw.html', {'form': form})
#access financialtools
def financial_tools(request):
    return render(request, 'IBBank/financial-tools.html')

 
def emi_view(request):
    context = {}
    if request.method == 'POST':
        try:
            principal = validate_positive_float(float(request.POST.get('principal')), "Principal")
            rate = validate_positive_float(float(request.POST.get('rate')), "Interest Rate")
            tenure = validate_positive_int(int(request.POST.get('tenure')), "Tenure")
 
            emi = calculate_emi(principal, rate, tenure)
            context['emi'] = round(emi, 2)
            context['success'] = True
 
        except Exception as e:
            context['error'] = str(e)
 
    return render(request, 'IBBank/emi_form.html', context)
def sip_calculator_view(request):
    context = {}
    if request.method == 'POST':
        try:
            monthly_investment = float(request.POST.get('monthly_investment'))
            annual_rate = float(request.POST.get('annual_rate'))
            years = int(request.POST.get('years'))
 
            maturity = calculate_sip(monthly_investment, annual_rate, years)
            context['maturity'] = maturity
            context['success'] = True
 
        except Exception as e:
            context['error'] = str(e)
 
    return render(request, 'IBBank/sip_form.html', context)
def fd_calculator_view(request):
    context = {}
    if request.method == 'POST':
        try:
            principal = float(request.POST.get('principal'))
            annual_rate = float(request.POST.get('annual_rate'))
            years = int(request.POST.get('years'))
 
            maturity = calculate_fd(principal, annual_rate, years)
            context['maturity'] = maturity
            context['success'] = True
 
        except Exception as e:
            context['error'] = str(e)
 
    return render(request, 'IBBank/fd_form.html', context)
def rd_calculator_view(request):
    context = {}
    if request.method == 'POST':
        try:
            monthly_deposit = float(request.POST.get('monthly_deposit'))
            annual_rate = float(request.POST.get('annual_rate'))
            years = int(request.POST.get('years'))
 
            maturity = calculate_rd(monthly_deposit, annual_rate, years)
            context['maturity'] = maturity
            context['success'] = True
        except Exception as e:
            context['error'] = str(e)
 
    return render(request, 'IBBank/rd_form.html', context)
def retirement_savings_view(request):
    context = {}
    if request.method == 'POST':
        try:
            current_savings = float(request.POST.get('current_savings'))
            monthly_contribution = float(request.POST.get('monthly_contribution'))
            annual_rate = float(request.POST.get('annual_rate'))
            years = int(request.POST.get('years'))
 
            future_value = estimate_retirement_corpus(
                current_savings, monthly_contribution, annual_rate, years
            )
            context['future_value'] = future_value
            context['success'] = True
        except Exception as e:
            context['error'] = str(e)
 
    return render(request, 'IBBank/retirement_form.html', context)
def home_loan_eligibility_view(request):
    context = {}
    if request.method == 'POST':
        try:
            monthly_income = float(request.POST.get('monthly_income'))
            monthly_expenses = float(request.POST.get('monthly_expenses'))
            loan_tenure_years = int(request.POST.get('loan_tenure_years'))
            annual_rate = float(request.POST.get('annual_rate'))
 
            eligibility = estimate_home_loan_eligibility(
                monthly_income, monthly_expenses, loan_tenure_years, annual_rate
            )
            context['eligibility'] = eligibility
            context['success'] = True
        except Exception as e:
            context['error'] = str(e)
 
    return render(request, 'IBBank/home_loan_eligibility.html', context)
def credit_card_interest_view(request):
    context = {}
    if request.method == 'POST':
        try:
            balance = float(request.POST.get('balance'))
            annual_rate = float(request.POST.get('annual_rate'))
            months = int(request.POST.get('months'))
            min_payment_percent = float(request.POST.get('min_payment_percent'))
 
            final_balance = calculate_credit_card_balance(
                balance, annual_rate, months, min_payment_percent
            )
            context['final_balance'] = final_balance
            context['success'] = True
        except Exception as e:
            context['error'] = str(e)
 
    return render(request, 'IBBank/credit_card_interest.html', context)
def taxable_income_view(request):
    context = {}
    if request.method == 'POST':
        try:
            gross_income = float(request.POST.get('gross_income'))
            deductions = float(request.POST.get('deductions'))
 
            taxable_income = calculate_taxable_income(gross_income, deductions)
            context['taxable_income'] = taxable_income
            context['success'] = True
        except Exception as e:
            context['error'] = str(e)
    return render(request, 'IBBank/taxable_income.html', context)
def budget_planner_view(request):
    context = {}
    if request.method == 'POST':
        try:
            income = float(request.POST.get('income'))
            expenses = float(request.POST.get('expenses'))
 
            plan = plan_budget(income, expenses)
            context['plan'] = plan
            context['success'] = True
        except Exception as e:
            context['error'] = str(e)
    return render(request, 'IBBank/simple_budget_planner.html', context)
def net_worth_view(request):
    net_worth = None  # Variable to hold the result
 
    if request.method == 'POST':
        try:
            # Retrieve and convert form data
            assets = float(request.POST.get('assets', 0))
            liabilities = float(request.POST.get('liabilities', 0))
 
            # Calculate net worth using the function
            net_worth = calculate_net_worth(assets, liabilities)
        except ValueError:
            # Handle invalid input
            error_message = "Please enter valid numbers for both assets and liabilities."
            return render(request, 'IBBank/net_worth_calculator.html', {'error_message': error_message})
 
    # Render the form and the result
    return render(request, 'IBBank/net_worth_calculator.html', {'net_worth': net_worth})