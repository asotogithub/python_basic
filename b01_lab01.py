from persistence.Customers import Customer, CustomerSalary
import datetime
class Main:
    print(datetime.datetime.now())
    def __init__(self):
        pass


    print("Instanciar una Clase Customer")
    cli1 = Customer('Abel','Soto', 45, '10-05-1979')
    print(cli1.get_first_name())
    print(cli1.first_name)

    cli1.str_customer()
    cli1Salary = CustomerSalary(2345.4,200)
    cli1Salary.srt_sal_incre()

