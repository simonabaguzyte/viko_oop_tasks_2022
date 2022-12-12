class User:
   def __init__(self, person, username, password):
      self.validate_age(person)

      self.person = person
      self.username = username
      self.password = password
      self.picture = None

   def validate_age(self, person):
      if person.age() < 14:
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



      

