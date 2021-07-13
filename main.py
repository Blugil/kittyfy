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
        print("directory does not exist")
        return

def nameParser(list):
    
    themeNames = []
    for string in list:
        themeNames.append(string[string.rindex('/')+1:string.rindex('.')])

    return themeNames
    

def readJson(filename):
    if filename:
        data = json.load(open(filename,'r'))
        print(data)
    else:
        print("download a theme!")


class App(npyscreen.NPSApp):
    def __init__(self, themes):
        self.themes = themes

    def main(self):
        F = npyscreen.Form(name = "Hello World!",)
        select = F.add(npyscreen.TitleSelectOne, 
                max_height=(len(self.themes)+1), 
                value = [0,], 
                name = "Select Theme",
                values = nameParser(self.themes))
        F.edit()
        
        selectedTheme = {
            "test":select.get_selected_objects()
        }

        with open("test.json", 'w') as file:
            json.dump(selectedTheme, file)


if __name__ == "__main__":
    
    # themes = ["Nord", "Gruvbox", "Solarized", "One Dark"]
    app = App(readDirectory("./themes"))
    app.run()
