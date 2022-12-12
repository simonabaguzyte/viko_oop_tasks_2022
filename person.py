import datetime

class Person:
   def __init__(self, first_name, last_name, date_of_birth):
      self.validate_first_name(first_name)
      self.validate_last_name(last_name)

      date_of_birth = datetime.datetime.strptime(date_of_birth, "%Y-%m-%d")
      self.validate_date_of_birth(date_of_birth)
      
      self.first_name = first_name
      self.last_name = last_name
      self.birth_year = int(date_of_birth.year)
      self.birth_month = int(date_of_birth.year)
      self.birth_day = int(date_of_birth.year)

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

   def validate_first_name(self, first_name):
      if first_name == None or first_name.strip() == "":
         raise ValueError("First name must not be null or whitespace")

   def validate_last_name(self, last_name):
      if last_name == None or last_name.strip() == "":
         raise ValueError("Last name must not be null or whitespace")
         
   def validate_date_of_birth(self, date_of_birth):
      if date_of_birth.date() > datetime.date.today():
         raise ValueError("Date of birth cannot be later than today's date")


