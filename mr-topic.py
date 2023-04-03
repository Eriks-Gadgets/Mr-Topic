#Mr. Topic
#(c) Erik's Gadgets, 2023
import PySimpleGUI as sg
import random
print("Mr. Topic event log")
sg.theme("DarkBrown1")
loading_window = sg.Popup("Mr. Topic\n© Erik's Gadgets, 2023")
mr_window = sg.Window(title="Mr Topic", layout=[[sg.Text("Mr Topic")],[sg.Button("Categories")],[sg.Button("Exit")],[sg.Text("© Erik's Gadgets")]], margins=(100, 50))
while True:
    event, values = mr_window.Read()
    print(event)
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == "Return [1]":
        mr_window.close()
        mr_window = sg.Window(title="Mr Topic", layout=[[sg.Text("Mr Topic")],[sg.Button("Categories")],[sg.Button("Exit")],[sg.Text("© Erik's Gadgets")]], margins=(100, 50))
    if event == "Categories" or event == "Return [2]":
        mr_window.close()
        mr_window = sg.Window(title="Mr Topic", layout=[[sg.Text("Mr Topic")],[sg.Button("Animals")],[sg.Button("Return [1]")],[sg.Button("Exit")],[sg.Text("© Erik's Gadgets")]], margins=(100, 50))
    if event == "Get Topic":
        if type_of_prompt == 1:
            topic = animals[random.randint(0, animal_index - 1)]
            sg.Popup("Your Topic: \n" + str(topic))
    if event == "Animals":
        mr_window.close()
        type_of_prompt = 1
        animals = ["Bear","Cat","Dog","Fish","Horse","Lion","Monkey","Rabbit","Snake","Zebra"]
        animal_formatting = ""
        animal_index = 0
        for i in animals:
            animal_index += 1
            animal_formatting += "["
            animal_formatting += str(animal_index)
            animal_formatting += "] "
            animal_formatting += i
            if i != animals[-1]:
                animal_formatting += "\n"
        mr_window = sg.Window(title="Mr Topic", layout=[[sg.Text("Mr Topic")],[sg.Text(animal_formatting)],[sg.Button("Get Topic")],[sg.Button("Return [2]")],[sg.Button("Exit")],[sg.Text("© Erik's Gadgets")]], margins=(100, 50))
mr_window.close()

