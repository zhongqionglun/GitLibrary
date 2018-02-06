from person import Person

class Manager(Person):
    def giveRaise(self, percent, bonus=0.1):
        Person.giveRaise(self, percent+bonus)

    """
    print the attributes of instance
    """
    def __str__(self):
        return '< %s => %s >'%(self.__class__.__name__, self.__dict__)

if __name__ == '__main__':
    tom = Manager(name='Tom Doe', age=50, pay=50000)
    print(str(tom))
    print(tom.lastName())
    tom.giveRaise(.20)
    print(tom.pay)
