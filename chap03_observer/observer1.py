"""
ソフトウェアでは、ある値が変わるとそれに呼応して別の部分も変化する、というものがよくあります。

例えば、表計算ソフトでセルの値を変更すると、グラフのバーが伸び縮みする等。
Observerパターンでは、あるオブジェクトに何かがおきたとき、
登録されたオブザーバーにそれを通知します。

例えば、会計システムを考えます。
従業員が昇給・減給したとき、それを経理部に通知しなくてはなりません。

しかも、通知するべき相手といえば経理部に限りません。新たに増えるかも。
通知する相手を集めて管理してしまいましょう。

このような何かのニュースを通知するパターンを、Observerパターンと言います。
通知する側（今回はEmployee）はSubject、通知される側（TaxmanやPayroll）はObserverと呼ばれます。


ところでこのソースでは、

    observer(self)

と、オブザーバーにサブジェクト自身を渡し、
オブザーバーが自分で詳細情報を引っ張り出していますが（Pull型）、

    observer(self.name, self.title, self.salary)

のように、サブジェクトの側で詳細情報をオブザーバーに渡す（Push型） やり方もあります。

Push型は、オブザーバーの側が監視のために一々情報を引っ張りだす必要がないので楽ですが、
反面、サブジェクト側の負担になります。
"""


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
        """
        :type changed_employee: Employee
        """
        print(f"{changed_employee.name}のために小切手を切ります！")
        print(f"{changed_employee.name}の給料は現在{changed_employee.salary}円、"
              f"肩書きは{changed_employee.title}です")


class Taxman:
    @staticmethod
    def update(changed_employee):
        """
        :type changed_employee: Employee
        """
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
