import datetime

class Person:
   def __init__(self, first_name, last_name, year, month, day):
      self.first_name = first_name
      self.last_name = last_name
      self.birth_year = year
      self.birth_month = month
      self.birth_day = day

   def age(self):
      today = datetime.date.today()
      age = today.year - self.birth_year

      is_birth_month_later = today.month < self.birth_month
      is_birthday_this_month = today.month == self.birth_month
      is_birthday_later = today.day < self.birth_day

      birthday_has_not_come = is_birth_month_later or (
         is_birthday_this_month and is_birthday_later
      )

      if birthday_has_not_come:
         age -= 1
      return age

   def days_until_birthday(self):
      today = datetime.date.today()

      year = today.year
      if today > next_birthday:
         year = today.year + 1

      next_birthday = datetime.date(
         year=year,
         month=self.birth_month,
         day=self.birth_day
      )

      return (next_birthday - today).days

   def personal_info(self):
      return f"{self.first_name} {self.last_name}, age {self.age()} year(s)"