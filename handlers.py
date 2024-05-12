from decorators.errors import input_error
from classes.AddressBook import AddressBook
from classes.Record import Record


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message
  

@input_error
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone = args
    record = book.find(name)
    if(record):
        record.edit_phone(old_phone, new_phone)
        return "Contact updated."
    else:
        raise AttributeError('Please, first create contact with command "add [name] [phone]".')


@input_error
def show_phone(args, book: AddressBook):
    name, *_ = args
    if(record):
        record = book.find(name)
        return f"{'; '.join(p.value for p in record.phones)}"
    else:
        raise AttributeError('Please, first create contact with command "add [name] [phone]".')
    

@input_error
def show_all(book: AddressBook):
    contacts = book.data
    if len(contacts):
        str_ = ''
        for name, record in contacts.items():
            phones = record.phones
            str_ += f"Contact name: {name}, phones: {'; '.join(p.value for p in phones)}" + '\n'
        return str_ 
    else:
        return "Your contacts list is empty."
    

@input_error
def add_birthday(args, book: AddressBook):
    name, bday_date = args
    record = book.find(name)
    if(record):
        record.add_birthday(bday_date)
        return "Birthday date added."
    else:
        raise AttributeError('Please, first create contact with command "add [name] [phone]".')


@input_error
def show_birthday(args, book: AddressBook):
    name, *_ = args
    record = book.find(name)
    if(record.birthday):
        return f"{record.birthday}"
    else:
        return "No birthday date."


@input_error
def birthdays(book: AddressBook):
    upcoming_bdays = book.get_upcoming_birthdays()
    str_ = ''
    for bday in upcoming_bdays:
        str_ += f"{bday}" + '\n'
    return str_
