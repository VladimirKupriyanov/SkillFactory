class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


# Task 1.10.3
# В  проекте «Дом питомца» предполагается новая услуга: электронный кошелек.
# То есть система будет хранить данные о своих клиентах и их финансовых операциях.
# Вам нужно написать программу, обрабатывающую данные, и на выходе в консоль
# получить следующее: Клиент «Иван Петров». Баланс: 50 руб.
class Client(Person):
    balance = None

    def __init__(self, name, balance=0):
        Person.__init__(self, name)
        self.balance = balance

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        if isinstance(balance, int):
            self.balance += balance

    def __str__(self):
        return f"Клиент <<{self.get_name()}>>. Баланс: {self.get_balance()} руб."


client1 = Client("Иван Петров", 100)
client2 = Client("Peter Robertson", 80)
client3 = Client("Julia Donaldson", 90)

print(str(client1), str(client2), str(client3), sep="\n")
print("\nИзменение баланса:")

client1.set_balance(-50)
client2.set_balance(20)
client3.set_balance(-70)

print(str(client1), str(client2), str(client3), sep="\n", end="\n\n\n")


# Task 1.10.4
# Команда проекта «Дом питомца» планирует большой корпоратив для своих волонтеров.
# Вам необходимо написать программу, которая позволяла бы составлять список нескольких гостей.
# Решите задачу с помощью метода конструктора и примените один из принципов наследования.
# При выводе в консоль вы должны получить:  «Иван Петров, г. Москва, статус "Наставник"»
class Volunteer(Person):
    def __init__(self, name, city, status):
        Person.__init__(self, name)
        self.city = city
        self.status = status

    def get_city(self):
        return self.city

    def get_status(self):
        return self.status

    def __str__(self):
        return f'«{self.get_name()}, г. {self.get_city()}, статус "{self.get_status()}"»'


class GuestList:
    def __init__(self, name, guest_list=None):
        self.name = name
        if guest_list is None:
            guest_list = []
        self.guest_list = guest_list

    def get_name(self):
        return self.name

    def add_guest(self, guest):
        return self.guest_list.append(str(guest))

    def get_guest_list(self):
        if self.guest_list:
            print(f'\t\t"{self.get_name()}"\nСписок гостей:')
            guest_list = ""
            for i in range(len(self.guest_list)):
                guest_list += f"{self.guest_list[i]}\n"
            return guest_list

guest1 = Volunteer("Иван Петров", "Москва", "Наставник")
guest2 = Volunteer("Peter Robertson", "Лондон", "Writer")
guest3 = Volunteer("Julia Donaldson", "Нью-Йорк", "Manager")

office_party = GuestList("Корпоратив для волонтеров")
office_party.add_guest(guest1)
office_party.add_guest(guest2)
office_party.add_guest(guest3)
print(office_party.get_guest_list())
