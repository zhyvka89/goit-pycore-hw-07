from collections import UserDict
from datetime import datetime, timedelta


class AddressBook(UserDict):
    def add_record(self, record):
        if record.name.value not in self.data:
            self.data[record.name.value] = record
        else:
            print('Contact name already exist.')

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise KeyError('Contact name not found.')

    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            raise KeyError("Record not found.")
        
    def get_congrat_day(date):
        weekday = date.weekday()
        congrat_day = date

        if(weekday == 5):
            congrat_day = date + timedelta(days=2)
            
        if(weekday == 6):
            congrat_day = date + timedelta(days=1)
            
        return congrat_day.strftime("%Y.%m.%d")


    def get_upcoming_birthdays(self):
        current_date = datetime.today().date()
        list_of_upcoming_bdays = []

        for user in self.data:
            user_obj = {}
            user_obj["name"] = user["name"]
            
            bday_obj = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
            bday_day = bday_obj.day
            bday_month = bday_obj.month

            bday_this_year = datetime(
            year=current_date.year, month=bday_month, day=bday_day).date()
            bday_next_year = datetime(
                year=current_date.year+1, month=bday_month, day=bday_day).date()
            
            if (bday_this_year < current_date):
                user_obj["congratulation_date"] = self.get_congrat_day(bday_next_year)
            else:
                user_obj["congratulation_date"] = self.get_congrat_day(bday_this_year)
                diff = bday_this_year - current_date
                time_delta = timedelta(7)
                if (diff <= time_delta):
                    print(f"We will celebrate bday of {user['name']} this week!!!")
            
            list_of_upcoming_bdays.append(user_obj)

        return list_of_upcoming_bdays