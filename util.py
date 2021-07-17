import json


# figure out what this returns (a dict with line numbers corresponding to settings perhaps?)
# need to figure out the flow of this project before I continue I feel.
def parseKitty():
    
    # successfully parses my kitty conf file, just gotta work on changing it now
    # kitty = open("./kitty.conf", "wt")
    theme = open("theme.conf", "rt")

    if theme:
        cond = True
        color_count = 0
        line_count = 0

        initial_color = 0
        
        # runs through 
        while cond: 

            line = theme.readline()
            line_count += 1
            color = "color" + str(color_count) + " "

            if not line and color_count < 15:
                line_count = 0
                theme.seek(initial_color)

            elif color in line:
                if color_count == 0:
                    initial_color = line_count

                color_count += 1

                #removes \n just from print (keep it for actual file)
                print(line.strip('\n'))

            elif color_count > 15:
                cond = False
    else:
        return

def nameSplitter(paths: list):
    if paths:
        themeNames = []
        for string in paths:
            themeNames.append(string[string.rindex('/')+1:string.rindex('.')])
        return themeNames
    else:
        return []

def validateTheme(data: dict):

    theme_keys = list(data.keys())

    # available kitty color theming options
    kitty_theme_options = ['color0','color1','color2','color3','color4','color5','color6','color7','color8', 'color9','color10','color11','color12','color13','color14','color15','background', 'foreground', 'selection_background', 'selection_foreground']

    check_theme = 0
    validated_theme = len(theme_keys)

    # checks that all options in theme.json file are valid
    for i in range(len(theme_keys)):
        for option in kitty_theme_options:
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

def replace(theme: dict):
    if not validateTheme(theme):
        return 0 

    else: 
        return 1


if __name__ == "__main__":
    # parseKitty()
    data = json.load(open('./themes/gruvbox.json', 'r'))
    print(validateTheme(data))


