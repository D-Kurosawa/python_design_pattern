class Employee:
    def __init__(self, name, title, salary):
        self.name = name
        self.title = title
        self.salary = salary
        self.observers = set()

    def set_salary(self, new_salary):
        self.salary = new_salary
        for observer in self.observers:
            observer(self)

    def add_observer(self, observer):
        self.observers.add(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)


class Payroll:
    @staticmethod
    def update(changed_employee):
        print(f"{changed_employee.name}のために小切手を切ります！")
        print(f"{changed_employee.name}の給料は現在{changed_employee.salary}円、"
              f"肩書きは{changed_employee.title}です")


class Taxman:
    @staticmethod
    def update(changed_employee):
        print(f"{changed_employee.name}に新しい税金の請求書を送ります。")


if __name__ == "__main__":
    payroll = Payroll()
    taxman = Taxman()

    fred = Employee("フレッド", "クレーン技師", 300 * 10000)
    fred.add_observer(payroll.update)
    fred.add_observer(taxman.update)
    fred.set_salary(350 * 10000)

    print()

    fred.remove_observer(taxman.update)
    fred.set_salary(400 * 10000)
