from datetime import datetime, timedelta

class Field:
    pass

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Name(Field):
    def __init__(self, value):
        self.value = value

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit():
            raise ValueError("Phone number must contain only digits")
        self.value = value

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def days_to_birthday(self):
        if self.birthday:
            today = datetime.today()
            next_birthday = self.birthday.value.replace(year=today.year)
            if next_birthday < today:
                next_birthday = next_birthday.replace(year=today.year + 1)
            return (next_birthday - today).days
        return None

class AddressBook:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_upcoming_birthdays(self, days=7):
        today = datetime.today()
        upcoming_birthdays = []
        for record in self.records:
            if record.birthday:
                days_to_birthday = record.days_to_birthday()
                if days_to_birthday is not None and days_to_birthday <= days:
                    upcoming_birthdays.append(record)
        return upcoming_birthdays

# Перевірка використання
book = AddressBook()
record1 = Record("Inna")
record1.add_phone("1234567890")
record1.add_birthday("01.04.1990")
book.add_record(record1)

record2 = Record("Olga")
record2.add_phone("0987654321")
record2.add_birthday("05.04.1985")
book.add_record(record2)

record3 = Record("Sergiy")
record3.add_phone("5648951356")
record3.add_birthday("05.05.1987")
book.add_record(record3)

record4 = Record("Tanny")
record4.add_phone("11225566488")
record4.add_birthday("03.04.1975")
book.add_record(record4)

upcoming_birthdays = book.get_upcoming_birthdays()
for record in upcoming_birthdays:
    print(f"Name: {record.name.value}, Birthday: {record.birthday.value.strftime('%d.%m.%Y')}")