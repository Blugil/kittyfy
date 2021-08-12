import os
import json
import kitty


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


#takes list of filepaths as strings
def nameSplitter(paths: list) -> dict:
    if paths:
        combined = {}
        for i, string in enumerate(paths):
            # grabs filename from file path 
            combined[string[string.rindex('/')+1:string.rindex('.')]] = paths[i]
        return combined
    else:
        return {}


# validates that a theme contains *only* the available kitty theme config options
def validateTheme(data: dict) -> bool:

    theme_keys = list(data.keys())

    # available kitty color theming options

    check_theme = 0
    validated_theme = len(theme_keys)

    # checks that all options in theme.json file are valid
    for i in range(len(theme_keys)):
        for option in kitty.kitty_theme_options:
            try:
                if theme_keys[i] == option:
                    check_theme += 1
                    break
            except:
                print('Exception handled')
                return False
    if check_theme == validated_theme:
        return True
    else:
        return False

def startSelect(data: list, selected: str) -> int:
    if data and selected:
        for i, value in enumerate(data):
            print(selected, value)
            if selected in value:
               return i
        return 0
    else: 
        return 0

if __name__ == "__main__":
    
    themes = readDir('./themes')
    selected = readSelected('./selected.json')

    nameSplitter(themes)
    
    print(startSelect(themes, selected[0]))


