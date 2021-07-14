#! /usr/bin/env python3
import npyscreen
import json
import os

#TODO:
#adjust size of tui
#pipe size of contents variable into select size of tui
#readJson function picks from selected file in tui
#actually pipe the theme from selected theme into a variable

def readDirectory(filepath):
    try:
        contents = os.listdir(filepath)
        themePaths = []
        for i in contents:
            themePaths.append(os.path.join(filepath, i))
        return themePaths

    except:
        return []

def nameParser(list):
    
    if list:
        themeNames = []
        for string in list:
            themeNames.append(string[string.rindex('/')+1:string.rindex('.')])
        return themeNames
    else:
        return []
    

def readSelected(filename):
    if filename:
        data = json.load(open(filename,'r'))
        key = list(data.keys())

        #terrible code lol, json field saves as list with one value for some reason
        string = data[key[0]][0]
        return string
    else:
        return ""


def startSelect(data, selected):
    if data:
        for i, value in enumerate(data):
            print(value)
            if selected in value:
               return i
        return 0
    else:
        return 0 


class App(npyscreen.NPSApp):
    def __init__(self, themes):
        self.themes = themes

    def main(self):

        F = npyscreen.Form(name = "Hello World!",)
        select = F.add(npyscreen.TitleSelectOne, 
                max_height=(len(self.themes)+1), 
                value = [startSelect(readDirectory("./themes"), readSelected("./test.json")),],
                name = "Select Theme",
                values = nameParser(self.themes))
        F.edit()
        
        selectedTheme = {
            "selected_theme":select.get_selected_objects()
        }

        with open("test.json", 'w') as file:
            json.dump(selectedTheme, file)


if __name__ == "__main__":

    app = App(readDirectory("./themes"))
    app.run()
