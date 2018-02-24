class Employee:

    num_of_emps = 0
    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp1 = Employee('Lily', 'Chen', 20000)
emp2 = Employee('Lucy', 'Lee', 30000)

print"There're %d employees in total." % Employee.num_of_emps
print "%s\'s annual salary is %r." % (emp1.first, emp1.pay)
print "%s\'s full name is %s." % (emp1.first, emp1.fullname())
emp1.apply_raise()
print(emp1.pay)
