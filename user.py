from person import Person

class User(Person):
   def __init__(self, first_name, last_name, date_of_birth, username, password):
      super().__init__(first_name, last_name, date_of_birth)

      self.validate_age()
      self.username = username
      self.password = password
      self.picture = None

   def validate_age(self):
      if self.age() < 14:
         raise ValueError("User's age cannot be less than 14")

   def update_password(self, old_password, new_password):
      if self.password == old_password:
         self.password = new_password
      else:
         raise ValueError("Old password does not match the current password")

   def upload_picture(self, profile_picture):
      self.picture = profile_picture

   def __str__(self):
      return f'{self.username}'



      

