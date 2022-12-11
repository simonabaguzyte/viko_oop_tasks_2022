from person import Person
import PySimpleGUI as sg

layout = [
    [sg.Text("First name"), sg.InputText()],
    [sg.Text("Last name"), sg.InputText()],
    [sg.Text("Year of birth"), sg.InputText()],
    [sg.Text("Month of birth"), sg.InputText()],
    [sg.Text("Day of birth"), sg.InputText()],
    [sg.Button("Submit"), sg.Button("Cancel")]
]

window = sg.Window(title="Person creator", layout=layout, margins=(140, 160))

while True:
   event, values = window.read()
   if event in (None, "Cancel"):
      break

   elif event == "Submit":
      try:
         person = Person(values[0], values[1], values[2], values[3], values[4])
         
         sg.popup(f"Person's age is {person.age()} year(s). " +
            f"{person.days_until_birthday()} days left until birthday")

      except ValueError as error:
         sg.popup(str(error))

window.close()