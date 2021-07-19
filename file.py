import os
import json

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

