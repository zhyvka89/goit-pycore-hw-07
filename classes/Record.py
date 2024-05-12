from classes.Birthday import Birthday
from classes.Name import Name
from classes.Phone import Phone


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def add_birthday(self, bday_date):
        self.birthday = Birthday(bday_date)

    def remove_phone(self, phone_number):
        if phone_number in self.phones:
            self.phones.remove(phone_number)
        else:
            raise ValueError('Phone number does not exist.')
        
    def edit_phone(self, old_phone_number, new_phone_number):
        for index, phone_number in enumerate(self.phones):
            if phone_number.value == old_phone_number:
                self.phones[index] = Phone(new_phone_number)

    def find_phone(self, phone_number):
        for number in self.phones:
            if number.value == phone_number:
                return phone_number
            
        