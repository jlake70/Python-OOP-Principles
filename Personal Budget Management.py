class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget  
    
    
    def get_category_name(self):
        return self.__category_name
    
    
    def set_category_name(self, category_name):
        self.__category_name = category_name
    
    
    def get_allocated_budget(self):
        return self.__allocated_budget
    
    
    def set_allocated_budget(self, allocated_budget):
        if allocated_budget < 0:
            raise ValueError("Budget should be a positive number")
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget  
    
    
    def get_remaining_budget(self):
        return self.__remaining_budget
    
    
    def add_expense(self, expense_amount):
        if expense_amount < 0:
            raise ValueError("Expense amount should be a positive number")
        if expense_amount > self.__remaining_budget:
            raise ValueError("Insufficient budget")
        self.__remaining_budget -= expense_amount
    
    
    def display_budget_details(self):
        return (f"Category: {self.__category_name}\n"
                f"Allocated Budget: {self.__allocated_budget}\n"
                f"Remaining Budget: {self.__remaining_budget}")

def main():
    categories = {}
    
    while True:
        print("\nPersonal Budget Management")
        print("1. Create a new budget category")
        print("2. Add expense to a category")
        print("3. View budget details")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            category_name = input("Enter category name: ")
            allocated_budget = float(input("Enter allocated budget: "))
            categories[category_name] = BudgetCategory(category_name, allocated_budget)
            print(f"Budget category '{category_name}' created with a budget of {allocated_budget}.")

        elif choice == "2":
            category_name = input("Enter category name: ")
            if category_name in categories:
                expense_amount = float(input("Enter expense amount: "))
                try:
                    categories[category_name].add_expense(expense_amount)
                    print(f"Expense of {expense_amount} added to '{category_name}' category.")
                except ValueError as e:
                    print(e)
            else:
                print("Category not found.")

        elif choice == "3":
            category_name = input("Enter category name: ")
            if category_name in categories:
                print(categories[category_name].display_budget_details())
            else:
                print("Category not found.")

        elif choice == "4":
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")

main()