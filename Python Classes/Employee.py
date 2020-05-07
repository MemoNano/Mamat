# Python Object-Oriented Programming


class Employee:
    raise_amt = 10.5

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + last + "@company.com"

    def fullname_email(self):
        return '{}, {}, {}'.format(self.first, self.last, self.email)

    def apply_raise(self):
        raised = self.salary = int(self.salary * self.raise_amt)
        return raised

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.salary)


emp_1 = Employee('Corey', "Schafer", 50000)
emp_2 = Employee('Test', "User", 80000)

print(emp_1.__repr__() + " Helllo guys")

print(emp_1.fullname_email())
print(emp_2.fullname_email())

raised = emp_2.apply_raise()

print('After salary raised by raised amt for emp_2: {}'.format(emp_2.salary))

print("\n\n Developer class starts here:  *******************  \n\n")


class Developer(Employee):
    raise_amt = 5.5

    def __init__(self, first, last, salary, programming_language):
        super().__init__(first, last, salary)
        self.programming_language = programming_language


dev_1 = Developer('Mamat', 'Mamytov', 80000, 'Python')
dev_2 = Developer('Tester', 'Employee', 130200, 'Java')

print(dev_1.fullname_email(), dev_1.programming_language)
print(dev_2.fullname_email(), dev_2.programming_language)

print(dev_1.email)
print(dev_2.email)

print(dev_1.salary)
raised2 = dev_1.apply_raise()
print("After raising salary by raised amt for dev_1: {}".format(raised2))

print("\n\n Manager class starts here:  *******************  \n\n")


class Manager(Employee):

    def __init__(self, first, last, salary, employees=None):
        super().__init__(first, last, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_all_employees(self):
        for emp in self.employees:
            print('---> ' + emp.fullname_email())


manager = Manager('Mark', 'Markovskii', 90000, [dev_1])
manager.print_all_employees()

print('Adding second employee')

manager.add_employee(dev_2)
manager.print_all_employees()

print('\n\nThis is a way to know if instance is belongs to particular class')
print(isinstance(manager, Manager))

print('This is a way to know if class is subclass of particular class')
print(issubclass(Manager, Employee))
