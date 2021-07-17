#! /usr/bin/env python3
import npyscreen
import json
import os
import util

# returns a list of filenames from pilepaths

# -------------------Filesystem related stuff--------------------

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

def writeSelected(selected, filename):
    selectedTheme = {
        "selected_theme":selected
    }
    with open(filename, 'w') as file:
        json.dump(selectedTheme, file)

# returns index of selected theme


class App(npyscreen.NPSApp):

    def __init__(self, themes):
        self.themes = themes
        self.selected = 0


    def startSelect(self, data, selected):
        if data:
            for i, value in enumerate(data):
                print(selected, value)
                if selected in value:
                   self.selected = i

    def main(self):
       
        value = []
        if (len(self.themes)) > 0:
            value = [self.startSelect(readDir("./themes"), readSelected("./test.json")),] 
        else:
            value = None

        name =  "Select Theme" if len(self.themes) > 0 else "No Themes"
        values = util.nameSplitter(self.themes)

        F = npyscreen.Form(name = "Kitty Theme", lines=20)
        select = F.add(
                npyscreen.TitleSelectOne, 
                max_height=(len(self.themes)+2), 
                value = value, 
                name = name, 
                values = values)

        F.edit()
        
        # write selected theme to file
        if len(self.themes) > 0:
            writeSelected(select.get_selected_objects()[0], 'test.json')


if __name__ == "__main__":
    
    app = App(readDir("./themes"))
    app.run()
