class Customer:
    def __init__(self,first_name, last_name, age, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.birth_date = birth_date
        self.cus_active_fl = 'Y'
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    #Print all the fields

    def str_customer(self):
        print('first name: ', self.first_name, 'last name: ', self.last_name, 
              'age: ',self.age, 'birth date: ', self.birth_date)

class CustomerSalary:
    def __init__(self, salary, increment):
        self.salary = salary
        self.increment = increment
    
    def get_salary(self):
        return self.salary
    def get_increment(self):
        return self.increment

    def srt_sal_incre(self):
        print('Salary:',self.salary, 'increment:', self.increment)


