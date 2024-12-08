class person:
    def __init__(self, idnumber, name, net_worth):
        self.idnumber = idnumber
        self.name = name
        self.net_worth = net_worth
    def display(self):
            print(self.idnumber)
            print(self.name)
class employee(person):
    def __init__(self, idnumber, name, net_worth, post, salary):
        self.salary = salary
        self.post = post
        person.__init__(self, idnumber, name, net_worth)
a = employee('raul',987, 1000000, "intern", 10000)
a.display()   