from decorators.errors import input_error
from task_bot.classes import AddressBook, Record

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, book: AddressBook):
    # name, phone = args
    # contacts[name] = phone
    # return "Contact added."
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
    # name, phone = args
    # contacts[name] = phone
    # return "Contact updated."
    name, old_phone, new_phone = args
    record = book.find(name)
    record.edit_phone(old_phone, new_phone)
    return "Contact updated."


@input_error
def show_phone(args, book: AddressBook):
    name = args
    record = book.find(name)
    for phone in  record.phones:
        return f"{phone}"
               

@input_error
def show_all(book: AddressBook):
    contacts = book.data
    if len(contacts):
        str_ = ''
        for name, phone in contacts.items():
            str_ += name + ' ' + phone + '\n'
        return str_ 
    else:
        return "Your contacts list is empty."
    

@input_error
def add_birthday(args, book: AddressBook):
    name, bday_date = args
    record = book.find(name)
    record.add_birthday(bday_date)
    return "Birthday date added."


@input_error
def show_birthday(args, book: AddressBook):
    name = args
    record = book.find(name)
    return f"{record.birthday}"


@input_error
def birthdays(book: AddressBook):
    upcoming_bdays = book.get_upcoming_birthdays()
    for bday in upcoming_bdays:
        return f"{bday}"
