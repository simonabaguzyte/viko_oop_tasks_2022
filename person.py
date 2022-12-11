import datetime

class Person:
   def __init__(self, first_name, last_name, year, month, day):
      self.first_name = first_name
      self.last_name = last_name
      self.birth_year = int(year)
      self.birth_month = int(month)
      self.birth_day = int(day)

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

      next_birthday = datetime.date(
         year=today.year,
         month=self.birth_month,
         day=self.birth_day
      )
      
      has_birthday_passed = today > next_birthday 
      if has_birthday_passed:
         next_birthday = next_birthday.replace(year=today.year + 1)
         
      return (next_birthday - today).days

   def personal_info(self):
      return f"{self.first_name} {self.last_name}, age {self.age()} years"


person1 = Person("Laura", "Harris", "1986", "12", "01")
print(person1.first_name)
print(person1.last_name)
print(person1.birth_year)
print(person1.birth_month)
print(person1.birth_day)
print(person1.age())
print(person1.days_until_birthday())
print(person1.personal_info())

