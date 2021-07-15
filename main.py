#! /usr/bin/env python3
import npyscreen
import json
import os

# returns a list of directory contents
def readDir(filepath):
    try:
        contents = os.listdir(filepath)
        themePaths = []
        for i in contents:
            themePaths.append(os.path.join(filepath, i))

        return themePaths
    except:
        return []


# returns a list of filenames from pilepaths
def nameParser(list):
    if list:
        themeNames = []
        for string in list:
            themeNames.append(string[string.rindex('/')+1:string.rindex('.')])
        return themeNames
    else:
        return []


# checks selected storage file to return a string of previously selected option
# needs refactor
def readSelected(filename):
    if filename:
        data = json.load(open(filename,'r'))

        #terrible code lol, json field saves as list with one value for some reason
        string = data["selected_theme"]
        return string
    else:
        return ""

# returns index of selected theme
def startSelect(data, selected):
    if data:
        for i, value in enumerate(data):
            print(selected, value)
            if selected in value:
               return i
        return 0
    else:
        return 0 


class App(npyscreen.NPSApp):
    def __init__(self, themes):
        self.themes = themes

    def main(self):
       
        value = []
        if (len(self.themes)) > 0:
            value = [startSelect(readDir("./themes"), readSelected("./test.json")),] 
        else:
            value = None

        name =  "Select Theme" if len(self.themes) > 0 else "No Themes"
        values = nameParser(self.themes)

        F = npyscreen.Form(name = "Kitty Theme",)
        select = F.add(npyscreen.TitleSelectOne, max_height=(len(self.themes)+2), value = value, name = name, values = values)

        F.edit()
        
        # write selected theme to file
        if len(self.themes) > 0:
            selectedTheme = {
                "selected_theme":select.get_selected_objects()[0]
            }
            with open("test.json", 'w') as file:
                json.dump(selectedTheme, file)


if __name__ == "__main__":
    
    app = App(readDir("./themes"))
    app.run()
