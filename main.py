#! /usr/bin/env python3
import npyscreen
import json
import os

#TODO:
#adjust size of tui
#pipe size of contents variable into select size of tui
#readJson function picks from selected file in tui



def readDirectory(filepath):
    try:
        contents = os.listdir(filepath)
        for i in contents:
            print(i)
            return os.path.join(filepath, i)
    except:
        print("directory does not exist")
        return


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
        F.add(npyscreen.TitleSelectOne, 
                max_height=(len(themes)+1), 
                value = [0,], 
                name = "Select Theme",
                values = themes)
        F.edit()

if __name__ == "__main__":
    
    readJson(readDirectory("./themes"))
    # readJson()
    themes = ["Nord", "Gruvbox", "Solarized", "One Dark"]
    app = App(themes)
    # app.run()
