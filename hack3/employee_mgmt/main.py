from employee_manager import employeeManager
from storage import Storage
 

def display_std(details: list) -> None:
    if not details:
        print("No data to display")
    else:
        for i in details:
            print(f"ID: {i.id}, Name: {i.name}, Department: {i.department}, Designation: {i.designation}, Gross Salary: {i.gross_salary}, Tax: {i.tax}, Bonus: {i.bonus}")

 
def main():
 
    manager = employeeManager()
    store = Storage()
 
    saved_stds = store.load()
    manager.load_std(saved_stds)
 
    while True:
 
        print("TODO Application: ")
        print("\n1. Add employee\n2. View all employees\n3.Search employee by ID\n4. Delete employee\n5. Exit\n")
        choice = input("Choice -> ")
 
        if choice == '1':
            name = str(input("Enter a name: "))
            department = str(input("Enter the department: "))
            designation = str(input("Enter the designation: "))
            gross_salary = int(input("Enter gross salary: "))
            tax= int(input("Enter the tax: "))
            bonus= int(input("Enter the bonus: "))
            employees = manager.add_std(name,department,designation,gross_salary,tax,bonus)
            store.save(manager.to_dict_list())
            print(f"Employee added with ID: {employees.id}")
 
        elif choice == '2':
            display_std(manager.get_all_std())
        elif choice == '3':
            tid = input("Enter the employee ID to search: ")
            result = manager.search_ID(tid)
            if (result):
                print(result)
                store.save(manager.to_dict_list())
                print("Search data")
            else:
                print("Employee ID not found")
               
        elif choice == '4':
            tid = input("Enter the ID to delete: ")
            if manager.delete_std(tid):
                store.save(manager.to_dict_list())
                print("Employee details Deleted")
            else:
                print("Employee ID not found")
        elif choice == '5':
            print("Goodbye !")
            break
        else:
            print("Invalid Choice")
 
if __name__ == "__main__":
 
    main()



##############