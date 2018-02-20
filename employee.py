class Employee:
    #first, last, pay are arguements
    #self is taken as an instance
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    #fullname() is a method
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

#emp1 is an instance of Employee; Lily = first, Chen = last, 100000 = pay
emp1 = Employee('Lily', 'Chen', 100000)
emp2 = Employee('Lucy', 'Lee', 800000)

print "%s\'s email is %s." % (emp1.first, emp1.email)
print(emp1.fullname())
print(Employee.fullname(emp2))
