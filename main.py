from person import Person
from user import User
import PySimpleGUI as sg

logged_in_user = None
admin_person = Person("Name1", "Surname1", "1980-01-01")
admin_user = User(admin_person, "admin", "admin123")

users = []

def open_anonymous_window():
   anonymous_layout = [
      [sg.Text("Welcome")],
      [sg.Text("You are currently anonymous")],
      [sg.Button("Login"), sg.Button("Register"), sg.Button("Leave")]
   ]
   return sg.Window(title="User portal", layout=anonymous_layout)

def open_registration_window():
   registration_layout = [
      [sg.Text("First name  "), sg.InputText(key="first_name")],
      [sg.Text("Last name  "), sg.InputText(key="last_name")],
      [
         sg.Text("Date of birth"),
         sg.Input(size=(20,1), key="date_of_birth", disabled=True),
         sg.CalendarButton("Choose", target=(2,1), format="%Y-%m-%d")
      ],
      [sg.Text("Username   "), sg.InputText(key="username")],
      [sg.Text("Password   "), sg.InputText(key="password", password_char="*")],
      [sg.Button("Submit"), sg.Button("Cancel")]
   ]
   return sg.Window(title="Registration", layout=registration_layout)

def open_registered_window():
   registered_layout = [
      [sg.Text("You are currently logged in as registered user")],
      [sg.Button("Edit personal info"), sg.Button("Leave"), sg.Button("Log out")]
   ]
   return sg.Window(title="User portal", layout=registered_layout)

def open_login_window():
   login_layout = [
      [sg.Text("Username"), sg.InputText(key="username")],
      [sg.Text("Password"), sg.InputText(key="password", password_char="*")],
      [sg.Button("Sign in"), sg.Button("Cancel")]
   ]
   return sg.Window(title="Login", layout=login_layout)

def open_admin_window():
   admin_layout = [
      [sg.Text("You are currently logged in as an admin")],
      [sg.Button("Edit personal info"), sg.Button("View list of users"), sg.Button("Leave")]
   ]
   return sg.Window(title="Admin portal", layout=admin_layout)

def open_edit_window():
   choose_picture = "Choose profile picture"
   if logged_in_user.picture != None:
      choose_picture = logged_in_user.picture

   edit_info_layout = [
      [sg.Text("Edit profile picture")],
      [sg.Text(choose_picture), sg.FileBrowse(key="uploaded_image")],

      [sg.HorizontalSeparator()],

      [sg.Text("Change password")],
      [sg.Text("Old password "), sg.InputText(key="old_password", password_char="*")],
      [sg.Text("New password"), sg.InputText(key="new_password", password_char="*")],

      [sg.Text("")],
      [sg.Button("Save"), sg.Button("Cancel")]
   ]

   return sg.Window(title="Edit personal information", layout=edit_info_layout, margins=(200,220))

def open_list_of_users():
   user_list_layout = [
    [sg.Text("Select a user from the list:")],
    [sg.Listbox(values=users, size=(30, len(users)), key="user_list")],
    [sg.Button("Delete user"), sg.Button("Cancel")]
]
   return sg.Window(title="List of users", layout= user_list_layout, margins=(200,220))


def register_user(values):
   first_name = values["first_name"]
   last_name = values["last_name"]
   date_of_birth = values["date_of_birth"]
   username = values["username"]
   password = values["password"]

   person = Person(first_name, last_name, date_of_birth)
   user = User(person, username, password)
   return user

def check_user(values):
   username = values["username"]
   password = values["password"]

   is_admin = password == admin_user.password and username == admin_user.username

   if is_admin:
      return admin_user

def edit_user(values):
   profile_picture = values["uploaded_image"]
   old_password = values["old_password"]
   new_password = values["new_password"]

   is_old_password_entered = old_password != None and old_password.strip() != ""
   is_new_password_entered = new_password != None and new_password.strip() != ""

   if is_old_password_entered and is_new_password_entered:
      logged_in_user.update_password(old_password, new_password)
   elif is_old_password_entered or is_new_password_entered:
      raise ValueError("One of password fields is empty")

   if profile_picture != None and profile_picture.strip() != "":
      logged_in_user.upload_picture(profile_picture)

def decide_which_window():
   if logged_in_user is not None and logged_in_user != admin_user:
      return open_registered_window()
   elif logged_in_user is not None and logged_in_user == admin_user:
      return open_admin_window()
   else:
      return open_anonymous_window()

window = open_anonymous_window()
# window = decide_which_window()

while True:
   event, values = window.read()
   if event in (None, "Leave"):
      break

   elif event == "Log out":
      window.close()
      window = open_anonymous_window()

   elif event == "Cancel":
      window.close()
      window = decide_which_window()

   elif event == "Register":
      window.close()
      window = open_registration_window()

   elif event == "Login":
      window.close()
      window = open_login_window()

   elif event == "Submit":
      try:
         logged_in_user = register_user(values)
         users.append(logged_in_user)
         window.close()
         window = decide_which_window()
      except Exception as error:
         sg.popup(str(error))
   
   elif event == "Edit personal info":
      window.close()
      window = open_edit_window()

   elif event == "Save":
      try:
         edit_user(values)
         window.close()
         if logged_in_user == admin_user:
            window = open_admin_window()
         else:
            window = open_registered_window()

      except Exception as error:
         sg.popup(str(error))
   
   elif event == "Sign in":
      try:
         logged_in_user = check_user(values)
         window.close()
         window = decide_which_window()
      except Exception as error:
         sg.popup(str(error))

   elif event == "View list of users":
      window = open_list_of_users()

   elif event == "Delete user":
       selected_user = values['user_list'][0]
       users.remove(selected_user)
       window['user_list'].update(values=users)

window.close()
